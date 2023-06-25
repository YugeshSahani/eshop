from django import forms
from shop_app.models import Item
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ("seller", "views_count", "listed_at")

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the title of item ...",
                    "required": True,
                }
            ),
            
            'detail': SummernoteWidget(),
            "status": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-control"}),
            "target_customer": forms.Select(attrs={"class": "form-control"}),
            # "target_customer": forms.SelectMultiple(attrs={"class": "form-control"}),
        }