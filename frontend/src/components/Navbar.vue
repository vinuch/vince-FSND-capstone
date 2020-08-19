<template>
  <div>
    <nav class="flex fixed w-full bg-white justify-between  py-4 px-4 sm:px-10 shadow-md z-40">
      <h1 class="font-extrabold text-2xl "><a href="/">Sony Studios</a> </h1>
      <div class="hidden sm:block">
        <input class="border rounded-l-lg py-1 px-2" type="text" name="" id="" size="40">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded-r-lg">
          Search
        </button>
      </div>
      <ul class="hidden lg:flex items-center">
        <li class="px-4 font-bold ">
          <a href="/actors" class="nav-link border-b-2 border-blue-300 text-gray-600">Actors</a> 
        </li>
        <li class="px-4 font-bold">
          <a href="/movies" class="nav-link hover:text-gray-600">Movies</a> 
        </li>
        <li class="px-4 font-bold">
          <button  class="bg-blue-500 px-4 py-1 text-white rounded-md font-bold">
            
            <a v-if="this.auth.token" :href="loginLink">Logout</a>
            <a v-else :href="loginLink">Login</a>
          </button>
        </li>
      </ul>
      <button class="block lg:hidden">
        <img class="w-8 p-1" src="../assets/images/menu.svg" alt="menu icon">
      </button>
    </nav>
  </div>
</template>

<script>
import AuthService from '../auth/AuthService.js'
// const auth = new AuthService()
const auth = new AuthService()


  export default {
    data(){
      return {
        auth,
        loginLink: auth.build_login_link('/tabs/user-page'),

      }
    }
  }
</script>

<style scoped>

.nav-link::after {
    content: '';
    display: block;
    width: 0;
    height: 2px;
    background: #90cdf4;
    transition: width .3s;
}

.nav-link:hover::after {
    width: 100%;
    transition: width .3s;
}
</style>