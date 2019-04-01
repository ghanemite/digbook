from django.conf.urls import include, url
from django.contrib import admin

from bookmarks import urls as b_urls
urlpatterns = [
    # Examples:
    # url(r'^$', '_digbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(b_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
