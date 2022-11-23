<template>
  <div class="py-1 px-1">
    

    <v-container >
      <v-card dark small dense class="elevation-5 ">
        
        <v-container>
        <v-row class="py-1 px-1">

          <!--Encabezado-->
          <v-col cols="12" sm="12" md="12">
            <v-row>
              <v-col cols="12" sm="12" md="3">
                <v-select
                    outlined
                    dense
                    v-model="Vendor"
                    label="Vendor"
                    :items="VendorList"
                    item-text="PrincipalName"
                ></v-select>
              </v-col>
              <v-col cols="12" sm="12" md="3">

                <v-select
                    outlined
                    dense
                    v-model="ShipTo"
                    label="Ship To"
                    :items="WarehouseList"
                    item-text="WarehouseName"
                ></v-select>

              </v-col>
              <v-col cols="12" sm="12" md="3">
                
                <v-select
                    outlined
                    dense
                    v-model="Bill"
                    label="Bill"
                    :items="WarehouseList"
                    item-text="WarehouseName"
                ></v-select>

              </v-col>

              <v-col cols="12" sm="12" md="3">
                  
                  <v-autocomplete
                    outlined
                    dense
                    :items="PurchaseTypeList"
                    item-text="PurchaseTypeName"
                    label="Purchase Type"
                    v-model="PurchaseType"
                  ></v-autocomplete> 
                </v-col>


              <!-- <v-col cols="12" sm="12" md="3">
                <v-file-input
                  outlined
                    dense
                  v-model="files"
                  label="Quoute"
                ></v-file-input>
              </v-col> -->
            </v-row>

          </v-col>
          <!--Encabezado-->

          <!--Encabezado 2 -->
          <!-- <v-col cols="12" sm="12" md="12">
            <v-row>
              <v-col cols="12" sm="12" md="6">
                  <v-text-field
                    label="Subject"
                    v-model="Subject"
                  ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                  <v-text-field
                    label="CC"
                    v-model="CC"
                  ></v-text-field>
              </v-col>
            </v-row>
          </v-col> -->
          <!--Encabezado 2 -->


          <!--Datatable-->
          <v-col cols="12" sm="12" md="12">
            <v-row>
              <v-col cols="12" sm="12" md="2">
                  
                  <v-autocomplete
                    outlined
                    dense
                    :items="UsersList"
                    item-text="username"
                    label="Purchase Agent"
                    v-model="PurchaseAgent"
                  ></v-autocomplete> 
                </v-col>


              <v-col cols="12" sm="12" md="2" >
                  <v-select
                    outlined
                    dense
                    
                    v-model="TypeCurrency"
                    label="Currency"
                    :items="CurrencyList"
                    item-text="CurrencyAbre"
                ></v-select>
              </v-col>

              

                <v-col cols="12" sm="12" md="6">
                  
                  <v-autocomplete
                    outlined
                    dense
                    :items="MaterialList"
                    item-text="Name"
                    label="Materials"
                    v-model="MaterialData"
                  ></v-autocomplete> 
                </v-col>
                <v-col cols="12" sm="12" md="2"  v-if="Vendor != '' &&  ShipTo != '' && Bill != '' && TypeCurrency !='' && PurchaseAgent != '' && PurchaseType != ''">
                    <v-btn
                       
                        class="mx-2"
                        fab
                        dark
                        small
                        color="green"
                        v-on:click="AgregarCarrito(MaterialData)"
                    >
                    <v-icon dark>
                        mdi-plus
                    </v-icon>
                    </v-btn>
                </v-col>
                <v-col cols="12" sm="12" md="2" v-else>
                  <v-badge
                    
                    left
                    content="Complete the application form"
                    color="error"
                   
                    overlap
                  >

                  <v-btn
                        class="mx-2"
                        fab
                        dark
                        small
                        color="grey"
                    >
                    <v-icon dark>
                        mdi-plus
                    </v-icon>
                    </v-btn>
                  </v-badge>
                </v-col>

                

                
            </v-row>
            <v-data-table
              :headers="headers"
              :items="desserts"
              :items-per-page="15"
              class="elevation-1"
                dense
                multi-sort 
                :headers-length='100'
                height='400'
                fixed-header
            >
            <template v-slot:item.Qty="{ item }">
                 <v-text-field
                    v-model="item.Qty"
                    type="number"
                    dense
                    v-on:keyup="UpdatePrice(item)"
                    v-on:click.capture="UpdatePrice(item)"
                  ></v-text-field>
            </template>

            <template v-slot:item.Price="{ item }">
                 <v-text-field
                    v-model="item.Price"
                    type="number"
                    dense
                    v-on:keyup="UpdatePrice(item)"
                    v-on:click.capture="UpdatePrice(item)"
                  ></v-text-field>
            </template>

            <template v-slot:item.Tax="{ item }">
                {{item.Tax.toLocaleString("en-US", {minimumFractionDigits: 2}) }}
            </template>

            <template v-slot:item.SubTotal="{ item }">
                  {{item.SubTotal.toLocaleString("en-US", {minimumFractionDigits: 2}) }}
            </template>

            </v-data-table>
          </v-col>
          <!--Datatable-->
          
          <!--Apartado de comentario y subtotales-->
          <v-col cols="12" sm="12" md="12">
            <v-row>
              <v-col cols="12" sm="12" md="6">
                <v-textarea
                  outlined
                  v-model="Nota"
                  name="Nota"
                  label="Nota"
                  
                ></v-textarea>
              </v-col>
              <v-col cols="12" sm="12" md="1"></v-col>
              <v-col cols="12" sm="12" md="5">
                  <!--Table SubTotales-->
                  <v-simple-table >
                    <template v-slot:default>
                      <thead>
                        <tr>
                          <th class="text-left red--text" >
                            <h1>Sub Total </h1>
                          </th>
                          <th class="text-left">
                           <h1>{{TypeCurrency}} {{SubTotal_.toLocaleString("en-US", {minimumFractionDigits: 2})}}</h1> 
                          </th>
                        </tr>
                      </thead>
                      <thead>
                        <tr>
                          <th class="text-left red--text">
                            <h1>Tax </h1> 
                          </th>
                          <th class="text-left">
                            <h1>{{TypeCurrency}} {{Tax_.toLocaleString("en-US", {minimumFractionDigits: 2})}}</h1>
                          </th>
                        </tr>
                      </thead>
                      <thead>
                        <tr>
                          <th class="text-left red--text">
                            <h1>Total </h1> 
                          </th>
                          <th class="text-left">
                           <h1>{{TypeCurrency}} {{Total_.toLocaleString("en-US", {minimumFractionDigits: 2})}}</h1>
                          </th>
                        </tr>
                      </thead>
                    </template>
                  </v-simple-table>
                  <!--Table SubTotales-->
              </v-col>
            </v-row>
          </v-col>
          <!--Apartado de comentario y subtotales-->

          <template v-if="Vendor != '' &&  ShipTo != '' && Bill != '' && TypeCurrency !='' && PurchaseAgent != '' && desserts.length > 0">
            <v-btn dark color="green" block v-on:click="SavePO()" >
              Save Purchase Order
            </v-btn>
          </template >
          <template v-else>
            <v-btn dark color="grey" block >
              Save Purchase Order
            </v-btn>
          </template>
          
        </v-row>
        </v-container>
      </v-card>
    </v-container>
    

    <!--Notificacion-->

    <v-snackbar
      v-model="Snackbar"
      :color="Color"
      top
      app
      right
    >
      <h3> <v-icon > mdi-48px {{mdi}}</v-icon> {{ Text }} </h3>
    </v-snackbar>
    <!--Notificacion-->

  </div>
