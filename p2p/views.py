# views.py

from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Answer, Offer
from .serializers import AnswerSerializer, Offererializer


class OfferListCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        # If the data is a list of items, add them to the database
        if isinstance(data, list):
            items = []
            for item_data in data:
                serializer = Offererializer(data=item_data)
                if serializer.is_valid():
                    items.append(serializer.save())
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(Offererializer(items, many=True).data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid data format. Expected a list of items.'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerListCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # If the data is a list of items, add them to the database
        serializer = AnswerSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GetAnswers(APIView):


    def get(self, request, *args, **kwargs):
        items = Answer.objects.all()
        serializer = AnswerSerializer(items, many=True)
        data = serializer.data
        if items:
            items.delete()

        host_uuid=kwargs['host_uuid']
        
        now = timezone.now()
    
        Offer.objects.filter(active_date__lte=now - timezone.timedelta(seconds=15)).delete()

        Offer.objects.filter(host_uuid=host_uuid).update(active_date=timezone.now())

        return Response(data)


class GetOffer(APIView):
    def get(self, request, *args, **kwargs):
        now = timezone.now()
    
        Offer.objects.filter(active_date__lte=now - timezone.timedelta(seconds=15)).delete()
        first_offer = Offer.objects.first()
        serializer = Offererializer(first_offer)
        data=serializer.data
        if first_offer:
            first_offer.delete()
        return Response(data)