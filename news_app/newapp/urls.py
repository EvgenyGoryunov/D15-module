from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from newapp import views
# from appointments import views
from .views import *

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewset)
router.register(r'category', views.CategoryViewset)

urlpatterns = [
    # не пашет нихера
    path('indexD15/', TemplateView.as_view(template_name='indexD15.html', extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),

    path('rout/', include(router.urls)),  # модуль Д15 - работа с REST Framework

    path('routapi/', include('rest_framework.urls', namespace='rest_framework')),  # модуль Д15 робота с REST Framework

    path('i18n/', include('django.conf.urls.i18n')),  # модуль Д14 - перевод тестов

    path('indexD14/', Index.as_view(), name='Index'),  # для тестирования создана

    path('', NewsList.as_view(), name='news'),  # модуль Д4 - вывод инфы из БД, создание новостей и пр.
    # cache_page(60*1)
    path('search/', NewsSearch.as_view(), name='news_search'),

    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),  # (8)

    path('add/', AddNews.as_view(), name='news_add'),  # (5)
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),

    path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),  # модуль Д6 - подписка на рассылку новостей
    path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),

]

"""******************************************* Пояснения к коду *************************************************** """

"""
(5)
модуль Д5 - регистрация пользователей, ограничение прав доступа к сайту
добавлено новое представление во view с ограничением прав доступа, изначально ограничиваем права в админ панели,
там нужно из огромного списка выбрать наше приложения (newapp) и варианты ограничения, такие как
Can add post например (выбрал еще Can change post, Can delete post), далее эти ограничения привязать к нашим
представлениям во вьюхах

(8)
модуль Д8 - кэширование страничек о деталях новостей
добавим кэширование на детали товара. Раз в 5 минут товар будет записываться в кэш для экономии ресурсов.
cache_page(60*10) - 60 секунд * 5 (=5 минутам, то есть 5 раз по 60 секунд)


"""
