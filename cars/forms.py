from django import forms
from cars.models import Car

class NewCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 20000:
            self.add_error('value', 'O valor mínimo do carro deve ser 20000')
        else:
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação não pode ser menor do que 1975')
        else:
            return factory_year