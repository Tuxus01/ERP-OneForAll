from turtle import width
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import date, datetime
from django.forms import model_to_dict



#Base Global para todas las tablas
### List Status for App #####
"""
    1.  Active
    2.  Process 
    3.  Cancel
    4.  Void
    5.  Reject
    6.  Inspect
    7.  Issued
    8.  Approved
    9.  Complete
    10. Incomplete
    11. Propose
    12. In Process
    13. 

    --- Estatus de PO
    Issued
    In Process
    Complete
    Propose
    Void

    -- Estados de Materiales/Componentes
    Active
    Reject
    Inspect
    Void

    -- Estado de Localidades 
    Active
    Void

    



    --- Estatus para detalles de PO
    
"""
### List Status for App #####
class StatusNames(models.Model):
    StatusNames = models.CharField(max_length=500,unique=True)
    is_material = models.BooleanField(default=False)
    is_container = models.BooleanField(default=False)
    is_purchaseorder = models.BooleanField(default=False)


    def __str__(self):
        return self.StatusNames


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    date_create = models.DateField('Date of Create',auto_now = False, auto_now_add = True)
    date_change = models.DateField('Date of Change',auto_now = True, auto_now_add = False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    date_time_c = models.TimeField(auto_now = False, auto_now_add = True)
    date_time_m = models.TimeField(auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True


## Modulos de empresas Filiales, configuracion , Monedas, Tax, etc.....
class Company(ModelBase):
    NameCompany = models.CharField(max_length=500,unique=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='CompanyStatus',blank=True,null=True)

    def __str__(self):
        return self.NameCompany


class Branch(ModelBase):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='BranchCompany')
    NameBranch = models.CharField(max_length=500,unique=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='BranchStatus',blank=True,null=True)
    
    def __str__(self):
        return self.NameBranch





class Profile(ModelBase):
    UserProfile =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,related_name='ProfileUser')
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='ProfileBranch')
    is_admin = models.BooleanField(default=False)
    expire =models.DateField(blank=True,null=True)


    def __str__(self):
        return self.UserProfile.first_name
 
##Se asignara un Branch al usuario y asi solo podra visualizar materailes, bodegas y de esa filial


class Warehouse(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='Branch')
    WarehouseName =models.CharField(max_length=500,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='WarehouseStatus',blank=True,null=True)

    def __str__(self):
        return self.WarehouseName
    




########################################################################################################################
## Modulos de Creacion de componentes
### Maquinaria, Objeto, Herramienta, ETC
class Category(ModelBase):
    Branch =models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='CategoryBranch')
    CategoryName = models.CharField(max_length=400,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='CategoryStatus',blank=True,null=True)

    def __str__(self):
        return self.CategoryName


class SubCategory(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='SubCategoryBranch')
    SubCategoryName = models.CharField(max_length=400,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='SubCategoryStatus',blank=True,null=True)

    def __str__(self):
        return self.SubCategoryName


### Como viene el producto, Unidad, Yard, Peso, Libra, Galon etc...
class Units(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='UnitsBranch')
    UnitName =  models.CharField(max_length=400,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='UnitsStatus',blank=True,null=True)

    def __str__(self):
        return self.UnitName

#### Color esta realacionada con el material
class Colors(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='ColorsBranch')
    ColorsName =  models.CharField(max_length=400,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='ColorsStatus',blank=True,null=True)

    def __str__(self):
        return self.ColorsName
    


class Component(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='ComponentBranch')
    ComponentName = models.CharField(max_length=400,unique=True)
    NominalCost = models.FloatField(blank=True, null=True)
    MinimunStock = models.FloatField(blank=True, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='ComponentCategory')
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name='ComponentSubCategory')
    Comment =  models.TextField(max_length=400,blank=True,null=True)
    MinimunOrdered = models.FloatField(default=1) ## Medida en Inch
    UsageUnit = models.ForeignKey(Units, on_delete=models.CASCADE ,related_name='ComponentUsageUnit')
    PurchasUnit = models.ForeignKey(Units, on_delete=models.CASCADE ,related_name='ComponentPurchasUnit')
    CoversionFactor = models.FloatField(default=1,blank=True, null=True)  ## Se compra en caja pero se utiliza en unidad
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='ComponentStatus',blank=True,null=True)
    tax = models.FloatField(default=0,blank=True, null=True)

    def __str__(self):
        return self.ComponentName


class Bins(ModelBase):
    Bin = models.CharField(max_length=400,unique=True)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='BinsBranch')
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name='BinsWarehouse')
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='BinsStatus',blank=True,null=True)

    def __str__(self):
        return self.Bin
    





