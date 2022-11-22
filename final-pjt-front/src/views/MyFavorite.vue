<template>
  <div>
    myFavorite
    <ul>
      <li v-for="movie in movies" :key="movie">{{ movie }}</li>
    </ul>
  </div>
</template>

<script>
import { fetchLikeMovies } from "../api/authAPI";
import { toNextRouter } from "../router/routingLogic";
import {
  getLocalStorage,
  LOCALSTORAGE_KEYS,
} from "../utils/localStorage/LocalStorage";
export default {
  name: "myFavorite",
  data() {
    return {
      movies: [],
    };
  },
  created() {
    fetchLikeMovies(this.setData);
    const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
    jwt ? "" : toNextRouter(this.$router, "login");
  },
  methods: {
    setData(data) {
      this.movies = data.like_movies;
      console.log(data);
    },
  },
};
</script>

<style></style>
