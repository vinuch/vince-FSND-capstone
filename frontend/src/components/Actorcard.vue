<template>

    <div v-if="!editing" class="bg-gray-100 mb-8 sm:w-3/12 py-10 px-6 cursor-pointer transition duration-500 ease-in-out transform hover:-translate-y-4 hover:shadow-xl hover:scale-105">
      
      <img class="rounded-lg shadow-2xl w-72 h-auto mb-10" :src="actor.image" alt="idris elba">
      <p class="font-bold tracking-wider text-lg mb-4">{{actor.name}}</p>
      <p class="text-xs">{{actor.bio}}</p>

      <div class="flex justify-center items-end mt-6 ">
        <button :disabled="!auth.can('patch:actors') ? 'disabled' : false " @click="editing = true" class="mx-4 py-1 rounded-md px-4 bg-blue-300 text-white" :class="auth.can('patch:actors') ? 'hover:bg-blue-500': 'false'">
          Edit Actor
        </button>
        <button class="mx-4 py-1 rounded-md px-4 bg-red-300 hover:bg-red-500 text-white">
          Delete Actor
        </button>
      </div>
    </div>


      <EditCard @close="editing = !editing" v-else :actor="actor"/>




</template>

<script>
import EditCard from '@/components/EditCard.vue'

  export default {
    props: ['actor',],
    components: {
      EditCard
    },
    data(){
      return {
        auth: this.$auth,
        editing: false
      }
    },

  }
</script>

<style lang="scss" scoped>

</style>