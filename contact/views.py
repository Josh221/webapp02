from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Envio de email y redirección
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribio:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["jack.sepiol11@protonmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha salido bien, redirecciona a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo salio mal, redirecciona a fail
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'form':contact_form})