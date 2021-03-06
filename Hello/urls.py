"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf import settings
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),

    url(r'^reviews/$', views.archive),
    url(r'^reviews/<year>[0-9]{4}/$', views.archive),
    url(r'^reviews/<year>[0-9]{4}/<month>[0-9]{2}$', views.archive),
    url(r'^reviews/<year>[0-9]{4}/<month>[0-9]{2}/<day>[0-9]{2}$', views.review_detail),

]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
