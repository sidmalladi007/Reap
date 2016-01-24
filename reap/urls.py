from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^account/$', views.account, name='account'),
    url(r'^new-account/$', views.create_account, name='newaccount'),
    url(r'^myrewards/$', views.myrewards, name='myrewards'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^logout/$', views.signout, name='logout'),
    url(r'^create-reward/$', views.new_reward, name='create'),
    url(r'^reward-added/$', views.add_reward, name='add'),
    url(r'^(?P<reward_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<reward_id>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'^update-radius/$', views.update_radius, name='update_radius'),
]

# Handle signup and profile in one link.