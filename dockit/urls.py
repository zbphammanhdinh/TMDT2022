from django.contrib import admin
from django.urls import path
from .views import index, logout_user
from .views import host_stats
from .views import docker_images, search_images, pull_image, pull_image_progress, launch_image, remove_image
from .views import container_list, container_details, start_container, restart_container, stop_container, edit_container, delete_container, container_stats
from .views import users_list, new_user, edit_user, delete_user, change_password, container_diff, terminal
from .views import ip_list, new_ip, edit_ip, delete_ip, backup_container, ssh_access, container_top, container_info
from django.urls import include, re_path

urlpatterns = [
    path("", index, name="index"),
    re_path(r'^logout/$', logout_user, name='logout'),
    re_path(r'^host_stats/$', host_stats, name='host_stats'),
    re_path(r'^images/$', docker_images, name='docker-images-list'),
    
    re_path(r'^images/search$', search_images, name='search-images'),
    re_path(r'^images/pull/(?P<uuid_token>[-\w]+)/$', pull_image, name='pull-image'),
    re_path(r'^images/pull-progress/(?P<uuid_token>[-\w]+)/$', pull_image_progress, name='pull-image-progress'),
    re_path(r'^images/(?P<name>.+)/launch/$', launch_image, name='launch-image'),
    re_path(r'^images/(?P<name>.+)/remove/$', remove_image, name='remove_image'),

    re_path(r'^container/list/$', container_list, name='container-list'),
    re_path(r'^container/(?P<container_id>[-\w]+)/$', container_details, name='container-details'),
    re_path(r'^container/(?P<container_id>[-\w]+)/start/$', start_container, name='start-container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/restart/$', restart_container, name='restart-container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/stop/$', stop_container, name='stop-container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/edit/$', edit_container, name='edit_container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/delete/$', delete_container, name='delete_container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/stats/$', container_stats, name='container_stats'),
    re_path(r'^container/(?P<container_id>[-\w]+)/backup/$', backup_container, name='backup_container'),
    re_path(r'^container/(?P<container_id>[-\w]+)/change-password/$', change_password, name='change_password'),
    re_path(r'^container/(?P<container_id>[-\w]+)/ssh-access/$', ssh_access, name='ssh_access'),
    re_path(r'^container/(?P<container_id>[-\w]+)/top/$', container_top, name='top'),
    re_path(r'^container/(?P<container_id>[-\w]+)/(?P<total>[-\w]+)/diff/$', container_diff, name='diff'),
    re_path(r'^container/(?P<container_id>[-\w]+)/terminal/$', terminal, name='terminal'),
    re_path(r'^container/info/(?P<container_id>[-\w]+)/$', container_info, name='container_info'),
    # users
    re_path(r'^settings/users/$', users_list, name='users-list'),
    re_path(r'^settings/users/new/$', new_user, name='new-user'),
    re_path(r'^settings/users/(?P<pk>\d+)/edit/$', edit_user, name='edit-user'),
    re_path(r'^settings/users/(?P<pk>\d+)/delete/$', delete_user, name='delete-user'),
    # ip address
    re_path(r'^settings/ip/list/$', ip_list, name='ip-list'),
    re_path(r'^settings/ip/new/$', new_ip, name='new-ip'),
    re_path(r'^settings/ip/(?P<pk>\d+)/edit/$', edit_ip, name='edit-ip'),
    re_path(r'^settings/ip/(?P<pk>\d+)/delete/$', delete_ip, name='delete-ip'),
]