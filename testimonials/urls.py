from django.urls import path
from . import views


urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path(
        'testimonial/<int:pk>/',
        views.testimonial_detail,
        name='testimonial_detail',
    ),
    path('testimonial/add/', views.add_testimonial, name='add_testimonial'),
    path(
        'testimonial/<int:pk>/edit/',
        views.edit_testimonial,
        name='edit_testimonial',
    ),
    path(
        'testimonial/<int:pk>/delete/',
        views.delete_testimonial,
        name='delete_testimonial',
    ),
    path('contact/', views.contact_view, name='contact'),
]
