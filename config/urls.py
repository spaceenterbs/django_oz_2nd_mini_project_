"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/questions/", include("questions.urls")),
    path("api/results/", include("results.urls")),
]

# from django.contrib import admin
# from django.urls import path, include

# # from questions import views as questions_views
# # from results import views as results_views

# # from questions.views import say_hello
# # from results.views import say_hello

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path("rooms", views.say_hello),
#     # path("api/v1/questions/", include("questions.urls")),
#     # path("api/v1/results/", include("results.urls")),
#     # path("api/v2/questions/", include("feeds.urls")),
#     # path("api/v3/questions/", include("feeds.urls")),
#     # path("api/v2/results/", include("results.urls")),
#     # path("api/v3/results/", include("results.urls")),
# ]
