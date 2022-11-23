<template>
  <div>
    <div style="padding:1rem; margin:1rem;">
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
            <div class="hstack gap-3">
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
            </div>
          </div>
          <p style="text-align: left">
            {{ movie.overview }}
          </p>

        </div>
      </div>
      <div class="detail-right">
        <form action="submit" @click.prevent>
          <InputComponent :userInput="content" @inputFromChild="getReview" />
          <button @click="onReviewSubmit">리뷰 등록하기</button>
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
    </div>
    <SliderComponent />
  </div>
</template>

<script>
import ReviewComponent from "../components/ReviewComponent.vue";
import SliderComponent from "../components/SliderComponent.vue";
import InputComponent from "../components/InputComponent.vue";
import { fetchMovieDetail, createReview, fetchReview } from "../api/authAPI";

export default {
  name: "DetailPage",
  components: {
    ReviewComponent,
    SliderComponent,
    InputComponent,
  },
  data() {
    return {
      movie: {},
      movieId: 0,
      reviews: [],
      reviewScore: 3,
      content: "",
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
      this.movie = movie;
    },
    setReviewData(reviews) {
      this.reviews = reviews;
    },
    resetInput() {
      this.content = "";
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
.detail-right {
  text-align: left;
}

.container {
  display: flex;
  border: 1px solid pink;
}
.reviews {
}
</style>