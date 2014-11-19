from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from website.views import test_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'techpatron.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', test_view),
)
