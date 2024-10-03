# myapp/forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'quantity']  # ไม่รวม ID, created_at, updated_at
