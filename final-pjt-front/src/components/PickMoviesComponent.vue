<template>
  <div>
    <ul>
      <MovieCard v-for="(movie, index) in movies" :key="index" :movie="movie" />
    </ul>
  </div>
</template>

<script>
import { fetchMovies } from "../api/authAPI";
import MovieCard from "./MovieCard.vue";

export default {
  name: "MoviesComponent",
  components: { MovieCard },
  data() {
    return {
      movies: [],
    };
  },
  created() {
    fetchMovies(this.setData);
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
  },
};
</script>

<style></style>
