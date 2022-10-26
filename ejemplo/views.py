from django.shortcuts import get_object_or_404, render
from django.views import View
from ejemplo.forms import Buscar_Apellido, PersonaForm
from ejemplo.models import Persona
from ejemplo.forms import PersonaForm, Buscar, Buscar_Apellido



# Create your views here.
class ListarPersonas(View):
    template_name = "ejemplo/lista_de_personas.html"

    def get(self,request):
        personas = Persona.objects.all()
        return render (request, self.template_name, {"personas": personas})

class CargarPersonas(View):
    template_name = "ejemplo/carga_de_personas.html"
    form_class = PersonaForm
    initial = {"nombre":"", "apellido":"", "fecha_de_nacimiento":""}

    def get(self,request):
        form = self.form_class(initial=self.initial)
        return render (request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name,{"form":form})

        return render(request, self.template_name,{"form":form})

class ActualizarPersonas(View):
    template_name = "ejemplo/actualizar_persona.html"
    success_template = "ejemplo/exito.html"
    form_class = PersonaForm
    initial = {"nombre":"", "apellido":"", "fecha_de_nacimiento":""}

    def get(self,request,pk):
        persona= get_object_or_404(Persona, pk=pk)
        form = self.form_class(instance=persona)
        return render (request, self.template_name, {"form": form,"pk":pk})

    def post(self, request,pk):
        persona= get_object_or_404(Persona, pk=pk)
        form = self.form_class(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
    
        return render(request, self.success_template)
    
class BuscarCliente(View):

    form_class = Buscar
    template_name = 'ejemplo/Buscar.html'
    initial = {"nombre":""}

    def get(self, request):              
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):               
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_Clientes = Persona.objects.filter(nombre__contains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_Clientes':lista_Clientes})
        return render(request, self.template_name, {"form": form})
    
class BuscarClienteApellido(View):

    form_class = Buscar_Apellido
    template_name = 'ejemplo/Buscar_Apellido.html'
    initial = {"apellido":""}

    def get(self, request):              
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):               
        form = self.form_class(request.POST)
        if form.is_valid():
            apellido = form.cleaned_data.get("apellido")
            lista_Clientes = Persona.objects.filter(apellido__contains=apellido).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_Clientes':lista_Clientes})
        return render(request, self.template_name, {"form": form})