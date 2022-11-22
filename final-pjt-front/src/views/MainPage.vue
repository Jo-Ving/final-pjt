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
import { fetchLikeMovies, fetchMovies } from "../api/authAPI";

export default {
  name: "MainPage",
  components: { SliderComponent, CoverMovie, MoviesComponent },
  data() {
    return {
      movies: [],
      likedMovies: [],
      userMovies: [],
    };
  },
  created() {
    fetchMovies(this.setData);
    fetchLikeMovies();
    this.compareMovies();
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
    setLikedMoviesData(data) {
      this.likedMovies = data;
    },
    compareMovies() {
      this.movis.map((movie) => {
        if (this.likedMovies.includes(movie)) {
          const newMovie = { ...movie, isUserLiked: true };
          this.userMovies.push(newMovie);
        }
      });
      console.log(this.userMovies);
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
