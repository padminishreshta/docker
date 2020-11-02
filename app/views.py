from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.dates import WeekArchiveView
from app.models import Article

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = "%U"
    allow_future = True    


                      