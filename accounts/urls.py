from django.conf.urls import url
from .views import logout,profile,login,register
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns=[
    url(r'^logout$',logout,name='logout'),
    url(r'^profile$', profile,name='profile'),
    url(r'^login$',login,name='login'),
    url(r'^register$', register, name='register'),
   # .............password reset urls ..................
     url(r'^password/reset/$',password_reset,name='password_reset'),
     url(r'^password/reset/done/$',password_reset_done, name='password_reset_done'),
     url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm, name='password_reset_confirm'),
     url(r'^password/reset/complete/$', password_reset_complete, name='password_reset_complete')
]
