from django.conf.urls import patterns, url
import app_test

urlpatterns = patterns('',
    url(r'^just_test/', 'app_test.views.just_test'),
    url(r'^about/','app_test.views.pdf_view'),
)