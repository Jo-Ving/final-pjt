<template>
  <div style="display: inline-block">
    <div class="container" style="padding: 1rem; margin: 1rem" v-if="movie">
      <div @click="onMoviePick">
        <img
          style="
            width: 162px;
            height: 253px;
            padding-top: 2px;
            margin-top: 15px;
            border-radius: 16px;
          "
          :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          alt=""
        />
      </div>
    </div>
  </div>
</template>

<script>
import { pickMovie } from "../api/authAPI";
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  methods: {
    onMoviePick() {
      pickMovie(this.movie.id);
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
}
p {
  margin: 0;
  font-size: 10px;
}
.container {
  cursor: pointer;
}
.title {
  margin: 0;
}
</style>
