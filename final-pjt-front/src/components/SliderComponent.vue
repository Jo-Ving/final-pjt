<template>
  <div class="slider">
    <ul>
      <MovieCard v-for="(movie, index) in movies" :key="index" />
    </ul>
  </div>
</template>

<script>
const movies = [1, 2, 3, 4, 5, 6];

import MovieCard from "./MovieCard.vue";
export default {
  name: "SliderComponent",
  components: { MovieCard },
  data() {
    return { movies };
  },
};
</script>

<style scoped>
ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
}

.slider {
  display: flex;
  justify-content: center;
}
</style>
