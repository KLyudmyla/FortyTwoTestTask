from django.conf.urls import patterns, include, url
from apps.hello import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.detail, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
