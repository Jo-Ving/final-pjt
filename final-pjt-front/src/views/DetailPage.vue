<template>
  <div>
    <div class="container">
      <div class="detail-left">
        <img
          src="https://img.vogue.co.kr/vogue/2019/04/style_5ca1c2b8da359.jpg"
          alt=""
        />
        <h4>Title</h4>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim magnam
          ducimus totam architecto minima, veritatis omnis mollitia facere
          ratione harum, unde qui pariatur alias tenetur quos, animi earum!
          Ducimus, id.
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
import { fetchReview } from "../api/authAPI";

export default {
  name: "DetailPage",
  components: {
    ReviewComponent,
    SliderComponent,
    InputComponent,
  },
  data() {
    return {
      username: "admin@gmail.com",
      reviewScore: 3,
      content: "",
    };
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
