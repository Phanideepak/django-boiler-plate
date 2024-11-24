from . import views
from django.urls import path

urlpatterns = [
    path("", views.StartingPageView.as_view(), name = 'starting_page'),
    path("posts", views.AllPostsView.as_view(), name = 'posts_page'),
    path("posts/<slug>", views.SinglePostView.as_view(), name = 'post_detail_page'),
    path('read-later',views.ReadLaterView.as_view(), name='read-later'),
]