<template>
  <div>
    <form action="submit" @click.prevent>
      <StarPoint />
      <InputComponent
        :userInput="searchInput"
        :labelName="`검색`"
        @inputFromChild="onSearch"
      />
    </form>
    <MoviesComponent :movies="searchedMovies" />

    <!-- <ul>
      <li v-for="movie in searchedMovies" :key="movie.id">
        {{ movie.title }}
      </li>
    </ul> -->
  </div>
</template>

<script>
import InputComponent from "../components/InputComponent.vue";
import { fetchMovies } from "../api/authAPI";
import MoviesComponent from "../components/MoviesComponent.vue";
import StarPoint from "../components/StarPoint.vue";

export default {
  name: "SearchPage",
  components: { InputComponent, MoviesComponent, StarPoint },
  data() {
    return {
      searchInput: "",
      movies: [],
      searchedMovies: [],
    };
  },
  methods: {
    onSearch(e) {
      if (e.trim() !== "") {
        this.serchedMovies(e);
      } else {
        this.searchedMovies = [];
      }
    },
    setData(movies) {
      this.movies = movies;
    },
    serchedMovies(input) {
      this.searchedMovies = [];
      for (const movie of this.movies) {
        const isInclude = movie.title.includes(input);
        isInclude ? this.searchedMovies.push(movie) : "";
      }
    },
  },
  created() {
    fetchMovies(this.setData);
  },
};
</script>

<style></style>
