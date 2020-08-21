import Vue from "vue";
import Vuex from "vuex";
import axios from "axios"

const AuthAxios = axios.create({
  baseURL: 'http://127.0.0.1:5000/'
})

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('JWTS_LOCAL_KEY') || null,
    actors: [],
    movies: [],
    totalQuestions: 0,
    isLoading: true
  },
  mutations: {
    SET_ACTORS(state, payload) {
      state.actors = payload
    },
    SET_MOVIES(state, payload) {
      state.movies = payload
    },
    SET_LOADING(state, payload) {
      state.isLoading = payload
    }
  },
  actions: {
    
    async getActors({ commit}) {
      // console.log(this._vm.$auth.token);
      if(this._vm.$auth.can('get:actors')){
        AuthAxios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('JWTS_LOCAL_KEY') || null
        await AuthAxios
          .get("/actors")
          .then(function(response) {
            // handle success
            commit('SET_ACTORS', response.data.actors)
            commit('SET_LOADING', false)
          })
          .catch(function(error) {
            // handle error
            commit('SET_LOADING', false)
            console.log(error);
          })
      }else{
        commit('SET_LOADING', false)
      }   
    },


    async getMovies({ commit }) {
      if(this._vm.$auth.can('get:movies')){
        AuthAxios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('JWTS_LOCAL_KEY') || null
        await AuthAxios
          .get("/movies")
          .then(function(response) {
            // handle success
            commit('SET_MOVIES', response.data.movies)
            commit('SET_LOADING', false)
          })
          .catch(function(error) {
            // handle error
            commit('SET_LOADING', false)
            console.log(error);
          })
      }else{
        commit('SET_LOADING', false)
      } 
    },

    async updateActor({commit}, updated_actor){
      console.log(updated_actor,)
      if(this._vm.$auth.can('patch:actors')){
        AuthAxios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('JWTS_LOCAL_KEY') || null
        await AuthAxios
          .patch(`/actors/${updated_actor.id}`, updated_actor)
          .then(function(response) {
            // handle success
            commit('SET_ACTORS', response.data.new)
            commit('SET_LOADING', false)
          })
          .catch(function(error) {
            // handle error
            commit('SET_LOADING', false)
            console.log(error);
          })
      }
    }
  },
  getters: {
    actors: state => {
      return state.actors
    },
    movies: state => {
      return state.movies
    },
    token: state => {
      return state.token
    },
    isLoading: state => {
      return state.isLoading
    }
  },
});

export default store;