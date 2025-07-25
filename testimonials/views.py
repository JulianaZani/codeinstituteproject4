from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thank you for your message!")
            form = ContactForm()
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
