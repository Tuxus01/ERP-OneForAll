<template>
    <div class="py-1 px-1">
   
        <template>
            <v-data-table
                :headers="headers"
                :items="desserts"
                group-by="Vendor.PrincipalName"
                class="elevation-1"
                dense
                multi-sort 
                :headers-length='100'
                :items-per-page="100"
                height='600'
                fixed-header
                :single-expand="singleExpand"
                :expanded.sync="expanded"
                item-key="PO"
                show-expand
                :loading="carga" loading-text="Loading... Please wait"

            >
                <template v-slot:item.SubTotal="{ item }">
                    {{item.TypeCurrency.CurrencyAbre}}{{item.SubTotal.toLocaleString("en-US", {minimumFractionDigits: 2})}}
                </template>
                <template v-slot:item.Total="{ item }">
                    {{item.TypeCurrency.CurrencyAbre}}{{item.Total.toLocaleString("en-US", {minimumFractionDigits: 2})}}
                </template>
                <template v-slot:item.Tax="{ item }">
                    {{item.TypeCurrency.CurrencyAbre}}{{item.Tax.toLocaleString("en-US", {minimumFractionDigits: 2})}}
                </template>



                <template v-slot:expanded-item="{ headers, item }">
                    <td :colspan="headers.length">

                        <v-data-table
                            :headers="headersDetail"
                            :items="item.Detail"
                            class="elevation-1"
                            dense
                            multi-sort 
                            :headers-length='80'
                            :items-per-page="20"
                            height='300'
                            fixed-header
                            
                        >

                        </v-data-table>
                       
                    </td>
                </template>


                <template v-slot:top>
                <v-toolbar
                    flat
                >
                    <v-toolbar-title>Purchase Order</v-toolbar-title>
                    <v-divider
                    class="mx-4"
                    inset
                    vertical
                    ></v-divider>
                    <v-select
                        :items="['Propose','Issued','In Process','Complete','Void']"
                        dense
                        hide-details
                        v-model="Status_PO"
                        outlined
                    ></v-select>


                    <v-btn
                            class="mx-2"
                            fab
                            dark
                            small
                            color="green"
                            v-on:click="Detail()"
                        >
                        <v-icon dark>
                            mdi-card-search
                        </v-icon>
                        </v-btn>


                    <v-spacer></v-spacer>

                    


                    <v-dialog
                    v-model="dialog"
                    max-width="500px"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            class="mx-2"
                            fab
                            dark
                            small
                            color="blue"
                            to="/CreatePurchaseOrder"
                        >
                        <v-icon dark>
                            mdi-plus
                        </v-icon>
                        </v-btn>
                    </template>
                    <v-card dark>
                        <v-card-title>
                        <span class="text-h5">{{ formTitle }}</span>
                        </v-card-title>

                        <v-card-text>
                        <v-container>
                            <v-row>
                             <v-col
                                cols="12"
                                sm="12"
                                md="12"
                                v-if="formTitle=='New Item'"
                            >
                                <v-select
                                    v-model="editedItem.Status"
                                    label="Status"
                                    id="editedItem.Status.id"
                                    :items="StatusList"
                                    item-text="StatusNames"
                                ></v-select>
                            </v-col>


                            <v-col
                                cols="12"
                                sm="12"
                                md="12"
                                v-if="formTitle=='Edit Item'"
                            >
                                <v-select
                                    v-model="editedItem.Status.StatusNames"
                                    label="Status"
                                    id="editedItem.Status.id"
                                    :items="StatusList"
                                    item-text="StatusNames"
                                ></v-select>
                            </v-col>
                            </v-row>
                        </v-container>
                        </v-card-text>

                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="close"
                        >
                            Cancel
                        </v-btn>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="save"
                        >
                            Save
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                        <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                        <v-spacer></v-spacer>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>

                    <v-text-field
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="Search"
                        
                        hide-details
                        outlined
                        dense
                    ></v-text-field>


                </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                <v-icon
                    small
                    class="mr-2"
                    @click="editItem(item)"
                >
                    mdi-pencil
                </v-icon>
                <v-icon
                    small
                    @click="deleteItem(item)"
                >
                    mdi-delete
                </v-icon>
                </template>
                <!-- <template v-slot:no-data>
                <v-btn
                    color="primary"
                    @click="initialize"
                >
                    Reset
                </v-btn>
                </template> -->
            </v-data-table>
            </template>
            <Alert color="red" :text=textAX icon="mdi-shield-remove-outline" :snackbarA="snackbarAX"/>

    </div>
</template>
<script>
import Axios from 'axios'
import Alert from "@/components/Alert.vue"

