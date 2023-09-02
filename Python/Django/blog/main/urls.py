from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.ArticleView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('review/<int:pk>', views.AddComment.as_view(), name='add_comment'),
    path('<int:pk>/<int:comment_pk>/add_comment_like/', views.AddCommentLike.as_view(), name='add_comment_like'),
    path('<int:pk>/<int:comment_pk>/del_comment_like', views.DelCommentLike.as_view(), name='del_comment_like'),
    path('<int:pk>/add_article_like/', views.AddArticleLike.as_view(), name='add_article_like'),
    path('<int:pk>/del_article_like', views.DelArticleLike.as_view(), name='del_article_like'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile', views.profile_view, name='profile'),
]