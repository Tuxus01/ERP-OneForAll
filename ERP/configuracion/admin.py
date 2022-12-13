from django.contrib import admin
from .models import *
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','NameCompany','Status')
    list_filter = ('NameCompany', 'Status')
    search_fields = ['id','NameCompany']
admin.site.register(Company,CompanyAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','Company','NameBranch','Status')
    list_filter = ('NameBranch','Company', 'Status')
    search_fields = ['id','NameBranch','Company']
admin.site.register(Branch,BranchAdmin)


class StatusNamesAdmin(admin.ModelAdmin):
    list_display = ('id','StatusNames')
    
    search_fields = ['id','StatusNames']
admin.site.register(StatusNames,StatusNamesAdmin)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','WarehouseName','Status')
    list_filter = ('Branch','WarehouseName', 'Status')
    search_fields = ['id','Branch','WarehouseName']
admin.site.register(Warehouse,WarehouseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','CategoryName','Status')
    list_filter = ('Branch','CategoryName', 'Status')
    search_fields = ['id','Branch','CategoryName']
admin.site.register(Category,CategoryAdmin)


class SubCategoryNameAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','SubCategoryName','Status')
    list_filter = ('Branch','SubCategoryName', 'Status')
    search_fields = ['id','Branch','SubCategoryName']
admin.site.register(SubCategory,SubCategoryNameAdmin)


class UnitNameNameAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','UnitName','Status')
    list_filter = ('Branch','UnitName', 'Status')
    search_fields = ['id','Branch','UnitName']
admin.site.register(Units,UnitNameNameAdmin)


class ComponentNameAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','ComponentName','NominalCost','MinimunStock','Category','SubCategory','UsageUnit','PurchasUnit','CoversionFactor','Status')
    list_filter = ('Branch','ComponentName', 'Status')
    search_fields = ['id','Category','SubCategory']
admin.site.register(Component,ComponentNameAdmin)


class BinsAdmin(admin.ModelAdmin):
    list_display = ('id','Bin','Branch','Warehouse','Status')
    list_filter = ('Branch','Bin', 'Warehouse','Status')
    search_fields = ['id','Bin','Warehouse']
admin.site.register(Bins,BinsAdmin)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','PartNumber','SerialNumber','PartColor','OnHand','Ordered','Reject','Allocated','Inspected','Status')
    list_filter = ('Branch','PartNumber', 'Status')
    search_fields = ['id','PartNumber','SerialNumber','PartColor']
admin.site.register(Materials,MaterialsAdmin)

""" class AdrressesAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','PrincipalName','Status')
    ##list_filter = ('Branch','VendorName','Status')
    search_fields = ['id','PrincipalName'] """
admin.site.register(Adrresses)

""" class VendorsAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','VendorName','Status')
    ##list_filter = ('Branch','VendorName','Status')
    search_fields = ['id','VendorName']
admin.site.register(Vendors,VendorsAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','CustomerName','Status')
    ##list_filter = ('Branch','VendorName','Status')
    search_fields = ['id','CustomerName']
admin.site.register(Customer,CustomerAdmin) """

class PurchaseOrdersAdmin(admin.ModelAdmin):
    list_display = ('id','PO','Branch','Vendor','Tax','SubTotal','Total','Status')
    list_filter = ('Branch', 'Vendor','Status')
    search_fields = ['PO','Branch','Vendor','Tax','SubTotal','Total','Status']
admin.site.register(PurchaseOrders,PurchaseOrdersAdmin)



class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','Warehouse','Bin','PurchaseOrder','PPRC','PartNumber','DyeLot','Label','OnHand','InvoiceNumber','ReceiveDate','Status')
    list_filter = ('Bin','Warehouse')
    search_fields = ['Bin','PurchaseOrder','PPRC','PartNumber','DyeLot','Label','OnHand','InvoiceNumber','ReceiveDate']
admin.site.register(Container,ContainerAdmin)



class ColorsNameAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','ColorsName','Status')
    list_filter = ('Branch','ColorsName', 'Status')
    search_fields = ['id','Branch','ColorsName']
admin.site.register(Colors,ColorsNameAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','Branch','UserProfile')
    list_filter = ('Branch','UserProfile')
    search_fields = ['id','Branch','UserProfile']
admin.site.register(Profile,ProfileAdmin)


admin.site.register(Currency)
admin.site.register(PurchaseType)


class PurchaseOrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id','PurchaseOrder','PartNumber','Price','QuantityOrdered','QuantityReceived','QuantityInspect','QuantityReject','Tax','SubTotal','Status')
    #list_filter = ('Branch','UserProfile')
    search_fields = ['id','PurchaseOrder__PO']
admin.site.register(PurchaseOrderDetail,PurchaseOrderDetailAdmin)
