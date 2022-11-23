from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name','last_name']

class StatusNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusNames
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    Status=StatusNamesSerializer()
    class Meta:
        model = Company
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    Status=StatusNamesSerializer()
    Company = CompanySerializer()
    class Meta:
        model = Branch
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Category
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Warehouse
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = SubCategory
        fields = '__all__'


class UnitsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Units
        fields = '__all__'



class ColorsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Colors
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    UsageUnit  =UnitsSerializer()
    PurchasUnit=UnitsSerializer()
    Status=StatusNamesSerializer()
    SubCategory=SubCategorySerializer()
    Category=CategorySerializer()
    class Meta:
        model = Component
        fields = '__all__'


class BinsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Warehouse = WarehouseSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Bins
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    PartColor=ColorsSerializer()
    Component = ComponentSerializer()
    class Meta:
        model = Materials
        fields = '__all__'


class AdrressesSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    
    class Meta:
        model = Adrresses
        fields = '__all__'


""" class CustomerSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Customer
        fields = '__all__' """

class PurchaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseType
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class PurchaseOrdersSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    Vendor=AdrressesSerializer()
    PurchaseType=PurchaseTypeSerializer()
    TypeCurrency = CurrencySerializer()
    PurchaseAgent=UserSerializer()
    
    class Meta:
        model = PurchaseOrders
        fields = '__all__'


class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    #Branch = BranchSerializer()
    Status=StatusNamesSerializer()
    PurchaseOrder = PurchaseOrdersSerializer()
    class Meta:
        model = PurchaseOrderDetail
        fields = '__all__'


class ContainerSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    Branch = BranchSerializer()
    Warehouse= WarehouseSerializer()
    Status=StatusNamesSerializer()
    class Meta:
        model = Container
        fields = '__all__'