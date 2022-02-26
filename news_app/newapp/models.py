from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    # рейтинг пользователя
    ratingAuthor = models.SmallIntegerField(default=0)

    # метод обновления рейтинга пользователя, суммарный рейтинг пользователя за его посты
    # лайки и прочее
    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating', )
        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating', )
        # складываем две переменные, рейтинг за статью (посты), и рейтинг за комменты
        self.ratingAuthor = pRat * 3 + cRat
        # сохранение модели в БД
        self.save()

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.authorUser}'


# Категории новостей/статей — темы, которые они отражают (спорт, политика,образование и т. д.).
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    # Модуль Д6
    subscribers = models.ManyToManyField(User, )

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.name}'

    # функция абсолютный путь
    # def get_absolute_url(self):
    #     return reverse('news_category', kwargs={'category_id': self.pk})


# Модель статьй и новостей
class Post(models.Model):
    # связь «один ко многим» с моделью Author;
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')  # default="John",
    # поле с выбором — «статья» или «новость»;
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE,
                                    verbose_name='Категория')
    # автоматически добавляемая дата и время создания;
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 verbose_name='Категория')  # default="Nature",
    # заголовок статьи/новости;
    title = models.CharField(max_length=128, verbose_name='Название')
    # текст статьи/новости;
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    # метод (функция) описания лайков и дизлайков
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    # превью статьи, мы взяли часть статьи (первые 123 символа) и прибавили многоточие в конце
    def preview(self):
        return self.text[0:123] + '...'

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


class Comment(models.Model):
    # связь «один ко многим» с моделью Post;
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    # текст комментария;
    text = models.TextField()
    # дата и время создания комментария;
    dateCreation = models.DateTimeField(auto_now_add=True)
    # рейтинг комментария.
    rating = models.SmallIntegerField(default=0)

    # метод (функция) описания лайков и дизлайков
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.commentUser}: {self.text[:20]}'
