from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms


# Contact form definition
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')


def testimonial_list(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})


def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, approved=True)
    return render(request, 'testimonials/testimonial_detail.html', {'testimonial': testimonial})


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Your testimonial was submitted and is awaiting approval.')
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/add_testimonial.html', {'form': form})


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})
