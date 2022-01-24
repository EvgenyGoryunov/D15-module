from django.urls import path
from django.views.decorators.cache import cache_page

from .views import NewsList, NewsDetail, NewsSearch, AddNews, ChangeNews, DeleteNews, add_subscribe, \
    del_subscribe

urlpatterns = [

    # модуль Д4 - вывод инфы из БД, создание новостей, редактирование, удаление и прочее
    path('', NewsList.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='news_search'),

    # модуль Д8 - кэширование страничек о деталях новостей
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
    # cache_page(60*10) - 60 секунд * 10 (=10 минутам, то есть 10 раз по 60 секунд)
    path('<int:pk>/', cache_page(60*10)(NewsDetail.as_view()), name='news_detail'),
    # path('<int:pk>/', (ProductDetailView.as_view()), name='product_detail'),



    # модуль Д5 - регистрация пользователей, ограничение прав доступа к сайту (1)
    path('add/', AddNews.as_view(), name='news_add'),
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),

    # модуль Д6 - подписка на рассылку на статью
    path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),
    path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),

]

#
#
# (1)
# модуль Д5 - регистрация пользователей, ограничение прав доступа к сайту
# добавлено новое представление во view с ограничением прав доступа, изначально ограничиваем права в админ панели,
# там нужно из огромного списка выбрать наше приложения (newapp) и варианты ограничения, такие как
# Can add post например (выбрал еще Can change post, Can delete post), далее эти ограничения привязать к нашим
# представлениям во вьюхах
