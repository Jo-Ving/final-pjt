<template>
  <div class="pickmovies">
    <ul>
      <PickMovieCard
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
    </ul>
  </div>
</template>

<script>
import { fetchMovies } from "../api/authAPI";
import PickMovieCard from "./PickMovieCard.vue";

export default {
  name: "MoviesComponent",
  components: { PickMovieCard },
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

<style scoped>
.pickmovies {
  background-color: var(--gray8);
}
</style>
