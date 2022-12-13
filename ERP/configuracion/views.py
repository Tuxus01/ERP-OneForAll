from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import dataclasses
from urllib import request

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth import login, logout
import threading
from django.core.files import File
from django.db.models import Prefetch



#################################### Model Base for action in all querys ##########################
@method_decorator(csrf_exempt)
def Example(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        action = body['action']
        if action == 'Edit':
            pass
        if action == 'Create':
            pass
        if action == 'Update':
            pass 
        if action == 'Delete':
            pass

        return JsonResponse(editedItem,safe=False)
#################################### Model Base for action in all querys ##########################


from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import redirect
#@login_required(login_url='/login/')

class index(View):
    def get(self,request, *args, **kwargs):
        print(request)
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            response = redirect('/admin')
            return response
        



# Create your views here.
""" @login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html') """

@method_decorator(csrf_exempt)
def ComponentGet(request,*args, **kwargs):
    i = Component.objects.values()
    return JsonResponse(list(i),safe=False)


##Function create by validate permision and level access in the project!!
def ValidarPorfile(request):
    i = Profile.objects.filter(UserProfile=request.user)
    return i[0]

##Acciones de Guardar/Editar/Modificar/Eliminar
@method_decorator(csrf_exempt)
def CategoryAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            #ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            a = Category()
            a.CategoryName = editedItem['CategoryName']
            a.Description = editedItem['Description'] 
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            #ST = StatusNames.objects.get(pk=editedItem['Status']['id'])
            
            e = Category.objects.get(pk=ids)

            e.Description = editedItem['Description'] 
            e.CategoryName = editedItem['CategoryName']
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Category.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Category.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)
    

@method_decorator(csrf_exempt)
def BinAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        #print(editedItem)
        
        if action == 'Create':
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            WH =  Warehouse.objects.filter(WarehouseName=editedItem['Warehouse'])[:1]
            a = Bins()
            a.Bin = editedItem['Bin']
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Warehouse = WH[0]
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            #print("editando bin")
            #print(editedItem['Warehouse']['WarehouseName'])
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            WH =  Warehouse.objects.filter(WarehouseName=editedItem['Warehouse']['WarehouseName'])[:1]
            #ST = StatusNames.objects.get(pk=editedItem['Status']['id'])
            e = Bins.objects.get(pk=ids)
            e.Bin = editedItem['Bin'] 
            e.Warehouse = WH[0]
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Bins.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Bins.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)


@method_decorator(csrf_exempt)
def SubCategoryAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            #ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            a = SubCategory()
            a.SubCategoryName = editedItem['SubCategoryName']
            a.Description = editedItem['Description'] 
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            #ST = StatusNames.objects.get(pk=editedItem['Status']['id'])
            
            e = SubCategory.objects.get(pk=ids)

            e.Description = editedItem['Description'] 
            e.SubCategoryName = editedItem['SubCategoryName']
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = SubCategory.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = SubCategory.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)


@method_decorator(csrf_exempt)
def ColorsAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            #ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            a = Colors()
            a.ColorsName = editedItem['ColorsName']
            a.Description = editedItem['Description'] 
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            #ST = StatusNames.objects.get(pk=editedItem['Status']['id'])
            
            e = Colors.objects.get(pk=ids)

            e.Description = editedItem['Description'] 
            e.ColorsName = editedItem['ColorsName']
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Colors.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Colors.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)


