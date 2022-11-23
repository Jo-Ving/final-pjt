<template>
  <div class="cardContainer">
    <div class="container" v-if="movie">
      <div @click="onMovieClick">
        <img
          style="
            width: 262px;
            height: 393px;
            padding-top: 2px;
            margin-top: 15px;
            border-radius: 16px;
          "
          :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          alt=""
        />
        <div>
          <h6 class="title">{{ movie?.title }}</h6>
          <div>
            <div>
              <h6 class="title">{{ movie?.release_date }}</h6>
              <h6 class="title">{{ movie?.vote_average }}</h6>
            </div>
          </div>
        </div>
      </div>
      <button @click="onlikeButtonClick">❤</button>
    </div>
  </div>
</template>

<script>
import { fetchLikeState } from "../api/authAPI";
// import { toNextRouter } from "../router/routingLogic";
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  methods: {
    onlikeButtonClick() {
      fetchLikeState(this.movie.id);
    },
    onMovieClick() {
      this.$router.push({
        name: "detail",
        params: { id: this.movie.id },
      });
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
.cardContainer {
  display: inline-block;
}
.container {
  cursor: pointer;
  margin: 1rem;
}
.title {
  margin: 0;
}
</style>
