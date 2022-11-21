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
export default {
  name: "myFavorite",
  data() {
    return {
      movies: [],
    };
  },
  created() {
    fetchLikeMovies(this.setData);
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
  },
};
</script>

<style></style>
