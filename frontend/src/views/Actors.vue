<template>
  <div class="home py-24 p-4 sm:px-10">
    <h1 class=" font-bold text-3xl border-b-4 border-gray-600 inline-block mb-12">ACTORS</h1>
    <!-- <button @click="login">login</button> -->
    <div v-if="isLoading" class="flex justify-center">
      <img class="align-center" src="../assets/images/load.svg" alt="">
    </div>

    <div v-else class="flex flex-wrap justify-around">
      <Actorcard v-for="actor in actors" :key="actor.name" :actor="actor" :editing="editing" @close="editing = !editing" />
    </div>
    <button class="mx-4 py-1 rounded-md px-4 bg-blue-500 text-white">
         Add Actor
    </button>
     
    <!-- <EditCard /> -->
    
  </div>
</template>

<script>
// @ is an alias to /src
import Actorcard from '@/components/Actorcard.vue'
// import EditCard from '@/components/EditCard.vue'
import { mapActions, mapGetters } from 'vuex'
// import axios from 'axios'

export default {
  name: 'Home',
  components: {
    // EditCard,
    Actorcard
  },
  data(){
    return {
      editing: false
    }
  },
  methods: {
    login(){
      this.$AuthAxios
        .get("/login")
        .then(function(response) {
          // handle success

          console.log(response);
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
    },
    ...mapActions({
      getActors: 'getActors'
    })
  },
  computed: {
    ...mapGetters([
      'actors',
      'isLoading'
    ])
  },
  mounted() {
    this.getActors()
  },
  created() {
    this.$auth.check_token_fragment()

  }
}
</script>
