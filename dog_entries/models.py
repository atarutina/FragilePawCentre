from django.db import models
from django.utils import timezone


# Create your models here.
class DogEntry(models.Model):
    author = models.ForeignKey('volunteers.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    height = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ['-published_date']
