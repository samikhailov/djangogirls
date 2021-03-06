from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
