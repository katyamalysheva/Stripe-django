import stripe
from django.conf import settings
from django.http import HttpResponse
from django.http.response import JsonResponse  # new
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from stripepay.models import Item
from stripepay.serializers import ItemSerializer


class CheckoutCreateView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):

        item = Item.objects.get(id=kwargs["id"])
        stripe.api_key = settings.STRIPE_SECRET_KEY

        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cancel",
            mode="payment",
            line_items=[{"price": item.price_stripe, "quantity": 1}],
        )
        return JsonResponse({"sessionId": session["id"]})


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(APIView):
    template_name = "index.html"
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = ItemSerializer

    def get(self, request, id):
        item = get_object_or_404(Item, pk=id)
        return Response({"item": item})


def success(request):
    return HttpResponse("<h1>Оплата прошла успешно!</h1>")


def cancel(request):
    return HttpResponse("<h1>Оплата не прошла :(</h1>")
