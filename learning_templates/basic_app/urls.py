from django.urls import path, include
from . import views

# TEMPLAE TAGS
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('others/', views.others, name="others")
]
