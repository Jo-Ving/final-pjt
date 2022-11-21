<template>
  <div class="container">
    <!-- header1  -->
    <CoverMovie />
    <!-- movies you must watch  -->
    <SliderComponent />
    <SliderComponent />
    <SliderComponent />
    <MoviesComponent :movies="movies" />
  </div>
</template>

<script>
import SliderComponent from "../components/SliderComponent.vue";
import CoverMovie from "../components/CoverMovie.vue";
import MoviesComponent from "../components/MoviesComponent.vue";
import { fetchMovies } from "../api/authAPI";

export default {
  name: "MainPage",
  components: { SliderComponent, CoverMovie, MoviesComponent },
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
ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
}
li {
  width: 183px;
  height: 275px;
  border: 1px solid white;
}
.slider {
  display: flex;
  justify-content: center;
}
</style>
