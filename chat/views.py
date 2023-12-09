from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

def chat(request):
    mensajes = Mensaje.objects.all()
    if request.method == 'POST':
        form = MensajeForm(request.POST)        
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.usuario = request.user
            nuevo_mensaje.save()
            return redirect('chat')
    else:
        form = MensajeForm()
    return render(
        request=request,
        template_name = "chat/chat.html",
        context={'mensajes': mensajes, 'form': form},
        )