</template>
<script>

export default {
  
  name: "",
  data: () => ({
    //SnackBar
    Snackbar:false,
    Color:'',
    Text:'',
    mdi:'',
    //SnackBar
    breadcrumbsI: [
      {
        text: "Dashboard",
        disabled: false,
        to: "/",
      },
      {
        text: "Purchase Order",
        disabled: false,
        to: "/",
      },
      {
        text: "Create",
        disabled: true,
        to: "",
      },
    ],

    headers: [
          { text: 'Qty', value: 'Qty' , 'class':'white--text black darken-3 ',width:"10" },
          { text: 'Product', value: 'Product' , 'class':'white--text black darken-3 ',width:"100"},
          { text: 'PartNumber', value: 'PartNumber' , 'class':'white--text black darken-3 ',width:"100"},
          { text: 'Description', value: 'Description' , 'class':'white--text black darken-3 ',width:"100"},
          { text: 'Price', value: 'Price' , 'class':'white--text black darken-3 ',width:"10"},
          { text: 'Tax %', value: 'isv' , 'class':'white--text black darken-3 ',width:"10"},
          { text: 'Tax', value: 'Tax' , 'class':'white--text black darken-3 ',width:"10"},
          { text: 'SubTotal', value: 'SubTotal' , 'class':'white--text black darken-3 ',width:"10"},
        ],

    desserts:[],
    StatusList:[],
    VendorList:[],
    PurchaseTypeList:[],
    WarehouseList:[],
    CurrencyList:[],
    MaterialList:[],
    UsersList:[],
    
    //Formulario
    Vendor:'',
    ShipTo:'',
    Bill:'',
    files: [],
    Subject:'',
    CC:'',
    MaterialData:'',
    Nota:'',
    TypeCurrency:'',
    PurchaseAgent:'',
    PurchaseType:'',

    Tax_ :0,
    SubTotal_:0,
    Total_:0,

  }),
  mounted() {
    this.$store.commit('bartitlex', 'Manual Purchase Order')
    this.$store.commit("breadcrumbsx", this.breadcrumbsI);
    this.STList()
    this.VDRList()
    this.PTList()
    this.CRList()
    this.WHList()
    this.MTRList()
    this.USRList()

  },
  methods: {
    async STList(){
      var self=this;
      await axios.get('/api/Status')
      .then(function(res){
          let i = 0
          for(i in res.data){
              if(res.data[i].is_purchaseorder){
                  self.StatusList.push(res.data[i])
              }
          }   
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async VDRList(){
      var self=this;
      await axios.get('/api/Adrresses')
      .then(function(res){
          let i = 0
          for(i in res.data){
              if(res.data[i].is_vendor){
                  self.VendorList.push(res.data[i])
              }
          }   
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async PTList(){
      var self=this;
      await axios.get('/api/PurchaseType')
      .then(function(res){
          self.PurchaseTypeList = res.data
              
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async CRList(){
      var self=this;
      await axios.get('/api/Currency')
      .then(function(res){
          self.CurrencyList = res.data
          
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async WHList(){
      var self=this;
      await axios.get('/api/Warehouse')
      .then(function(res){
          self.WarehouseList = res.data
          
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async MTRList(){
      var self=this;
      await axios.get('/api/Materials')
      .then(function(res){
          self.MaterialList = res.data
          
      })
      .catch(function(err){
          console.log(err)
      })
    },

    async USRList(){
      var self=this;
      await axios.get('/api/Users')
      .then(function(res){
          self.UsersList = res.data
          
      })
      .catch(function(err){
          console.log(err)
      })
    },


    AgregarCarrito(item){
      //Agregar a lista de deseos :D
      var self=this;
      let encontrado = false
      let i =0 
      for(i in self.MaterialList){
          if(self.MaterialList[i].Name === item){
            if(self.desserts.length === 0 ){
           
              self.desserts.push({
                  Qty: self.MaterialList[i].Component.MinimunOrdered,
                  Product:self.MaterialList[i].Name,
                  PartNumber:self.MaterialList[i].PartNumber,
                  Description:self.MaterialList[i].Description,
                  Price:self.MaterialList[i].Component.NominalCost,
                  isv : self.MaterialList[i].Component.tax,
                  Tax: (parseFloat(self.MaterialList[i].Component.NominalCost) * self.MaterialList[i].Component.MinimunOrdered)*  parseFloat(self.MaterialList[i].Component.tax),
                  SubTotal:((parseFloat(self.MaterialList[i].Component.NominalCost) * self.MaterialList[i].Component.MinimunOrdered)*  parseFloat(self.MaterialList[i].Component.tax) ) + (self.MaterialList[i].Component.NominalCost * self.MaterialList[i].Component.MinimunOrdered)
              })
              self.Updatetotales()
              self.MaterialData = ''
            }
            else{
            
              //buscamos si existe el material
              encontrado = false
              let x =0 
              for(x in self.desserts){
                if(self.desserts[x].Product === item){
                  encontrado = true
                 
                  break  
                }
                else{
                  encontrado = false
                }
              }

              if(encontrado=== false){
                  self.desserts.push({
                    Qty: self.MaterialList[i].Component.MinimunOrdered,
                    Product:self.MaterialList[i].Name,
                    PartNumber:self.MaterialList[i].PartNumber,
                    Description:self.MaterialList[i].Description,
                    Price:self.MaterialList[i].Component.NominalCost,
                    isv : self.MaterialList[i].Component.tax,
                    Tax: (parseFloat(self.MaterialList[i].Component.NominalCost) * self.MaterialList[i].Component.MinimunOrdered)*  parseFloat(self.MaterialList[i].Component.tax),
                    SubTotal:((parseFloat(self.MaterialList[i].Component.NominalCost) * self.MaterialList[i].Component.MinimunOrdered)*  parseFloat(self.MaterialList[i].Component.tax) ) + (self.MaterialList[i].Component.NominalCost * self.MaterialList[i].Component.MinimunOrdered)
                })
              }
              if(encontrado === true){
                self.Snackbar=true
                self.Color='red'
                self.mdi = 'mdi-alert'
                self.Text='Material adding in list the purchase!!!'
                self.MaterialData = ''
              }

              self.Updatetotales()
            }
              
            encontrado= false
            self.MaterialData = ''
          }
          
          self.MaterialData = ''
      
            /* self.Snackbar=true
            self.Color='red'
            self.mdi = 'mdi-alert'
            self.Text='Material adding in list the purchase!!!'
            self.MaterialData = '' */
       
        
      }

      self.Updatetotales()
    },

    UpdatePrice(item){
      var self=this;
      let tax = 0
      let subt = 0
      let i =0

      tax = (parseFloat(item.Price) * item.Qty)*  parseFloat(item.isv)
      subt = ((parseFloat(item.Price) * item.Qty)*  parseFloat(item.isv) ) + (item.Price * item.Qty)
      for(i in self.desserts){
        if(self.desserts[i].PartNumber === item.PartNumber){
          console.log(item.PartNumber)
          
          self.desserts[i].Tax = tax 
          self.desserts[i].SubTotal = subt
        }
      }

      subt = 0
      tax = 0

      self.Updatetotales()
    },

    Updatetotales(){
      
      var self=this;

      self.Tax_ = 0
      self.SubTotal_= 0
      self.Total_= 0
      let i = 0
      for(i in self.desserts){
        self.Tax_ += self.desserts[i].Tax
        self.SubTotal_ += self.desserts[i].SubTotal

      }
      self.Total_ = self.Tax_ + self.SubTotal_

    },

    async SavePO(){
       var self=this;
       //console.log(self.files)
       let editedItem={
              Vendor:self.Vendor,
              ShipTo:self.ShipTo,
              Bill:self.Bill,
              Quotes:'',
              Subject:self.Subject,
              CC:self.CC,
              Nota:self.Nota,
              TypeCurrency:self.TypeCurrency,
              PurchaseAgent:self.PurchaseAgent,
              Tax_:self.Tax_,
              SubTotal_:self.SubTotal_,
              Total_:self.Total_,
              PurchaseType:self.PurchaseType
          }
      
      
     
       await axios.post('/apitux/SavePOManualAxios',{
          editedItem:editedItem,
          detail : self.desserts,
          action : 'Create',
       })
       .then(function(res){
          console.log(res.data)
          self.Snackbar=true
          self.Color='green'
          self.mdi = 'mdi-content-save'
          self.Text='Purchase order created successfully (' + res.data.PO + ')'

          self.Vendor=''
          self.ShipTo=''
          self.Bill=''
          self.files= []
          self.Subject=''
          self.CC=''
          self.MaterialData=''
          self.Nota=''
          self.TypeCurrency=''
          self.PurchaseAgent=''
          self.PurchaseType=''
          self.desserts=[]

          self.Tax_ =0
          self.SubTotal_=0
          self.Total_=0
       })
       .catch(function(err){
          console.log(err)
       })
    },
  },
}
</script>