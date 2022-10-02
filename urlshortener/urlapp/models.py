from email.policy import default
import imp
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class ShortenedUrl(models.Model):
    """
    A modelfor shortened urls
    -------------------------
    slug : The slug for shortened url
    target_url : The url that user will be redirected to
    link: The final shortened url
    date: The time that object was created.
    """
    slug = models.SlugField(unique=True, null=True)
    target_url = models.URLField(default='http://www.google.com')
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.link}'

@receiver(post_save, sender=ShortenedUrl)
def create_url_link(sender, instance, created, **kwargs):
    """
    Creates final link from slug and current site domain
    """
    if created:
        instance.link = f'http://{settings.SITE_DOMAIN}/url/{instance.slug}'
        instance.save()
