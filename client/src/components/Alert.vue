<template>

<v-container >
    <v-snackbar
        v-model="snackbarA"
        :color="color"
        top 
        dense
        shaped
        absolute
        multi-line
        >
        <v-row>
            <v-col cols="1">
                <v-icon>
                    {{ icon }}
                </v-icon>
            </v-col>
            <v-col cols='10'>
                {{ text}}
            </v-col>
        </v-row>
    
    </v-snackbar>
</v-container>

</template>
<script>


export default {

    name : "",

    props: ['text','icon','color','snackbarA','rigth','left'],
    data: () => ({
     
        show:false,
    
    }),
    mounted() {
        this.show=snackbarA
      
    },
    methods: {

     
    }
}
</script>
