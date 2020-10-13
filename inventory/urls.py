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
]
