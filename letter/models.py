from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    category = models.ForeignKey("Category")

    def __unicode__(self):
        return self.name


class Letter(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField()
    category = models.ForeignKey("Category")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('letter:detail', args=(str(self.pk),))
