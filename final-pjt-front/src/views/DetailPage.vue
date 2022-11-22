<template>
  <div>
    <div class="container">
      <div class="detail-left">
        <img
          :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          alt=""
        />
        <h4>{{ movie.title }}</h4>
        <p>
          {{ movie.overview }}
        </p>
      </div>
      <div class="detail-right">
        <form action="submit" @click.prevent>
          <InputComponent :userInput="content" @inputFromChild="getReview" />
          <button @click="onReviewSubmit">리뷰 등록하기</button>
        </form>
        <div class="reviews">
          <h4>리뷰 목록</h4>
          <ul>
            <ReviewComponent />
            <ReviewComponent />
            <ReviewComponent />
            <ReviewComponent />
            <ReviewComponent />
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
import { fetchMovieDetail, fetchReview } from "../api/authAPI";

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
      username: "admin@gmail.com",
      reviewScore: 3,
      content: "",
    };
  },
  created() {
    const splitedLocation = location.pathname.split("/");
    const movieId = splitedLocation[splitedLocation.length - 1];
    fetchMovieDetail(this.setData, movieId);
  },
  methods: {
    getReview(content) {
      this.content = content;
      console.log(content);
    },
    onReviewSubmit() {
      fetchReview({
        username: this.username,
        content: this.content,
        reviewScore: this.reviewScore,
      });
    },
    setData(movie) {
      console.log(movie);
      this.movie = movie;
    },
  },
};
</script>

<style scoped>
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
