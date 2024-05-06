# -*- coding: utf-8 -*-
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from cafehome.models import Transaction, Computer
from cafee83 import constant
import json


class Payments(TemplateView):
    template_name = constant.PAYMENTS_HTML

    def get_context_data(self, **kwargs):
        computer_id = self.kwargs.get("computer_id")
        computer = Computer.objects.get(id=computer_id)
        return {"computer": computer}


class OrderCompleteView(View):

    def post(self, request, *args, **kwargs):
        order_details = json.loads(request.body)
        order = order_details["order_details"]["purchase_units"][0]
        Transaction.objects.create(
            payer_username=order["shipping"]["name"]["full_name"],
            customer=request.user,
            computer=Computer.objects.get(id=self.kwargs.get("computer_id")),
            transaction_id=order_details["order_details"]["id"],
            transaction_amount=order["amount"]["value"],
            transaction_status=order_details.get("order_details").get("status"),
        )

        return JsonResponse({"success": True})
