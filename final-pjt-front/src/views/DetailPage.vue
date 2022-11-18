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
          <InputComponent :userInput="review" @inputFromChild="getReview" />
          <button @click="onSubmitReview">리뷰 등록</button>
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
import axios from "axios";

export default {
  name: "DetailPage",
  data() {
    return {
      review: "",
    };
  },
  components: {
    ReviewComponent,
    SliderComponent,
    InputComponent,
  },
  methods: {
    getReview(reviewInput) {
      console.log(reviewInput);
      this.review = reviewInput;
    },
    onSubmitReview() {
      console.log(this.review);
    },
    postReview() {
      axios({
        method: "post",
        url: ``,
        data: {
          review_score: 5,
          content: "리뷰내용입니다",
          created_at: new Date(),
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
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
