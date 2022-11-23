<template>
  <v-app>
    <v-app-bar dense app dark elevation="4" color="red darken-4">
      <v-toolbar-title  style="width: 100px" class="ml-4 pl-4">

        TuxApp
      </v-toolbar-title>

      <v-divider inset class="mx-1" vertical></v-divider>

      <v-menu bottom offset-y dense open-on-hover>
        <template v-slot:activator="{ on, attrs }">
          <v-btn dark v-bind="attrs" v-on="on" plain>
            Inventory
          </v-btn>
        </template>

        <v-list dense v-for="item in urlInventario">
          <v-list-item :to="item.path" link>
            <v-list-item-icon>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{item.name}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

      </v-menu>




      <v-menu bottom offset-y dense open-on-hover>
        <template v-slot:activator="{ on, attrs }">
          <v-btn dark v-bind="attrs" v-on="on" plain>
            Containers
          </v-btn>
        </template>


        <v-list dense v-for="item in urlAllocated">
          <v-list-item :to="item.path" link>
            <v-list-item-icon>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{item.name}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        

      </v-menu>



      <v-menu bottom offset-y dense open-on-hover>
        <template v-slot:activator="{ on, attrs }">
          <v-btn dark v-bind="attrs" v-on="on" plain>
            Purchase Order
          </v-btn>
        </template>


        <v-list dense v-for="item in urlPurchase">
          <v-list-item :to="item.path" link>
            <v-list-item-icon>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{item.name}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        

      </v-menu>



      <v-spacer></v-spacer>


      <v-divider inset class="mx-4" vertical></v-divider>
      <v-btn href="/logout" small fab>
        <v-icon>mdi-logout</v-icon>
      </v-btn>

      <v-divider inset class="mx-4" vertical></v-divider>
      {{ $store.state.USER }}
    </v-app-bar>

    <v-main>
      <v-system-bar
          color="dark darken-4"
          height="20"
          class="elevation-5 "
          dense
        >
   
        <v-row>
          
          <v-col cols="4" class="d-flex justify-start">
          <v-breadcrumbs   :items="$store.state.breadcrumbs">
              <template v-slot:item="{ item }">
                <v-breadcrumbs-item
                  dark
                  :to="item.to"
                  :disabled="item.disabled"
                
                >
                  {{ item.text.toUpperCase() }}
                </v-breadcrumbs-item>
              </template>
            </v-breadcrumbs>
          </v-col>

         

         
          <v-col cols="4" class="d-flex justify-center py-7">
          <h2 align="center" class="black--text" >{{ $store.state.bartitle}} </h2>
          </v-col>

           <v-col cols="4">
          </v-col>

          
        </v-row>
          
      </v-system-bar>




        <router-view></router-view>
      
    </v-main>


    <v-footer color="grey darken-4" padless app dense>
      <v-row>
        <v-col cols="12" md="12" sm="12">
          <v-card-title class="py-1 white--text body-2"> &copy; {{ new Date().getFullYear() }} — TuxApp <v-spacer
              vertical></v-spacer>
            <v-icon color="white">mdi-language-python</v-icon>
            <v-icon color="green">mdi-vuejs</v-icon>
            <v-icon color="blue">mdi-vuetify</v-icon>
            <v-icon color="yellow">mdi-language-javascript</v-icon>
            <h3 class="white--text"> Developer - Christian Valladares</h3>
          </v-card-title>

        </v-col>
      </v-row>
    </v-footer>


  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {

    // HelloWorld,
  },

  data: () => ({
    snackbar: false,
    urlInventario : [
        {
          'name':'Inventory - (All Material)',
          'path':'/Materials',
          'icon':'mdi-dolly',
        },
       
        
        {
          'name':'Component - (Mateial Base)',
          'path':'/Component',
          'icon':'mdi-shape',
        },

        {
          'name':'Category',
          'path':'/Category',
          'icon':'mdi-puzzle-outline',
        },
        {
          'name':'SubCategory',
          'path':'/SubCategory',
          'icon':'mdi-puzzle',
        },
        {
          'name':'Color',
          'path':'/Color',
          'icon':'mdi-format-color-fill',
        },
        {
          'name':'Units',
          'path':'/Units',
          'icon':'mdi-ruler-square-compass',
        },
      
    ],

    urlAllocated : [
        {
          'name':'Warehouse',
          'path':'/Warehouse',
          'icon':'mdi-warehouse',
        },
        
        {
          'name':'Bins',
          'path':'/Bins',
          'icon':'mdi-warehouse',
        },
        
       
      
    ],

    urlPurchase : [
        {
          'name':'Purchase Orders',
          'path':'/PurchaseOrders',
          'icon':'mdi-currency-usd-circle-outline',
        },
        {
          'name':'Create Purchase Order',
          'path':'/CreatePurchaseOrder',
          'icon':'mdi-tag-plus-outline',
        },

        {
          'name':'Received',
          'path':'/CreatePurchaseOrder',
          'icon':'mdi-swap-horizontal-bold',
        },
    ],
    breadcrumbsI: [
      {
        text: "Dashboard",
        disabled: false,
        to: "/",
      },

    ],

  }),
  mounted() {
    var self = this;
    this.perfil()
    this.$store.commit("breadcrumbsx", this.breadcrumbsI)
    //this.timeAlertas()

  },

  methods: {


    timeAlertas() {
      var self = this;
      const start = new Date()
      if (start <= new Date('2022-08-10')) {
        self.snackbar = true
      }
    },

    /* alerta(){
      alert('Mensaje llego')
    }, */
    perfil() {
      this.$store.commit('usuario', USER_LOCAL)
      this.$store.commit('id', ID_Token)
      this.$store.commit('tokens', CSRF_TOKEN)
      //console.log(this.$store.state.CSRF_TOKEN)
      //Permisos

      this.$store.commit('perms', permsx)

    }
  },

};
</script>

  
<style>