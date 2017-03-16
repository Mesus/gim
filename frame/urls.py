"""frame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,handler404,handler500
from django.contrib import admin
from gim import views
from gim.datastore import bs


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^async/', views.async),
    url(r'^ghpd', views.ghpd, name='ghpd'),
    url(r'^menu', views.menu, name='menu'),
    url(r'^cgje', views.cgje, name='cgje'),
    url(r'^dppd', views.dppd, name='dppd'),
    url(r'^dpje', views.dpje, name='dpje'),
    url(r'^jeqs', views.jeqs, name='jeqs'),
    url(r'^wqbg', views.wqbg, name='wqbg'),
    url(r'^map', views.map, name='map'),
    url(r'^login', views.login, name='login'),
    url(r'^charts', views.charts, name='charts'),
    url(r'^sub', views.sub_charts, name='sub_charts'),
    url(r'^nav', views.nav, name='nav'),
    url(r'^cd', views.createData, name='cd'),
    url(r'^cr', views.charts_right, name='cr'),
    url(r'^scr', views.scr, name='scr'),
    url(r'^llf', views.wlframe, name='lmf'),
    url(r'^lm', views.bmap_worklog, name='lm'),
    url(r'^rwl', views.right_worklog, name='rwl'),
    url(r'^ap4s', views.ajax_p4s, name='ap4s'),
    url(r'^r2', views.right_report, name='r2'),
    url(r'^ap4y', views.ajax_p4y, name='ap4y'),
    url(r'^bmcr', views.bmap_commreport, name='bmcr'),
    url(r'^snn', bs.snn, name='snn'),
    url(r'^ysxg', views.ysxg, name='ysxg'),
    url(r'^ayb', views.ajax_ysxg_bottom, name='ayb'),
]

