from django import forms
from projectApp.models import StudentRegister  

class StudentRegisterForm(forms.ModelForm):  
    class Meta:  
        model = StudentRegister  
        fields = ['name', 'mobile', 'email'] 
        
        widgets = { 
            'name': forms.TextInput(), 
            'mobile': forms.TextInput(),
            'email': forms.EmailInput(),
        }
        
        # Set fields as optional explicitly
    name = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    email = forms.EmailField(required=False)

