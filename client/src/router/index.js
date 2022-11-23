import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },

  //------------------ Inventory -----------------------------------//
  {
    path: '/Materials',
    name: 'Materials',
    component: () => import(/* webpackChunkName: "Materials" */ '../views/Inventory/Materials.vue')
  },
  {
    path: '/Category',
    name: 'Category',
    component: () => import(/* webpackChunkName: "Category" */ '../views/Inventory/Category.vue')
  },
  {
    path: '/SubCategory',
    name: 'SubCategory',
    component: () => import(/* webpackChunkName: "SubCategory" */ '../views/Inventory/SubCategory.vue')
  },
  {
    path: '/Color',
    name: 'Color',
    component: () => import(/* webpackChunkName: "Color" */ '../views/Inventory/Color.vue')
  },
  {
    path: '/Bins',
    name: 'Bin',
    component: () => import(/* webpackChunkName: "Bin" */ '../views/Inventory/Bin.vue')
  },

  {
    path: '/Component',
    name: 'Component',
    component: () => import(/* webpackChunkName: "Component" */ '../views/Inventory/Component.vue')
  },

  {
    path: '/Units',
    name: 'Units',
    component: () => import(/* webpackChunkName: "Units" */ '../views/Inventory/Units.vue')
  },

  {
    path: '/Warehouse',
    name: 'Warehouse',
    component: () => import(/* webpackChunkName: "Warehouse" */ '../views/Inventory/Warehouse.vue')
  },
  //------------------ Inventory -----------------------------------//



  //------------------ Purchase Orders -----------------------------------//
  {
    path: '/PurchaseOrders',
    name: 'PurchaseOrders',
    component: () => import(/* webpackChunkName: "PurchaseOrders" */ '../views/PurchaseOrder/PurchaseOrders.vue')
  },
  {
    path: '/CreatePurchaseOrder',
    name: 'PurchaseOrdersCreate',
    component: () => import(/* webpackChunkName: "PurchaseOrdersCreate" */ '../views/PurchaseOrder/PurchaseOrdersCreate.vue')
  },
  //------------------ Purchase Orders -----------------------------------//

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
