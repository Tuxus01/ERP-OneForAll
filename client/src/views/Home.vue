<template>
    <h1></h1>
</template>
<script>
export default {
    name : "",
    data: () => ({
     breadcrumbsI: [
      {
        text: "Dashboard",
        disabled: false,
        to: "/",
      },
       
      
     
    ],
      
    }),
    mounted() {
      this.$store.commit('bartitlex','Dashboard')
      this.$store.commit("breadcrumbsx",this.breadcrumbsI);
    },
    methods: {
      
    },
}
</script>