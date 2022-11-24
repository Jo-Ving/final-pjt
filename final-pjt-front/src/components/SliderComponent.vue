<template>
  <div class="container scrollbar">
    <h1 class="sliderTitle">{{ sliderName }}</h1>
    <!-- <swiper class="swiper" :options="swiperOption"> -->
    <!-- <swiper-slide v-for="movie in movies" :key="movie.id"> -->
    <div class="movieContainer wrapper">
      <MovieCard
        class="item"
        :movie="movie"
        v-for="movie in movies"
        :key="movie.id"
      />
    </div>
    <!-- </swiper-slide> -->
    <!-- <div class="swiper-pagination" slot="pagination"></div> -->
    <!-- </swiper> -->
  </div>
</template>

<script>
import MovieCard from "./MovieCard.vue";
// swiper
// import { Swiper, SwiperSlide } from "vue-awesome-swiper";
// import "swiper/css/swiper.css";

export default {
  name: "SliderComponent",
  components: {
    MovieCard,
    //  Swiper, SwiperSlide
  },
  props: {
    movies: Array,
    sliderName: String,
  },
  data() {
    return {
      // swiperOption: {
      //   slidesPerView: 3,
      //   spaceBetween: 30,
      //   freeMode: true,
      //   pagination: {
      //     el: ".swiper-pagination",
      //     clickable: true,
      //   },
      // },
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
  display: flex;
  flex-direction: column;
  /* border: 1px solid pink; */
}
/* .container ::-webkit-scrollbar {
  display: none;
} */
.slider {
}
.movieContainer {
  display: flex;
  overflow-x: scroll;
}

/* scrollbar  */

/* .scrollbar {
  margin-left: 30px;
  float: left;
  height: 300px;
  width: 65px;
  background: #f5f5f5;
  overflow-y: scroll;
  margin-bottom: 25px;
}

.force-overflow {
  min-height: 450px;
}

#wrapper {
  text-align: center;
  width: 500px;
  margin: auto;
}

#style-1::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: #f5f5f5;
}

#style-1::-webkit-scrollbar {
  width: 12px;
  background-color: #f5f5f5;
}

#style-1::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #555;
} */
</style>
