from zeep import Client
from django.shortcuts import render
from django.forms import Form,ChoiceField

class ModulosForm(Form):
    tema = ChoiceField(label='Tema', choices=[])

def index(request):
    cliente = Client('http://localhost:8080/disciplinasws?wsdl')
    temas = cliente.service.getTemas()
    context = {
        'temas': temas
    }
    return render(request, 'index.html', context=context)

def modulos(request):
    cliente = Client('http://localhost:8080/disciplinasws?wsdl')
    if request.method == 'POST':
        tema = request.POST['tema']
        modulos = cliente.service.getModulosTema(tema)
        context = {'modulos': modulos, 'tema': tema}
        return render(request, 'modulos_lista.html', context)
    else:
        form = ModulosForm()
        form.fields['tema'].choices = [tuple([x,x]) 
                            for x in cliente.service.getTemas()]
        return render(request, 'modulos_form.html', {'form': form})