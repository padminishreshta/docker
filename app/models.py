from django.db import models

# Create your models here.
class Article(models.Model):
      headline = models.CharField( max_length=50)
      slug = models.CharField(max_length=50,null=True)
      content = models.CharField(max_length=200)
      reporter = models.CharField(max_length=50)
      pub_date = models.DateField()
      def __str__(self):
          return self.headline