@method_decorator(csrf_exempt)
def ComponentAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            #print(editedItem)
            #ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            C = Category.objects.filter(CategoryName=editedItem['Category'])[:1]
            SC = SubCategory.objects.filter(SubCategoryName=editedItem['SubCategory'])[:1]
            UP = Units.objects.filter(UnitName=editedItem['PurchasUnit'])[:1]
            UU = Units.objects.filter(UnitName=editedItem['UsageUnit'])[:1]
            a = Component()
            a.ComponentName = editedItem['ComponentName']
            a.NominalCost = editedItem['NominalCost']
            a.MinimunStock = editedItem['MinimunStock'] 
            a.Comment = editedItem['Comment'] 
            a.MinimunOrdered = editedItem['MinimunOrdered'] 
            a.CoversionFactor = editedItem['CoversionFactor']  
            a.tax = editedItem['tax']  
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.Category = C[0] 
            a.SubCategory = SC[0]
            a.UsageUnit = UU[0]
            a.PurchasUnit = UP[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            
            
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            C = Category.objects.filter(CategoryName=editedItem['Category']['CategoryName'])[:1]
            SC = SubCategory.objects.filter(SubCategoryName=editedItem['SubCategory']['SubCategoryName'])[:1]
            UP = Units.objects.filter(UnitName=editedItem['PurchasUnit']['UnitName'])[:1]
            UU = Units.objects.filter(UnitName=editedItem['UsageUnit']['UnitName'])[:1]
            
            a = Component.objects.get(pk=ids)
            a.ComponentName = editedItem['ComponentName']
            a.NominalCost = editedItem['NominalCost']
            a.MinimunStock = editedItem['MinimunStock'] 
            a.Comment = editedItem['Comment'] 
            a.MinimunOrdered = editedItem['MinimunOrdered'] 
            a.CoversionFactor = editedItem['CoversionFactor']  
            a.tax = editedItem['tax']  
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.Category = C[0] 
            a.SubCategory = SC[0]
            a.UsageUnit = UU[0]
            a.PurchasUnit = UP[0]
            #a.owner=request.user
            a.save()
            Action_Status = False 
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Component.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Component.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)


@method_decorator(csrf_exempt)
def UnitsAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            #ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            a = Units()
            a.UnitName = editedItem['UnitName']
            a.Description = editedItem['Description'] 
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            #ST = StatusNames.objects.get(pk=editedItem['Status']['id'])
            
            e = Units.objects.get(pk=ids)

            e.Description = editedItem['Description'] 
            e.UnitName = editedItem['UnitName']
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Units.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Units.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)



@method_decorator(csrf_exempt)
def WarehouseAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            
            ST =  StatusNames.objects.filter(StatusNames='Active')[:1]
            
            a = Warehouse()
            a.WarehouseName = editedItem['WarehouseName']
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            
            a.Status = ST[0]
            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
           
            e = Warehouse.objects.get(pk=ids)
            e.WarehouseName = editedItem['WarehouseName'] 
     
            e.Status = ST[0]
            e.save()
            Action_Status = False
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Warehouse.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Warehouse.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)



@method_decorator(csrf_exempt)
def MaterialAxios(request,*args, **kwargs):
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        ##print(profile.Branch.id)
        action = body['action']
        Action_Status = False
        
        if action == 'Create':
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status'])[:1]
            PC = Colors.objects.filter(ColorsName=editedItem['PartColor'])[:1]
            COMP = Component.objects.filter(ComponentName=editedItem['Component'])[:1]
            a = Materials()
            a.PartNumber = editedItem['PartNumber']
            a.SerialNumber = editedItem['SerialNumber']
            a.Name = editedItem['Name'] 
            a.Description = editedItem['Description'] 
            a.OnHand = editedItem['OnHand'] 
            a.Ordered = editedItem['Ordered']  
            a.Reject = editedItem['Reject']  
            a.Allocated = editedItem['Allocated']  
            a.Inspected = editedItem['Inspected']  


            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.PartColor = PC[0] 
            a.Component = COMP[0]

            a.owner=request.user
            a.save()
            Action_Status = True
            
        if action == 'Edit':
            ids = editedItem['id']
            
            
            ST =  StatusNames.objects.filter(StatusNames=editedItem['Status']['StatusNames'])[:1]
            PC = Colors.objects.filter(ColorsName=editedItem['PartColor']['ColorsName'])[:1]
            COMP = Component.objects.filter(ComponentName=editedItem['Component']['ComponentName'])[:1]
            
            a = Materials.objects.get(pk=ids)
            a.PartNumber = editedItem['PartNumber']
            a.SerialNumber = editedItem['SerialNumber']
            a.Name = editedItem['Name'] 
            a.Description = editedItem['Description'] 
            a.OnHand = editedItem['OnHand'] 
            a.Ordered = editedItem['Ordered']  
            a.Reject = editedItem['Reject']  
            a.Allocated = editedItem['Allocated']  
            a.Inspected = editedItem['Inspected']  


            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            a.Status = ST[0]
            a.PartColor = PC[0] 
            a.Component = COMP[0]

            #a.owner=request.user
            a.save()
            Action_Status = False 
        
        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = Materials.objects.get(pk=ids)
                de.delete()
            Action_Status = False

        if Action_Status == True:
            i = Materials.objects.all().last()
            return JsonResponse({'Status':'Ok','id':i.id},safe=False)
        else:
            return JsonResponse({'Status':'Not-Ok'},safe=False)

