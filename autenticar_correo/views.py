import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.

# Esta funcion genera el codigo aleatorio        

def codigo():
    codigoderegistro = random.randint(0, 999999)
    return codigoderegistro
# Guardar el codigo en la variable codigo de registro
codigoderegistro = codigo()


#Esta clase se encarga de recibir la direccion de correo por formulario y retornar un correo electronico con un codigo de registro

class send(View):  

    # la primera funcion recibe una peticion get y renderiza nuestra vista de formulario para recibir la direccion de correo electronico
    def get(self, request):
        return render(request, 'send.html')  

    # La segunda funcion recibe el codigo que ingreso el usuario
    def post(self, request):
        #obtener el dato introducido por el usuario (email )
        email = request.POST.get('email')
        print(type(email))  


        #Creamos un template y a travez del metodo get_template y le indicamos que html hay que convertir en un objeto de la clase template
        template = get_template('respuesta.html')

        # Se renderiza el template y se envias parametros, en este caso el codigo generado anteriormente
        content = template.render({'codigoderegistro': codigoderegistro})
        

        # Se crea una variable(mshg) que va a ser un objeto de la clase EmailMultialternatives que nos permite tener parametros como el codigo, el msj, el correo del emisor y por ultimo el destinatario
        msg = EmailMultiAlternatives(
            'Codido de registro',
            'Hola, te enviamos un correo codigo de registro',
            settings.EMAIL_HOST_USER,
            [email]
        )
        #finalmente con el metodo attach_alternative adjuntamos el contenido que en este caso es el html que deseamos enviar, con los parametros. Lo adjuntamos y definimos de que tipo sera el contenido. 
        msg.attach_alternative(content, 'text/html')
        #enviando nuestro correo
        msg.send()      
        
        

       #Se redirige a una nueva pagina
        return redirect('verificacion')

        



# Esta clase se encarga de recibir el codigo que ingresa el usuario por formulario y cotejar si es el mismo que se envio por correo electronico
class verificacion(View):
    # la primera funcion recibe una peticion get y renderiza nuestra vista de formulario que solicita el codigo de seguridad al usuario.
    def get(self,request):
        return render(request, 'verificacodigo.html')
    # Esta funcion compara el codigo que envio el usuario con el que se le envio por correo
    def post(self,request):
        codigo = request.POST.get('verifica')
        codigoint = int(codigo)
        print(type(codigoint))
        if codigoint == codigoderegistro:
            print('es igual')
            return render(request, 'home.html') 
        else:
            ('no es igual')

        return render(request, 'verificacodigo.html',{
            'error':'no es el codigo correcto'
        }) 