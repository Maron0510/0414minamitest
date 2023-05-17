
from django import forms
from django.forms import widgets
from .models import Item


class ItemForm(forms.ModelForm):
    
    created_at = forms.DateField(
        widget=widgets.DateInput(
            attrs={'type': 'date'},
        ),
        label='製造日'
    )

    class Meta:
        model = Item
        fields = ('kanri','name','naka','hure','idou','kotei','tori','metuke','seikei','zumen','memo','created_at')#'age','sex',
        widgets = {
                    'kanri': forms.Select(attrs={'placeholder':'記入例：本社'}),
                    'name': forms.TextInput(attrs={'placeholder':'記入例：A55'}),
                    'naka': forms.TextInput(attrs={'placeholder':'記入例：A888'}),
                    #'hure': forms.TextInput(attrs={'placeholder':'記入例：A'}),
                    'hure': forms.TextInput(attrs={'onkeyup':'this.value = this.value.toUpperCase();'}),
                    'idou': forms.TextInput(),
                    'kotei': forms.TextInput(),
                    'tori': forms.TextInput(),
                    'metuke': forms.TextInput(),
                    #'age': forms.NumberInput(attrs={'min':1}),
                    #'sex': forms.RadioSelect(),
                    'hoka': forms.CheckboxInput(),
                    'seikei': forms.TextInput(attrs={'placeholder':'記入例：CD-8'}),
                    'zumen': forms.CheckboxInput(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
