<template>
  <div v-if="creating"  class="home relative py-24 p-4 sm:px-10">
    <h1 class=" font-bold text-3xl border-b-4 border-gray-600 inline-block mb-12">ACTORS</h1>
    <!-- <button @click="login">login</button> -->
    <div v-if="isLoading" class="flex justify-center">
      <img class="align-center" src="../assets/images/load.svg" alt="">
    </div>

    <div v-else class="flex flex-wrap justify-around mb-16">
      <Actorcard v-for="actor in actors" :key="actor.name" :actor="actor" :editing="editing" @close="editing = !editing" />
    </div>

    

    <button @click="creating = !creating" class="mx-4 py-2 rounded-md px-12 bg-blue-500 text-white">
         Add Actor
    </button>
        
  </div>
  <div v-else class="absolute top-0 h-full left-0 w-full bg-blue-100 bg-opacity-50">
      <div class="mt-24 flex justify-center items-center">
        <CreateCard  @close="creating = !creating"/>
      </div>
      
    </div>
</template>

<script>
// @ is an alias to /src
import Actorcard from '@/components/Actorcard.vue'
import CreateCard from '@/components/CreateCard.vue'
// import EditCard from '@/components/EditCard.vue'
import { mapActions, mapGetters } from 'vuex'
// import axios from 'axios'

export default {
  name: 'Home',
  components: {
    CreateCard,
    Actorcard
  },
  data(){
    return {
      creating: false,
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
