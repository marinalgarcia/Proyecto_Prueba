from django import forms
from ejemplo.models import Persona, Proveedores, Inventario

class PersonaForm(forms.ModelForm):

    #fecha_nacimiento = forms.DateField(label="fecha de nacimiento", input_formats=["%d/%m/%Y"],
    #widget=forms.TextInput(attrs={'placeholder':'30/12/1995'}))

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento']
        
class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)
      

class Buscar_Apellido(forms.Form):
      apellido = forms.CharField(max_length=100)


class BuscarProd(forms.Form):
      Producto = forms.CharField(max_length=200)

class InventarioForm(forms.ModelForm):
  class Meta:
    model = Inventario
    fields = ['Producto','Cantidad']

class ProveedoresForm(forms.ModelForm):
  class Meta:
    model = Proveedores
    fields = ['empresa', 'direccion', 'fecha_de_alta']