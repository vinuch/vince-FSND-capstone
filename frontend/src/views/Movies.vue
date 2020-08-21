<template>
  <div class="home h-full py-24 p-4 sm:px-10">
    <h1 class=" font-bold text-3xl border-b-4 border-gray-600 inline-block mb-12">MOVIES</h1>
    <div v-if="isLoading" class="flex justify-center">
      <img class="align-center" src="../assets/images/load.svg" alt="">
    </div>
    <div v-else class="flex flex-wrap justify-around">
      <Moviecard v-for="movie in movies" :key="movie.title" :movie="movie" />
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import Moviecard from '@/components/Moviecard.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'Home',
  components: {
    Moviecard
  },
  methods: {
    ...mapActions({
      getMovies: 'getMovies'
    })
  },
  computed: {
    ...mapGetters([
      'movies',
      'isLoading'
    ])
  },
  mounted() {
    this.getMovies()
  }
}
</script>
