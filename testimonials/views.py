from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonial
from .forms import TestimonialForm

def testimonial_list(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, approved=True)
    return render(request, 'testimonials/testimonial_detail.html', {'testimonial': testimonial})
