from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('testimonial_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
