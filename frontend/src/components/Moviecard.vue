<template>
  <div v-if="!editing" class="bg-gray-100 mb-8 sm:w-3/12 py-10 px-6 cursor-pointer transition duration-500 ease-in-out transform hover:-translate-y-4 hover:shadow-xl hover:scale-105">
    
    <img class="rounded-lg shadow-2xl w-72 h-auto mb-10" :src="movie.cover_image" alt="idris elba">
    <p class="font-bold tracking-wider text-lg mb-4">{{movie.title}}</p>
    <p class="text-xs">{{movie.description}}</p>

    <div class="flex justify-center items-end mt-6 ">
        <button :disabled="!auth.can('patch:movies') ? 'disabled' : false " @click="editing = true" class="text-xs mx-4 py-2 rounded-md px-4 bg-blue-500 text-white" :class="auth.can('patch:actors') ? 'bg-blue-300': 'false'">
          Edit Movie
        </button>
        <button @click="deleteMovieClicked" class="text-xs mx-2 py-2 rounded-md px-4 bg-black text-white">
          Delete Movie
        </button>
      </div>
  </div>

  <EditMovieCard @close="editing = !editing" v-else :movie="movie"/>

</template>

<script>
import EditMovieCard from '@/components/EditMovieCard.vue'
import { mapActions } from 'vuex'

  export default {
    props: ['movie'],
    components: {
      EditMovieCard
    },
    data() {
      return {
        auth: this.$auth,
        editing: false
      }
    },
    methods: {
      ...mapActions({
        deleteMovie: 'deleteMovie'
      }),
      deleteMovieClicked() {
        if(confirm('Are you sure you want to delete this actor? you cant get it back if you do')){
          this.deleteMovie(this.movie.id)
        }
        
      }
    }

  }
</script>

<style lang="scss" scoped>

</style>

