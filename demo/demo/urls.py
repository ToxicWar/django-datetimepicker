from django.conf.urls import patterns, url

urlpatterns = patterns('demo.views',
    url(r'^$', 'index', name='Index'),
)
