<template>
  <div>
    <div>
      <div style="padding: 1rem; margin: 1rem" class="container">
        <div class="detail-left">
          <div class="d-flex flex-column">
            <div>
              <img
                class=""
                :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                alt=""
              />
              <h4>{{ movie.title }}</h4>
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
        </div>
        <div class="detail-right">
          <form action="submit" @click.prevent>
            <StarPoint @starCheck="starPoint" />
            <InputComponent :userInput="content" @inputFromChild="getReview" />
            <!-- <button @click="onReviewSubmit">리뷰 등록하기</button> -->
            <ButtonComponent
              @onButtonClick="onReviewSubmit"
              :buttonName="`리뷰 등록`"
            />
          </form>
          <div class="reviews">
            <h4>리뷰 목록</h4>
            <ul>
              <ReviewComponent
                v-for="review in reviews"
                :review="review"
                :key="review.id"
              />
            </ul>
          </div>
        </div>
        <div>
          <SliderComponent />
        </div>
      </div>
    </div>
    <SliderComponent :movies="similarMovies" :sliderName="`Similar movies`" />
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
      // submitReviewButton: BUTTON_NAMES?.submitReview,
    };
  },
  created() {
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
  },
};
</script>

<style scoped>
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
  display: flex;
  width: 100%;
  height: 100vh;
  border: 1px solid pink;
}
.detail-left {
  width: 40%;
}
.detail-right {
  width: 60%;
  margin-left: 3rem;
  text-align: left;
  overflow-y: scroll;
}

.container {
}
.reviews {
}
</style>
