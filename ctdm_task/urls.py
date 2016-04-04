from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ctdm_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ctdm.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
