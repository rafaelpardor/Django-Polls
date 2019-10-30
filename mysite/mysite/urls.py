from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # the path() function is passed four arguments.
    # Two req. route and view, and two optionals, name and kwargs
    # Route: is a string type, and contains the URL pattern
    # View: While the URLpattern is matching, an view function is called with an HTTPRequest
    # Kwargs: 
    #  Name: Naming the URL let us to refer in other parts of our django app. Leaving apart unambiguously.
    path('admin/', admin.site.urls),

    # The include() function allows referencing other URLconfs.
    # The idea of this func. is to make it easy ti plug-and-play URLs.
    # We should use include when we include other url patterns.
    path('polls/', include('polls.urls')),
]
