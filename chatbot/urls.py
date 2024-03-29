from django.urls import path
from . import views
urlpatterns = [
    path('', views.chat),
    path('contact/', views.contact),
    # path('chat/', views.chat_message),  # Remove the leading slash
]
