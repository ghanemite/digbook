from django.conf.urls import url
from django.contrib.auth.views import login

from . import views 


urlpatterns = [
    # main views
    url(r'^$', views.main_page, name='home'),
    url(r'^user/(\w+)/$', views.user_page, name='user_page'),
    url(r'^tag/$', views.tag_cloud_page, name='tags_page'),
    url(r'^tag/(\d+)/$', views.tag_page, name='tag_page'),
    url(r'^search/$', views.search_page, name='search_page'),

    # session management
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', views.register_page, name='signup'),
    url(r'^logout/$', views.logout_page, name='logout'),

    # account and actions
    url(r'^save/$', views.bookmark_save_page, name='save'),

]