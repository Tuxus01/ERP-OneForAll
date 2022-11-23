<template>
    <div class="py-1 px-1">
    </div>
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
       {
        text: "Report",
        disabled: false,
        to: "/dashboardReport",
      },
       {
        text: "5 %",
        disabled: true,
        to: "",
      },
      
     
    ],
      
    }),
    mounted() {
      this.$store.commit('bartitlex','Dashboard Report')
      this.$store.commit("breadcrumbsx",this.breadcrumbsI);
    },
    methods: {
      
    },
}
</script>