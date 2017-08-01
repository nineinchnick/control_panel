from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^announcements/', include('announcements.urls', namespace='announcements')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'', include('panel.urls', namespace='panel')),

]
