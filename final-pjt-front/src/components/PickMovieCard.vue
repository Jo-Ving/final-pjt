<template>
  <div class="conatainer" @click="isPicked">
    <!-- <div class="movieCard" > -->
    <div
      class="movieCard"
      v-if="movie"
      @click="onMoviePick"
      :class="{ isPicked: isPicked }"
    >
      <img
        :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
        alt=""
      />
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
import { pickMovie } from "../api/authAPI";
export default {
  name: "MovieCard",
  data() {
    return {
      isPicked: false,
    };
  },
  props: {
    movie: Object,
  },
  methods: {
    onMoviePick() {
      pickMovie(this.movie.id);
      this.isPicked = !this.isPicked;
    },
  },
};
</script>

<style scoped>
/* .movieCard {
  width: 183px;
  height: 275px;
  border: 1px solid white;
} */

img {
  width: 80%;
  height: 80%;
  width: 162px;
  height: 253px;
  padding-top: 2px;
  border-radius: 16px;
  box-sizing: border-box;
}
p {
  margin: 0;
  font-size: 10px;
}
.conatainer {
  display: inline-block;
  box-sizing: border-box;
}
.movieCard {
  cursor: pointer;
  padding: 1rem;
  margin: 1rem;
  margin-top: 2rem;
  box-sizing: border-box;
}

.title {
  margin: 0;
}
.isPicked {
  border-inline: 2px solid #7ee5eb;

  border-radius: 16px;
  box-sizing: border-box;
  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset,
    rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
}
</style>
