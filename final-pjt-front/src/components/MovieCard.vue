<template>
  <div class="cardContainer">
    <div class="container" v-if="movie">
      <div @click="onMovieClick">
        <img
          :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          alt=""
        />
        <div>
          <h6 class="title">{{ movie?.title }}</h6>
          <div>
            <div class="desc-container">
              <hr />
              <h6 class="date desc">{{ movie?.release_date }}</h6>
              <h6 class="vote desc">{{ movie?.vote_average }}</h6>
            </div>
          </div>
        </div>
      </div>
      <button class="like-button" @click="onlikeButtonClick">
        {{ likeButtonState ? "💛" : "🤍" }}
      </button>
    </div>
  </div>
</template>

<script>
import { fetchLikeState } from "../api/authAPI";
import {
  getLocalStorage,
  LOCALSTORAGE_KEYS,
} from "../utils/localStorage/LocalStorage";

export default {
  name: "MovieCard",
  data() {
    return {
      likeButtonState: false,
    };
  },
  props: {
    movie: Object,
  },
  methods: {
    onlikeButtonClick() {
      this.$emit("likeButtonclick", this.movie.id);
      fetchLikeState(this.movie.id);
      this.likeButtonState = !this.likeButtonState;
    },
    onMovieClick() {
      this.$router.push({
        name: "detail",
        params: { id: this.movie.id },
      });
    },
    likeState() {
      this.likeButtonState = this.movie?.like_users.includes(this.getUserId())
        ? true
        : false;
    },
    getUserId() {
      return getLocalStorage(LOCALSTORAGE_KEYS.userJWT).userId;
    },
  },
  created() {
    this.likeState();
  },
};
</script>

<style scoped>
hr {
  margin: 3px;
}

/* .movieCard {
  width: 183px;
  height: 275px;
  border: 1px solid white;
} */
img {
  width: 80%;
  height: 80%;
  /* width: 262px;
  height: 393px;
  padding-top: 2px;
  margin-top: 15px;
  border-radius: 16px; */
}
p {
  margin: 0;
  font-size: 10px;
}
button {
  outline: none;
  border: none;
  background: transparent;
}
.cardContainer {
  display: inline-block;
  max-width: 262px;
  max-height: 393px;
  min-width: 180px;
  min-height: 310px;
}
.container {
  cursor: pointer;
  margin: 1rem;
}
.title {
  margin: 0;
  margin-top: 10px;
  font-weight: bold;
}
.desc-container {
  margin-top: 10px;
}
.desc {
  margin: 0;
  margin-left: 15px;
  margin-right: 15px;
}
.desc.date {
  text-align: left;
}

.desc.vote {
  text-align: right;
}
.like-button {
  align-items: left;
}
</style>
