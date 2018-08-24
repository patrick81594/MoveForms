"""
Definition of urls for MoveForm.
"""


import MoveForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.urls import include, path

urlpatterns = [
    # Examples:
    path('mvforms/', include('mvForms.urls')),
    path('admin/', admin.site.urls),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
