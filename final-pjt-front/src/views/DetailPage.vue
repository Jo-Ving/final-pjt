<template>
  <div class="outsideContainer">
    <div class="cont">
      <div class="container">
        <div class="detail-left">
          <div>
            <h4>{{ movie.title }}</h4>

            <img
              class=""
              :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
              alt=""
            />
            <!-- <h5>{{ movie.genres }}</h5> -->
            <li v-for="genre in genreName" :key="genre">{{ genre }}</li>
            <p>{{ movie.popularity }}</p>
          </div>
          <div class="vstack gap-1">
            <!-- <div class="hstack gap-3">
              <p>감독</p>
              <p>돼지</p>
            </div>
            <div class="hstack gap-3">
              <p>내용</p>
              <p>돼지</p>
            </div>
            <div class="hstack gap-3">
              <p>감독</p>
              <p>돼지</p>
            </div> -->
          </div>
          <p style="text-align: left">
            {{ movie.overview }}
          </p>
        </div>
        <div class="detail-right">
          <h4 class="reviewTitle">리뷰 보기</h4>

          <div class="reviewContainer">
            <form action="submit" @click.prevent>
              <StarPoint @starCheck="starPoint" />
              <div class="inputContainer">
                <InputComponent
                  class="input"
                  :userInput="content"
                  @inputFromChild="getReview"
                />
                <!-- <button @click="onReviewSubmit">리뷰 등록하기</button> -->
                <ButtonComponent
                  class="reviewSubmitButton"
                  :disabled="loginState === false"
                  @onButtonClick="onReviewSubmit"
                  :buttonName="`리뷰 등록`"
                />
              </div>
            </form>
          </div>

          <div class="reviews">
            <ul>
              <ReviewComponent
                v-for="review in reviews"
                :review="review"
                :key="review.id"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
    <SliderComponent
      class="slider"
      :movies="similarMovies"
      :sliderName="`Similar movies`"
    />
  </div>
</template>

<script>
import ReviewComponent from "../components/ReviewComponent.vue";
import SliderComponent from "../components/SliderComponent.vue";
import InputComponent from "../components/InputComponent.vue";
import StarPoint from "../components/StarPoint.vue";
import ButtonComponent from "../components/ButtonComponent.vue";
// import BUTTON_NAMES from "../assets/constants";

import { fetchMovieDetail, createReview, fetchReview } from "../api/authAPI";
import { isLogin } from "../utils/localStorage/LocalStorage";
import { genres } from "../assets/genres";
export default {
  name: "DetailPage",
  components: {
    ReviewComponent,
    SliderComponent,
    InputComponent,
    StarPoint,
    ButtonComponent,
  },
  data() {
    return {
      movie: {},
      movieId: 0,
      reviews: [],
      reviewScore: 0,
      content: "",
      similarMovies: [],
      loginState: true,
      genreName: [],
      // submitReviewButton: BUTTON_NAMES?.submitReview,
    };
  },
  created() {
    this.loginState = isLogin();
    const splitedLocation = location.pathname.split("/");
    const movieId = splitedLocation[splitedLocation.length - 1];
    this.movieId = movieId;
    fetchMovieDetail(this.setData, movieId);
    fetchReview({ movieId }, this.setReviewData);
  },
  methods: {
    getReview(content) {
      this.content = content;
    },
    onReviewSubmit() {
      const splitedLocation = location.pathname.split("/");
      const movieId = splitedLocation[splitedLocation.length - 1];
      createReview({
        content: this.content,
        reviewScore: this.reviewScore,
        movieId: movieId,
      });
      fetchReview({ movieId: this.movieId }, this.setReviewData);
      this.$forceUpdate();
      this.resetInput();
    },
    setData(movie) {
      console.log(movie);

      this.movie = movie.movie;
      this.similarMovies = movie.simliar_movies;
      this.getGenres(this.movie);
    },
    setReviewData(reviews) {
      this.reviews = reviews;
    },
    resetInput() {
      this.content = "";
    },
    starPoint(point) {
      this.reviewScore = point - 1;
    },
    getGenres(movie) {
      console.log(genres);
      genres.map((genre) => {
        console.log(genre, movie.genres);
        if (movie.genres.includes(genre.id)) {
          this.genreName.push(genre.name);
        }
      });
    },
  },
};
</script>

<style scoped>
.cont {
  display: flex;
  display: inline-block;
  padding: 3rem;
  box-shadow: 0 1px 1px rgba(238, 233, 233, 0.11),
    0 2px 2px rgba(240, 233, 233, 0.11), 0 4px 4px rgba(240, 237, 237, 0.11),
    0 8px 8px rgba(235, 233, 233, 0.11), 0 16px 16px rgba(216, 212, 212, 0.11),
    0 32px 32px rgba(238, 235, 235, 0.11);
}
.outsideContainer {
  width: 100vw;
  height: 90vh;
  margin-top: 3rem;
  margin-bottom: 3rem;
  align-items: center;
  overflow: auto;
}
h4 {
  font-size: 32px;
  font-weight: bold;
  margin-top: 3rem;
  margin-bottom: 2rem;
}
* {
  margin: 0;
  padding: 0;
}

img {
  width: 280px;
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.container {
  margin: 0px;
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: auto;
}
.detail-left {
  width: 35%;
}
.detail-right {
  width: 50%;
  height: 80vh;
  margin-left: 3rem;
  text-align: left;
  overflow-y: scroll;
  position: static;
}
.detail-right::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}

.reviewContainer {
  background-color: black;
  z-index: 99;
  position: sticky;
  top: 0;
}
.inputContainer {
  display: flex;
  flex-direction: column;
  /* border: 1px solid salmon; */
}
.reviewContainer form {
  border: 1px solid paleturquoise;
}
.reviewContainer .input {
  border: 1px solid white;
  width: 100%;
  height: 100%;
}
.reviewTitle {
  margin-top: 40px;
  margin-bottom: 20px;
}
.reviewSubmitButton {
  width: 90%;
}
.slider {
  display: inline-block;
}
</style>
