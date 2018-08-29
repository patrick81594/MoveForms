"""
Definition of urls for MoveForm.
"""


import MoveForm
import mvForms
from django.contrib import admin
admin.autodiscover()
from django.urls import include, path
from mvForms import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Examples:
    #path('mvforms/', include('mvForms.urls')),
    path('', include('mvForms.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),

    #path('', include('django.contrib.auth.urls'))
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

]