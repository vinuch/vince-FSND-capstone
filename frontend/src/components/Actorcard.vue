<template>
  <div class="bg-gray-100 mb-8 sm:w-3/12 py-10 px-6 cursor-pointer transition duration-500 ease-in-out transform hover:-translate-y-4 hover:shadow-xl hover:scale-105">
    
    <img class="rounded-lg shadow-2xl w-72 h-auto mb-10" :src="actor.image" alt="idris elba">
    <p class="font-bold tracking-wider text-lg mb-4">{{actor.name}}</p>
    <p class="text-xs">{{actor.bio}}</p>
  </div>
</template>

<script>
  export default {
    props: ['actor']
  }
</script>

<style lang="scss" scoped>

</style>