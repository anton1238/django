from django.urls import path

from calculator.views import omlet, pasta, buter

urlpatterns = [
    path('omlet/', omlet, name='omlet'),
    path('pasta/', pasta, name='pasta'),
    path('buter/', buter, name='buter'),
]