from django.urls import path
from .views import CreateCommentView, LikePostView

urlpatterns = [
    path('comment/<int:post_id>/', CreateCommentView.as_view()),
    path('like/<int:post_id>/', LikePostView.as_view(), name='like-post'),
]