class Materials(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='MaterialsBranch')
    #Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name='MaterialsWarehouse')
    PartNumber = models.CharField(max_length=400,unique=True)
    SerialNumber = models.CharField(max_length=400,blank=True,null=True) ## Codigo de barra
    Name = models.CharField(max_length=400,blank=True,null=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    PartColor = models.ForeignKey(Colors, on_delete=models.CASCADE,related_name='MaterialsColors',blank=True,null=True) # Color List
    OnHand = models.FloatField(blank=True, null=True)
    Ordered =models.FloatField(blank=True, null=True)
    Reject =models.FloatField(blank=True, null=True)
    Allocated =models.FloatField(blank=True, null=True)
    Inspected =models.FloatField(blank=True, null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='MaterialsStatus',blank=True,null=True)
    Component = models.ForeignKey(Component, on_delete=models.CASCADE,related_name='MaterialsComponent',blank=True,null=True)

    def __str__(self):
        return self.PartNumber
    

class Adrresses(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='AdrressesBranch')
    PrincipalName = models.CharField(max_length=400,blank=True,null=True )
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    Email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.PrincipalName

class PurchaseType(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='PurchaseTypeBranch')
    PurchaseTypeName =  models.CharField(max_length=400,unique=True)
    Description = models.TextField(max_length=400,blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='PurchaseTypeStatus',blank=True,null=True)

    def __str__(self):
        return self.PurchaseTypeName


def File(self, filename):
    today = date.today()
    year = format(today.year)
    mes = format(today.month)
    dia = format(today.day)
    path = "static/MultimediaData/PurchaseOrders_Files/%s/%s/%s/%s/%s" %(str(year), str(mes), str(dia), str(self.owner.username), str(filename))
    return path


class Currency(ModelBase):
    CurrencyName = models.CharField(max_length=300,unique=True)
    CurrencyAbre = models.CharField(max_length=300,unique=True)
    Description = models.TextField(max_length=700, blank=True,null=True)

    def __str__(self):
        return self.CurrencyAbre


def random_id():
    last_id = PurchaseOrders.objects.all().order_by('id').last()
    
    if last_id == None:
        new_last_int = 0 + 1
    else:
        last_int = int(last_id.id)
        new_last_int = last_int + 1
    return 'PO_'+ str(new_last_int).zfill(10) 

class PurchaseOrders(ModelBase):
    PO = models.CharField(max_length=400,unique=True, default=random_id)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='PurchaseOrdersBranch')
    Subject = models.CharField(max_length=400,blank=True, null=True)
    CC = models.CharField(max_length=600, blank=True,null=True)
    Vendor = models.ForeignKey(Adrresses, on_delete=models.CASCADE,related_name='PurchaseOrdersAdrresses')
    Tax = models.FloatField(default=0,blank=True, null=True) ## almacenara el total de todos los impuiestos por componente
    SubTotal =  models.FloatField(default=0,blank=True, null=True)
    Total = models.FloatField(default=0,blank=True, null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='PurchaseOrdersStatus',blank=True,null=True)
    ETA = models.DateField(blank=True, null=True)
    PurchaseType = models.ForeignKey(PurchaseType, on_delete=models.CASCADE,related_name='PurchaseOrdersPurchaseType',blank=True, null=True)
    Bill = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name='BillWarehouse',blank=True, null=True)
    Ship = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name='ShipWarehouse',blank=True, null=True)
    SubtotalShip = models.FloatField(default=0,blank=True, null=True)## por si se paga envio
    Quotes = models.FileField(upload_to=File,blank=True, null=True) ## File Cotizaciones, 
    PurchaseAgent = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,related_name='PurchaseOrdersProfile')
    Nota = models.TextField(max_length=1200, blank=True,null=True) # Comentarios
    TypeCurrency = models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='PurchaseOrdersCurrency', blank=True,null=True)
    Customer = models.ForeignKey(Adrresses, on_delete=models.CASCADE,related_name='PurchaseOrdersAdrressesCustomer',blank=True,null=True)

    


    def __str__(self):
        return self.PO

class PurchaseOrderDetail(ModelBase):
    PurchaseOrder = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE,related_name='PurchaseOrderDetailPurchaseOrder')
    PartNumber = models.CharField(max_length=400)
    Price = models.FloatField(blank=True, null=True)
    QuantityOrdered = models.FloatField(default=0)
    QuantityReceived = models.FloatField(blank=True, null=True)
    QuantityInspect = models.FloatField(blank=True, null=True)
    QuantityReject = models.FloatField(blank=True, null=True)
    Tax = models.FloatField(blank=True, null=True) ## Porcentaje de impuesto del producto
    SubTotal = models.FloatField(blank=True, null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='PurchaseOrderDetailStatus',blank=True,null=True)

    def __str__(self):
        return self.PartNumber





class Container(ModelBase):
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='ContainerBranch')
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name='ContainerWarehouse')
    PPRC = models.CharField(max_length=400,unique=True)
    PartNumber =  models.CharField(max_length=400,blank=True, null=True)
    DyeLot =  models.CharField(max_length=400,blank=True, null=True)
    Label =  models.CharField(max_length=400,blank=True, null=True)
    OnHand = models.FloatField(blank=True, null=True)
    Bin = models.ForeignKey(Bins, on_delete=models.CASCADE,related_name='ContainerBin')
    InvoiceNumber= models.CharField(max_length=400,blank=True, null=True)
    ReceiveDate = models.DateField()
    PurchaseOrder = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE,related_name='ContainerPurchaseOrder',blank=True,null=True)
    Status = models.ForeignKey(StatusNames, on_delete=models.CASCADE,related_name='ContainerStatus',blank=True,null=True)

    def __str__(self):
        return self.PPRC
    