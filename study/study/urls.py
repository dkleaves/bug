from django.conf.urls import include, url
from django.contrib import admin
from books import views
# from contact import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', views.test),
    url(r'^test2/', views.test2),
    # url(r'^search/$', views.search),
    # url(r'^contact/$', views.contact),
    # url(r'^contact/thanks/$', views.thanks),
]
