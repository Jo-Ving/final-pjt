<template>
  <div class="container">
    <!-- header1  -->
    <CoverMovie />
    <!-- movies you must watch  -->
    <div class="movieContainer">
      <SliderComponent :movies="recentMovies" :sliderName="`RECENT MOVIES`" />
      <SliderComponent :movies="hotMovies" :sliderName="`HOT MOVIES`" />
      <SliderComponent />
      <MoviesComponent :movies="movies" />
    </div>
  </div>
</template>

<script>
import SliderComponent from "../components/SliderComponent.vue";
import CoverMovie from "../components/CoverMovie.vue";
import MoviesComponent from "../components/MoviesComponent.vue";
import { fetchLikeMovies, fetchMovies, fetchRecommend1 } from "../api/authAPI";

export default {
  name: "MainPage",
  components: {
    SliderComponent,
    CoverMovie,
    MoviesComponent,
  },
  data() {
    return {
      movies: [],
      likedMovies: [],
      userMovies: [],
      hotMovies: [],
      recentMovies: [],
    };
  },
  created() {
    fetchRecommend1(this.setRecentData, this.setHotData);
    fetchMovies(this.setData);
    fetchLikeMovies();

    this.compareMovies();
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
    setRecentData(data) {
      this.recentMovies = data;
    },
    setHotData(data) {
      this.hotMovies = data;
    },
    setLikedMoviesData(data) {
      this.likedMovies = data;
    },
    compareMovies() {
      // fetchLikeMovies((data) => {
      //   console.log(data);
      // });
      this.movies?.map((movie) => {
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

<style lang="scss" scoped>
/* @import "./base.scss"; */
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
.container {
}
.movieContainer {
}
</style>
