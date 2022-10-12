import random
from django.conf import settings
from django.shortcuts import render

from django.views import View

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.

class Send(View):
    # la primera funcion recibe una peticion get y renderiza nuestra vista de formulario para recibir la direccion de correo electronico
    def get(self, request):
        return render(request, 'send.html')


    def post(self, request):
        email = request.POST.get('email')
        print(email)

        template = get_template('respuesta.html')
        
        codigoderegistro = random.randint(0, 999999)
        # Se renderiza el template y se envias parametros
        content = template.render({'codigoderegistro': codigoderegistro})

        # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives(
            'Codido de registro',
            'Hola, te enviamos un correo codigo de registro',
            settings.EMAIL_HOST_USER,
            [email]
        )

        msg.attach_alternative(content, 'text/html')
        msg.send()

        return render(request, 'send.html')