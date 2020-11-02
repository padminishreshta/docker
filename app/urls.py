from django.urls import path

from app.views import ArticleDetailView
from app.views import ArticleWeekArchiveView

urlpatterns = [
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
     path('<int:year>/week/<int:week>/',ArticleWeekArchiveView.as_view(),name="archive_week"),
]

