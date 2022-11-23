from rest_framework import viewsets, permissions, filters
from django.db.models import Prefetch
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from django.http import JsonResponse
import json


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    search_fields = ['=username']
    filter_backends = (filters.SearchFilter,)


class StatusNamesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = StatusNames.objects.all().order_by('-id')
    serializer_class = StatusNamesSerializer
    search_fields = ['=StatusNames']
    filter_backends = (filters.SearchFilter,)


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    search_fields = ['=NameCompany']
    filter_backends = (filters.SearchFilter,)

class BranchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Branch.objects.all().order_by('-id')
    serializer_class = BranchSerializer
    search_fields = ['=NameBranch']
    filter_backends = (filters.SearchFilter,)

    



class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Category.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Category.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = CategorySerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)



class WarehouseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Warehouse.objects.all().order_by('-id')
    serializer_class = WarehouseSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Warehouse.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Warehouse.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = WarehouseSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)


class SubCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = SubCategory.objects.all().order_by('-id')
    serializer_class = SubCategorySerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = SubCategory.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = SubCategory.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = SubCategorySerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class UnitsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Units.objects.all().order_by('-id')
    serializer_class = UnitsSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Units.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Units.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = UnitsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)


class ColorsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Colors.objects.all().order_by('-id')
    serializer_class = ColorsSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Colors.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Colors.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = ColorsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class ComponentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Component.objects.all().order_by('-id')
    serializer_class = ComponentSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Component.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Component.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = ComponentSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class BinsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Bins.objects.all().order_by('-id')
    serializer_class = BinsSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Bins.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Bins.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = BinsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class MaterialsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Materials.objects.all().order_by('-id')
    serializer_class = MaterialsSerializer
    search_fields = ['=id']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Materials.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Materials.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = MaterialsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class AdrressesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Adrresses.objects.all().order_by('-id')
    serializer_class = AdrressesSerializer
    search_fields = ['=PrincipalName']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Adrresses.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Adrresses.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = AdrressesSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

""" class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    search_fields = ['=CustomerName']
    filter_backends = (filters.SearchFilter,) """

class PurchaseTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = PurchaseType.objects.all().order_by('-id')
    serializer_class = PurchaseTypeSerializer
    search_fields = ['=PO']
    filter_backends = (filters.SearchFilter,)

class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Currency.objects.all().order_by('-id')
    serializer_class = CurrencySerializer
    search_fields = ['=PO']
    filter_backends = (filters.SearchFilter,)


class PurchaseOrdersyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = PurchaseOrders.objects.all().order_by('-id')
    serializer_class = PurchaseOrdersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =  ['PO','Status__StatusNames','PurchaseAgent__username']
    #search_fields = ['=PO','=Status__StatusNames']
    #filter_backends = (filters.SearchFilter,)

    def list(self, request):
        Status =  self.request.query_params.get('Status__StatusNames')
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = PurchaseOrders.objects.filter(Status__StatusNames=Status).order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = PurchaseOrders.objects.filter(Branch=i[0].Branch.id).filter(Status__StatusNames=Status).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = PurchaseOrdersSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)

class PurchaseOrderDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = PurchaseOrderDetail.objects.all().order_by('-id')
    serializer_class = PurchaseOrderDetailSerializer
    filterset_fields =  ['PurchaseOrder__Status__StatusNames']
    #search_fields = ['=PurchaseOrder__Status__StatusNames']
    #filter_backends = (filters.SearchFilter,)

class ContainerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Container.objects.all().order_by('-id')
    serializer_class = ContainerSerializer
    search_fields = ['=PartNumber']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        
        alert = False
        i = Profile.objects.filter(UserProfile=request.user)
        if i:
            if i[0].is_admin == True: 
                queryset = Container.objects.all().order_by('-id')
            else:
                if i[0].expire >= date.today():
                    #print(i.Branch.id)
                    queryset = Container.objects.filter(Branch=i[0].Branch.id).order_by('-id')
                else:
                    alert = True
                    queryset = {'Alert':'Your time has expired :' ,'Date': str(i[0].expire)}
        else:
            alert = True
            queryset = {'Alert':'Your profile not has permissions to run queries','Date':''} 

        if alert == False:
            serializer = ContainerSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse(queryset,safe=False)



