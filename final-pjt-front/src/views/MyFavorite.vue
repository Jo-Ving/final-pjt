<template>
  <div>
    <h1>내가 찜한 영화</h1>
    <ul>
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </ul>
  </div>
</template>

<script>
import MovieCard from "../components/MovieCard.vue";
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
  components: {
    MovieCard,
  },
  created() {
    fetchLikeMovies(this.setData);
    const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
    jwt ? "" : toNextRouter(this.$router, "login");
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
  },
};
</script>

<style></style>
