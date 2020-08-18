<template>
  <div class="home h-screen pt-24 p-4 sm:px-10">
    <h1 class=" font-bold text-3xl border-b-4 border-gray-600 inline-block">Actors</h1>
    <Actorcard />
  </div>
</template>

<script>
// @ is an alias to /src
import Actorcard from '@/components/Actorcard.vue'


export default {
  name: 'Home',
  components: {
    Actorcard
  }
}
</script>
