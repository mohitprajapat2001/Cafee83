# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, NumberInput, Select
from .models import Computer


class ComputerForm(ModelForm):

    class Meta:
        model = Computer

        fields = ["name", "processor", "ram", "gpu", "usage_price"]
        widgets = {}
        for field in fields:
            if field == "name":
                input_class = TextInput
            elif field == "usage_price":
                input_class = NumberInput
            else:
                input_class = Select
            widgets[field] = input_class(
                attrs={"class": "form-control", "required": "True"}
            )
