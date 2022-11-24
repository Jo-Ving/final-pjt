<template>
  <div class="container">
    <!-- header1  -->
    <CoverMovie />
    <!-- movies you must watch  -->
    <div class="movieContainer">
      <SliderComponent
        v-if="recommendData"
        :movies="recommendData"
        :sliderName="`RECOMMEND`"
      />
      <SliderComponent
        v-if="recentMovies"
        :movies="recentMovies"
        :sliderName="`LATEST MOVIES`"
      />
      <SliderComponent
        v-if="hotMovies"
        :movies="hotMovies"
        :sliderName="`HOT MOVIES`"
      />
      <!-- <MoviesComponent :movies="movies" /> -->
    </div>
  </div>
</template>

<script>
import SliderComponent from "../components/SliderComponent.vue";
import CoverMovie from "../components/CoverMovie.vue";
// import MoviesComponent from "../components/MoviesComponent.vue";
import {
  fetchLikeMovies,
  fetchMovies,
  fetchRecommend1,
  fetchRecommend2,
} from "../api/authAPI";

export default {
  name: "MainPage",
  components: {
    SliderComponent,
    CoverMovie,
    // MoviesComponent,
  },
  data() {
    return {
      movies: [],
      likedMovies: [],
      userMovies: [],
      hotMovies: [],
      recentMovies: [],
      recommendData: [],
    };
  },
  created() {
    fetchRecommend1(this.setRecentData, this.setHotData);
    fetchRecommend2(this.setRecommendData);
    fetchMovies(this.setData);
    fetchLikeMovies();

    this.compareMovies();
  },
  methods: {
    setData(data) {
      this.movies = data;
    },
    setRecommendData(data) {
      this.recommendData = data;
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
