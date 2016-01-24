from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Reap_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('reap.urls', namespace="reap")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reap/', include('reap.urls', namespace="reap")),
]
