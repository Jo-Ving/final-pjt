<template>
  <div class="pickmovies">
    <ul>
      <PickMovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        @pickmovie="pickMovieCount"
      />
    </ul>
  </div>
</template>

<script>
// import { fetchMovies } from "../api/authAPI";
import PickMovieCard from "./PickMovieCard.vue";
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: "MoviesComponent",
  components: { PickMovieCard },
  data() {
    return {
      movies: [],
      pickedMovieCount: 0,
    };
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/pick_list`
    })
    .then((res) => {
      this.movies = res.data
      console.log(res,'aaaa')
    })
    .catch((err) => {
      console.log(err)
    })    
  },
  methods: {
    // setData(data) {
    //   this.movies = data;
    // },
    pickMovieCount(isPicked) {
      isPicked ? (this.pickedMovieCount += 1) : (this.pickedMovieCount -= 1);
      this.$emit("pickMovieCount", this.pickedMovieCount);
    },
  },
};
</script>

<style scoped>
.pickmovies {
  background-color: var(--gray8);
}
</style>
