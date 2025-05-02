from django import forms
from .models import Booking, Table

class BookTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'table', 'table_for']

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(isAvailable=True)

