<template>
  <div class="container">
      <MovieCard v-for="(movie, index) in movies" :key="index" :movie="movie" />
  </div>
</template>

<script>
import MovieCard from "./MovieCard.vue";

export default {
  name: "MoviesComponent",
  components: { MovieCard },
  props: {
    movies: Array,
  },
};
</script>

<style scoped>
/* s */
</style>
