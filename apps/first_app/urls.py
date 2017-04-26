from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [ url(r'^$', views.index),
url(r'^registration$', views.registrationLogic),
url(r'^login$', views.loginLogic),
url(r'^quotes$', views.quotesLogic),
url(r'^createQuote$', views.createQuoteLogic),
url(r'^userData/(?P<id>\d+)$', views.userDataLogic),
url(r'^add/(?P<id>\d+)$', views.addLogic),
url(r'^delete/(?P<id>\d+)$', views.deleteLogic)]
