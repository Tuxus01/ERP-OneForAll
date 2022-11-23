import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    
    USER : '',
    ID_Token : '',
    CSRF_TOKEN:'',
    //Permisos 
    
    bartitle : '',
    breadcrumbs:[],
    perms : null


  },
  mutations: {
    usuario (state,datos) {
      state.USER = datos
    },
    id (state,datos) {
      state.ID_Token = datos
    },
    tokens (state,datos) {
      state.CSRF_TOKEN = datos
    },
    
    bartitlex (state,datos) {
      state.bartitle = datos
    },
    breadcrumbsx (state,datos) {
      state.breadcrumbs = datos
    },
    perms (state,datos) {
      state.perms = datos
    },
  },
  actions: {
  },
  modules: {
  }
})
