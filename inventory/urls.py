from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^display_laptop$', views.display_laptop, name="display_laptop"),
    url(r'^display_desktop$', views.display_desktop, name="display_desktop"),
    url(r'^display_mobile$', views.display_mobile, name="display_mobile"),
    url(r'^add_laptop$', views.add_laptop, name="add_laptop"),
    url(r'^add_desktop$', views.add_desktop, name="add_desktop"),
    url(r'^add_mobile$', views.add_mobile, name="add_mobile"),
    url(r'^edit_laptop/(?P<pk>\d+)$', views.edit_laptop, name="edit_laptop"),
    url(r'^edit_desktop/(?P<pk>\d+)$', views.edit_desktop, name="edit_desktop"),
    url(r'^edit_mobile/(?P<pk>\d+)$', views.edit_mobile, name="edit_mobile"),
    url(r'^delete_laptop/(?P<pk>\d+)$', views.delete_laptop, name="delete_laptop"),
    url(r'^delete_desktop/(?P<pk>\d+)$', views.delete_desktop, name="delete_desktop"),
    url(r'^delete_mobile/(?P<pk>\d+)$', views.delete_mobile, name="delete_mobile"),
]
