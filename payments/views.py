from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from django.http import JsonResponse
from cafehome.models import Transaction, Computer
import json

# Create your views here.


class Payments(TemplateView):
    template_name = "html/payment/payments.html"

    def get_context_data(self, **kwargs):
        computer_id = self.kwargs.get("computer_id")
        computer = Computer.objects.get(id=computer_id)
        return {"computer": computer}


class OrderCompleteView(View):

    def post(self, request, *args, **kwargs):
        order_details = json.loads(request.body)
        print(order_details)
        order = order_details["order_details"]["purchase_units"][0]
        Transaction.objects.create(
            customer_name=order["shipping"]["name"]["full_name"],
            customer=request.user,
            computer=Computer.objects.get(id=self.kwargs.get("computer_id")),
            transaction_id=order_details["order_details"]["id"],
            transaction_date=order_details["order_details"]["create_time"],
            transaction_amount=order["amount"]["value"],
        )

        return JsonResponse({"success": True})
