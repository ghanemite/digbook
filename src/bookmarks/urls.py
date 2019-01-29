from django.conf.urls import url
from django.contrib.auth.views import login

from .views import main_page, user_page, logout_page, register_page

urlpatterns = [
    url(r'^$', main_page, name='home'),
    url(r'^user/(\w+)/$', user_page, name='user_page'),
    url(r'^signup/$', register_page, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
]