from django.forms import *
from .models import Computer


class AddComputer(ModelForm):

    class Meta:
        model = Computer

        fields = ["name", "processor", "ram", "gpu", "usage_price"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "required": "True"},
            ),
            "processor": Select(attrs={"class": "form-control", "required": "True"}),
            "ram": Select(attrs={"class": "form-control", "required": "True"}),
            "gpu": Select(attrs={"class": "form-control", "required": "True"}),
            "usage_price": NumberInput(
                attrs={"class": "form-control", "required": "True"}
            ),
        }
