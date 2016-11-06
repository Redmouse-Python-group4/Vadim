from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from article.models import Article
# Create your models here.


class Comments(models.Model):
    body = models.CharField(max_length = 1000)
    author = models.ForeignKey(User, blank=True)
    article = models.ForeignKey(Article)
    enable = models.BooleanField(default = True)
    pub_date = models.DateTimeField(auto_now_add = True)
    patch_date = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "Comment to %s" % self.article.title
