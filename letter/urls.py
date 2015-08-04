# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.list,
        name='list'
    ),
    url(
        regex=r'(?P<pk>[0-9]+)$',
        view=views.detail,
        name='detail'
    ),

]
