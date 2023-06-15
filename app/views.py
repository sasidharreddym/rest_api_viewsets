from django.shortcuts import render
from rest_framework.viewsets import ViewSet
# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class Productcrudvs(ViewSet):
    def list(self,request):
        PDO=Product.objects.all()
        PSO=ProductSerializer(PDO,many=True)
        return Response(PSO.data)

    def create(self,request):
        PSD=ProductSerializer(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'success':'product has been created sucessfully'})
        else:
            return Response({'failure':'it is not created'})
        
    def retrieve(self,request,pk):
        def create(self,request):
            SD=ProductSerializer(data=request.data)
            if SD.is_valid():
                SD.save()
                return Response({'Success':'Product is Created'})
            else:
                return Response({'Failed':'Product is not created'})
    
    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO)
        return Response(SPD.data)
    
    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})
