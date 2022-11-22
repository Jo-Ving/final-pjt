<template>
  <div>
    myFavorite
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
    // fetchMovies(this.setLikedData);
    const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
    jwt ? "" : toNextRouter(this.$router, "login");
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
    // setLikedData(data) {
    //   const movieList = [];
    //   data.map((movie) => {
    //     if (this.movieIds.includes(movie.id)) {
    //       movieList.push(movie);
    //     }
    //   });
    //   console.log(this.movies, "🎈");
    //   console.log(data);
    //   this.movies = movieList;
    // },
  },
};
</script>

<style></style>
