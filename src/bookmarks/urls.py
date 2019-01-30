from django.conf.urls import url
from django.contrib.auth.views import login

from .views import (main_page, user_page, logout_page, 
                    register_page, bookmark_save_page, 
                    tag_page, tag_cloud_page)

urlpatterns = [
    # main views
    url(r'^$', main_page, name='home'),
    url(r'^user/(\w+)/$', user_page, name='user_page'),
    url(r'^tag/$', tag_cloud_page, name='tags_page'),
    url(r'^tag/(\d+)/$', tag_page, name='tag_page'),

    # session management
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', register_page, name='signup'),
    url(r'^logout/$', logout_page, name='logout'),

    # account and actions
    url(r'^save/$', bookmark_save_page, name='save'),

]