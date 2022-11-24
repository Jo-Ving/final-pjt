<template>
  <div>
    <h1 class="sliderTitle">{{ sliderName }}</h1>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <div class="movieContainer">
          <MovieCard :movie="movie" />
        </div>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
import MovieCard from "./MovieCard.vue";
// swiper
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: "SliderComponent",
  components: { MovieCard, Swiper, SwiperSlide },
  props: {
    movies: Array,
    sliderName: String,
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 30,
        freeMode: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      },
    };
  },
};
</script>

<style scoped>
.sliderTitle {
  margin-top: 3rem;
  font-size: 50px;
}
.container {
  border: 1px solid pink;
  overflow: hidden;
}
.slider {
}
.movieContainer {
}
</style>
