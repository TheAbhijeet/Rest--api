# from rest_framework.routers import DefaultRouter

# from .views import (
#     UserViewSet,
#     PostViewSet,
# )

# router = DefaultRouter()

# router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)

# urlpatterns = router.urls

from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view(), name = 'post_list'),
    path('page/', views.PageListView.as_view(), name = 'page_list'),
    path('user/', views.UserList.as_view(), name = 'user_list' ),
    path('user/create', views.UserCreateView.as_view(), name = 'user_create' ),
    path('post/<int:slug>/', views.PostDetailView.as_view(), name = 'post_deatil'),
    path('post/create/', views.PostCreateView.as_view(), name = 'post_create'),
    path('comment/', views.CommentListView.as_view(), name = 'comment_list'),
    path('comment/create/', views.CommentCreateView.as_view(), name = 'comment_create'),
    path('post/<int:slug>/edit', views.PostURDView.as_view(), name = 'post_URD'),
    path('useraction/create/', views.CreateUserAction.as_view(), name = 'user_action_create'),
    path('useraction/', views.UserActionListView.as_view(), name = 'user_actions'),






]