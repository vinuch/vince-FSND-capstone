import Vue from "vue";
import Vuex from "vuex";
import axios from "axios"

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    actors: [],
    movies: [],
    totalQuestions: 0,
  },
  mutations: {
    SET_ACTORS(state, payload) {
      state.actors = payload
    },
    SET_MOVIES(state, payload) {
      state.movies = payload
    }
  },
  actions: {
    getActors({ commit }) {
      axios
        .get("/actors")
        .then(function(response) {
          // handle success
          commit('SET_ACTORS', response.data.actors)
          console.log(response);
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
        
    },
    getMovies({ commit }) {
      axios
        .get("/movies")
        .then(function(response) {
          // handle success
          commit('SET_MOVIES', response.data.movies)
          console.log(response);
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
        
    },
  },
  getters: {
    actors: state => {
      return state.actors
    },
    movies: state => {
      return state.movies
    }
  },
});

export default store;