from django.utils.encoding import *
@method_decorator(csrf_exempt)
def SavePOManualAxios(request,*args, **kwargs):
    
    if request.method == 'POST':
        profile = ValidarPorfile(request)
        

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        editedItem = body['editedItem']
        action = body['action']
        

        
        Action_Status = False
        print(editedItem)
        if action == 'Create':
            detail = body['detail']
            Vendor = Adrresses.objects.filter(PrincipalName=editedItem['Vendor'])[:1]
            Customer = Adrresses.objects.filter(PrincipalName=editedItem['Customer'])[:1]
            Status = StatusNames.objects.filter(StatusNames='Propose')[:1]
            Bill = Warehouse.objects.filter(WarehouseName=editedItem['Bill'])[:1]
            Ship = Warehouse.objects.filter(WarehouseName=editedItem['ShipTo'])[:1]
            PurchaseAgent = User.objects.filter(username=editedItem['PurchaseAgent'])[:1]
            TypeCurrency = Currency.objects.filter(CurrencyAbre=editedItem['TypeCurrency'])[:1]
            PurchaseTypex = PurchaseType.objects.filter(PurchaseTypeName=editedItem['PurchaseType'])[:1]

            a = PurchaseOrders()
            a.Branch = Branch.objects.get(pk=profile.Branch.id)
            #a.Subject = editedItem['']
            #a.CC = editedItem['']
            a.Tax = editedItem['Tax_']
            a.SubTotal = editedItem['SubTotal_']
            a.Total = editedItem['Total_']
            #a.ETA = editedItem['']
            #a.SubtotalShip = editedItem['']
            #a.Quotes = editedItem['files']
            a.Nota = editedItem['Nota']



            a.Vendor = Vendor[0]
            a.Customer = Customer[0]
            a.Status = Status[0]
            a.PurchaseType = PurchaseTypex[0]
            a.Bill = Bill[0]
            a.Ship = Ship[0]
            a.PurchaseAgent = PurchaseAgent[0]
            a.TypeCurrency = TypeCurrency[0]
            a.owner = request.user
            a.save()
            
            Action_Status = True
            print(a)
            
            for x in detail:
                d = PurchaseOrderDetail()
                d.PurchaseOrder = a
                d.PartNumber = x['PartNumber']
                d.Price = x['Price']
                d.QuantityOrdered = x['Qty']
                d.QuantityReceived = 0
                d.QuantityInspect = 0
                d.QuantityReject = 0
                d.Tax = x['Tax']
                d.SubTotal = x['SubTotal']
                d.Status =  Status[0]

                d.save()

        if action == 'Delete':
            ids = editedItem['id']
            if ids > 0:
                de = PurchaseOrders.objects.get(pk=ids)
                de.delete()
            Action_Status = False
    if Action_Status == True:
        return JsonResponse({'id':a.id,'PO':a.PO},safe=False)
    if Action_Status == False:
        return JsonResponse({'id':0,'PO':'Error'},safe=False)