export default {
    components: {
       Alert
    },
    name: "",
    data: () => ({
        expanded: [],
        singleExpand: false,

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
                text: "List",
                disabled: true,
                to: "",
            },
        ],

        dialog: false,
        dialogDelete: false,
        headers: [
            { text: '', value: 'data-table-expand', 'class':'white--text black darken-3 ' },
            { text: 'Status', value: 'Status.StatusNames' , 'class':'white--text black darken-3 '},
            { text: 'PO', value: 'PO' , 'class':'white--text black darken-3 '},
            { text: 'Purchase Agent', value: 'PurchaseAgent.username' , 'class':'white--text black darken-3 '},

            { text: 'Order Date', value: 'date_create' , 'class':'white--text black darken-3 '},
            { text: 'Branch', value: 'Branch.NameBranch' , 'class':'white--text black darken-3 '},
            { text: 'ETA', value: 'ETA' , 'class':'white--text black darken-3 '},
            //{ text: 'Subject', value: 'Subject' , 'class':'white--text black darken-3 '},
            { text: 'Vendor', value: 'Vendor.PrincipalName' , 'class':'white--text black darken-3 '},
            { text: 'Tax', value: 'Tax' , 'class':'white--text black darken-3 '},
            { text: 'SubTotal', value: 'SubTotal' , 'class':'white--text black darken-3 '},
            { text: 'Total', value: 'Total', 'class':'white--text black darken-3 ' },
            //{ text: 'Actions', value: 'actions', sortable: false, 'class':'white--text black darken-3 ' },
        ],

        headersDetail: [
            { text: 'PartNumber', value: 'PartNumber' , 'class':'white--text green darken-3 '},
            { text: 'Price', value: 'Price' , 'class':'white--text green darken-3 '},
            { text: 'QuantityOrdered', value: 'QuantityOrdered' , 'class':'white--text green darken-3 '},
            { text: 'QuantityReceived', value: 'QuantityReceived' , 'class':'white--text green darken-3 '},
            //{ text: 'QuantityInspect', value: 'QuantityInspect' , 'class':'white--text green darken-3 '},
            //{ text: 'QuantityReject', value: 'QuantityReject' , 'class':'white--text green darken-3 '},
            { text: 'Tax', value: 'Tax' , 'class':'white--text green darken-3 '},
            { text: 'SubTotal', value: 'SubTotal' , 'class':'white--text green darken-3 '},
            { text: 'Status', value: 'Status.StatusNames' , 'class':'white--text green darken-3 '},
        ],
        desserts: [],
        dessertsDetail:[],
        editedIndex: -1,
        editedItem: {
            Branch: '',
            CategoryName: '',
            Description: '',
            Status: '',
            //protein: 0,
        },
        defaultItem: {
            Branch: '',
            CategoryName: '',
            Description: '',
            Status: '',
            //protein: 0,
        },

        StatusList:[],
        Status_PO : 'Issued',
        carga:true,
        snackbarAX:false,
        textAX:'',

    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },
    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
        
        
        
        
    },
    mounted() {
        this.Detail()
        this.$store.commit('bartitlex', '')
        this.$store.commit("breadcrumbsx", this.breadcrumbsI);
        this.STList()
        setTimeout(() => { this.initialize() }, 1100);
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


         Detail(){
            var self=this;
            self.carga = true
            self.dessertsDetail
             Axios.get(`/api/PurchaseOrderDetail/?PurchaseOrder__Status__StatusNames=${self.Status_PO}`)
            .then(function(res){
                //console.log(res.data)
                self.dessertsDetail =res.data
                self.carga = false
            })
            .catch(function(err){
                console.log(err)
                self.carga = false
            })

            setTimeout(() => { this.initialize() }, 1100);
        },
         initialize(){
            var self=this;
            self.carga = true
            self.desserts = []
            console.log(self.dessertsDetail)
             Axios.get(`/api/PurchaseOrders/?PO=&Status__StatusNames=${self.Status_PO}`)
            .then(function(res){
                if(res.data.Alert === 'Your time has expired :' || res.data.Alert === 'Your profile not has permissions to run queries'){
                    //alert(res.data.Alert)
                    self.snackbarAX=true
                    self.textAX = res.data.Alert + ' ' + res.data.Date
                    self.carga = false
                }
                else{
                    let i = 0
                    let x = 0
                    let detail = []
                    let inf = res.data
                    for(i in inf){
                        for(x in self.dessertsDetail){
                            //console.log(self.dessertsDetail[x].PurchaseOrder)
                            if(inf[i].PO === self.dessertsDetail[x].PurchaseOrder.PO){
                                detail.push(self.dessertsDetail[x])
                            }
                        }
                        inf[i].Detail = detail
                        detail=[]
                    }
                    self.desserts =inf
                    self.carga = false
                    //console.log(self.desserts)
                }


                
            })
            .catch(function(err){
                console.log(err)
                self.carga = false
               
            })
        },

        editItem (item) {
            this.editedIndex = this.desserts.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem (item) {
            this.editedIndex = this.desserts.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },

        async deleteItemConfirm () {
            var self=this;
            await axios.post('/apitux/SavePOManualAxios',{
                editedItem:self.editedItem,
                action : 'Delete'
            })
            .then(function(res){
                self.desserts.splice(self.editedIndex, 1)
                self.closeDelete()
            })
            .catch(function(err){
                console.log(err)
            })
            
        },

        close () {
            this.dialog = false
            this.$nextTick(() => {
            this.editedItem = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.editedItem = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        save () {
            if (this.editedIndex > -1) {
            Object.assign(this.desserts[this.editedIndex], this.editedItem)
            } else {
            this.desserts.push(this.editedItem)
            }
            this.close()
        },

    },
}
</script>