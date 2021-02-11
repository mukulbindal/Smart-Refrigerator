from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detect$', views.detect_items, name="detect"),

]