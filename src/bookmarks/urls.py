from django.conf.urls import url

from .views import main_page,user_page

urlpatterns = [
    url(r'^$', main_page, name='home'),
    url(r'^user/(\w+)/$', user_page, name='user_page'),
]