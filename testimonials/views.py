from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})

    return render(request, 'contact.html', {'form': form})
