<template>
  <div>
    <ul>
      <MovieCard v-for="(movie, index) in movies" :key="index" :movie="movie" />
    </ul>
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

<style></style>
