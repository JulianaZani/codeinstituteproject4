from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from Testimonials App!")
# This is a temporary view to avoid errors in the testimonials app.