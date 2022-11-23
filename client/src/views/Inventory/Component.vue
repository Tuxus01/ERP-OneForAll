<template>
    <div class="py-1 px-1">
       
        <template>
            <v-data-table
                :headers="headers"
                :items="desserts"
                sort-by="ComponentName"
                class="elevation-1"
                dense
                multi-sort 
                :headers-length='100'
                height='600'
                fixed-header
            >
                <template v-slot:top>
                <v-toolbar
                    flat
                >
                    <v-toolbar-title>Component's</v-toolbar-title>
                    <v-divider
                    class="mx-4"
                    inset
                    vertical
                    ></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog
                    v-model="dialog"
                    max-width="1500px"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            class="mx-2"
                            fab
                            dark
                            small
                            color="blue"
                            v-bind="attrs"
                            v-on="on"
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
                                md="6"
                            >
                                <v-text-field
                                v-model="editedItem.ComponentName"
                                label="Component Name"
                                ></v-text-field>
                            </v-col>
                            

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='New Item'"
                            >
                                <v-select
                                v-model="editedItem.Category"
                                label="Category"
                                id="editedItem.Category"
                                :items="CategoryList"
                                item-text="CategoryName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='Edit Item'"
                            >
                                <v-select
                                v-model="editedItem.Category.CategoryName"
                                label="Category"
                                id="editedItem.Category"
                                :items="CategoryList"
                                item-text="CategoryName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='New Item'"
                            >
                                <v-select
                                v-model="editedItem.SubCategory"
                                label="SubCategory"
                                id="editedItem.SubCategory.id"
                                :items="SubCategoryList"
                                item-text="SubCategoryName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='Edit Item'"
                            >
                                <v-select
                                v-model="editedItem.SubCategory.SubCategoryName"
                                label="SubCategory"
                                id="editedItem.SubCategory.id"
                                :items="SubCategoryList"
                                item-text="SubCategoryName"
                                ></v-select>
                            </v-col>


                           
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                v-model="editedItem.MinimunOrdered"
                                label="Minimun Ordered"
                                ></v-text-field>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                v-model="editedItem.tax"
                                label="tax"
                                ></v-text-field>
                            </v-col>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                v-model="editedItem.NominalCost"
                                label="NominalCost"
                                ></v-text-field>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="6"
                                md="3"
                            >
                                <v-text-field
                                v-model="editedItem.MinimunStock"
                                label="MinimunStock"
                                ></v-text-field>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='New Item'"
                            >
                                <v-select
                                v-model="editedItem.UsageUnit"
                                label="UsageUnit"
                                id="editedItem.UsageUnit.id"
                                :items="UnitList"
                                item-text="UnitName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='Edit Item'"
                            >
                                <v-select
                                v-model="editedItem.UsageUnit.UnitName"
                                label="UsageUnit"
                                id="editedItem.UsageUnit.id"
                                :items="UnitList"
                                item-text="UnitName"
                                ></v-select>
                            </v-col>


                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='New Item'"
                            >
                                <v-select
                                v-model="editedItem.PurchasUnit"
                                label="PurchasUnit"
                                id="editedItem.PurchasUnit.id"
                                :items="UnitList"
                                item-text="UnitName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
                                v-if="formTitle=='Edit Item'"
                            >
                                <v-select
                                v-model="editedItem.PurchasUnit.UnitName"
                                label="PurchasUnit"
                                id="editedItem.PurchasUnit.id"
                                :items="UnitList"
                                item-text="UnitName"
                                ></v-select>
                            </v-col>

                            <v-col
                                cols="12"
                                sm="12"
                                md="3"
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
                                md="3"
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
                                
                                <v-col
                                cols="12"
                                sm="12"
                                md="12"
                            >
                                <v-textarea
                                v-model="editedItem.Comment"
                                label="Description"
                                ></v-textarea>
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
                <template v-slot:no-data>
                <v-btn
                    color="primary"
                    @click="initialize"
                >
                    Reset
                </v-btn>
                </template>
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
        breadcrumbsI: [
            {
                text: "Dashboard",
                disabled: false,
                to: "/",
            },
            {
                text: "Inventory",
                disabled: false,
                to: "/",
            },
            {
                text: "Component",
                disabled: true,
                to: "",
            },
        ],

        dialog: false,
        dialogDelete: false,
        headers: [
            {
            text: 'Branch',
            align: 'start',
            sortable: false,
            value: 'Branch.NameBranch', 'class':'white--text black darken-3 '
            },
            
            { text: 'ComponentName', value: 'ComponentName' , 'class':'white--text black darken-3 '},
            { text: 'NominalCost', value: 'NominalCost' , 'class':'white--text black darken-3 '},
            { text: 'MinimunStock', value: 'MinimunStock' , 'class':'white--text black darken-3 '},
            { text: 'Minimun Ordered', value: 'MinimunOrdered' , 'class':'white--text black darken-3 '},
            { text: 'Category', value: 'Category.CategoryName' , 'class':'white--text black darken-3 '},
            { text: 'SubCategory', value: 'SubCategory.SubCategoryName' , 'class':'white--text black darken-3 '},
            { text: 'UsageUnit', value: 'UsageUnit.UnitName', 'class':'white--text black darken-3 ' },
            { text: 'PurchasUnit', value: 'PurchasUnit.UnitName' , 'class':'white--text black darken-3 '},
            { text: 'CoversionFactor', value: 'CoversionFactor' , 'class':'white--text black darken-3 '},

            { text: 'Status', value: 'Status.StatusNames' , 'class':'white--text black darken-3 '},
            //{ text: 'Protein (g)', value: 'protein' },
            { text: 'Actions', value: 'actions', sortable: false, 'class':'white--text black darken-3 ' },
        ],
        desserts: [],
        editedIndex: -1,
        editedItem: {
            Branch: [],
            Category: [],
            Comment: '',
            ComponentName: '',
            CoversionFactor: 1,
            MinimunStock:1,
            NominalCost:0,
            PurchasUnit:[],
            Status:[],
            SubCategory:[],
            UsageUnit:[],
            MinimunOrdered:0,
            date_change:'',
            date_create:'',
            date_time_c:'',
            date_time_m:'',
            id:0,
            tax:0,
        },
        defaultItem: {
            Branch: [],
            Category: [],
            Comment: '',
            ComponentName: '',
            CoversionFactor: 1,
            MinimunStock:1,
            NominalCost:0,
            PurchasUnit:[],
            Status:[],
            SubCategory:[],
            UsageUnit:[],
            MinimunOrdered:0,
            date_change:'',
            date_create:'',
            date_time_c:'',
            date_time_m:'',
            id:0,
            tax:0,
        },
        StatusList:[],
        CategoryList:[],
        SubCategoryList:[],
        UnitList:[],
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
      this.initialize()
    },
    mounted() {
        this.$store.commit('bartitlex', '')
        this.$store.commit("breadcrumbsx", this.breadcrumbsI);
        this.STList()
        this.CatList()
        this.SubCatList()
        this.UnitsList()
    },
    methods: {

        async STList(){
            var self=this;
            await axios.get('/api/Status')
            .then(function(res){
                let i = 0
                for(i in res.data){
                    if(res.data[i].is_material){
                        self.StatusList.push(res.data[i])
                    }
                }
                 
            })
            .catch(function(err){
                console.log(err)
            })
        },

        async CatList(){
            var self=this;
            await axios.get('/api/Category')
            .then(function(res){
                self.CategoryList = res.data
                 
            })
            .catch(function(err){
                console.log(err)
            })
        },

        async SubCatList(){
            var self=this;
            await axios.get('/api/SubCategory')
            .then(function(res){
                self.SubCategoryList = res.data
                 
            })
            .catch(function(err){
                console.log(err)
            })
        },

        async UnitsList(){
            var self=this;
            await axios.get('/api/Units')
            .then(function(res){
                self.UnitList = res.data
                 
            })
            .catch(function(err){
                console.log(err)
            })
        },

        async initialize(){
            var self=this;
            self.snackbarAX=false
            self.textAX = ''
            await Axios.get('/api/Component')
            .then(function(res){
                
                if(res.data.Alert === 'Your time has expired :' || res.data.Alert === 'Your profile not has permissions to run queries'){
                    //alert(res.data.Alert)
                    self.snackbarAX=true
                    self.textAX = res.data.Alert + ' ' + res.data.Date
                }
                else{
                    self.desserts =res.data
                }
            })
            .catch(function(err){
                console.log(err)
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
            await axios.post('/apitux/ComponentAxios',{
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

        async save () {
            var self=this;
            if (this.editedIndex > -1) {
                ///Edit or Update
                await axios.post('/apitux/ComponentAxios',{
                    editedItem:self.editedItem,
                    action : 'Edit'
                })
                .then(function(res){
                    Object.assign(self.desserts[self.editedIndex], self.editedItem)
                })
                .catch(function(err){
                    console.log(err)
                })
            } 
            else {
                //Create
                
                await axios.post('/apitux/ComponentAxios',{
                    editedItem:self.editedItem,
                    action : 'Create'
                })
                .then(function(res){
                    axios.get(`/api/Component/?search=${res.data.id}`)
                    .then(function(rsp){
                            self.editedItem = rsp.data[0]
                            self.desserts.push(self.editedItem)
                            self.desserts.sort(compareValues('id', 'desc'));
                    })
                    //Object.assign(self.desserts[self.editedIndex], self.editedItem)
                })
                .catch(function(err){
                    console.log(err)
                })


                
            }
            this.close()
        },

    },
}
</script>