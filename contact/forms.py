from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Juan Alvarez'}
    ), min_length=10, max_length=30)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'ejemplo@ejemplo.com'}
    ), min_length=10, max_length=50)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':5, 'placeholder':'Por favor escribe aquí tu mensaje'}
    ), min_length=20, max_length=500)