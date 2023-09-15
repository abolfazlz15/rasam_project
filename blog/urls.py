from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('articles', views.ArticleListView.as_view(), name='article_list'),
    path('detail/<str:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='article_detail'),

]