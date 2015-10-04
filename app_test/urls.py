# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from app_test.views import view_update_database
from app_test.views import view_predict_way1

urlpatterns = patterns('',
                       url(r'^$', 'app_test.views.rb'),
                       url(r'update_db',view_update_database),
                       url(r'way1',view_predict_way1)
)