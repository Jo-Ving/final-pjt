<template>
  <div>
    <h1>Pick your movies!</h1>
    <!-- <button @click="goHome">pick!!</button> -->
    <ButtonComponent
      :disabled="pickedCount === 0"
      @onButtonClick="goHome"
      :buttonName="`pick!!`"
    />
    <PickMoviesComponent @pickMovieCount="pickMovieCount" />
  </div>
</template>

<script>
import PickMoviesComponent from "../components/PickMoviesComponent.vue";
import ButtonComponent from "../components/ButtonComponent.vue";

export default {
  name: "PickRecommendData",
  components: {
    PickMoviesComponent,
    ButtonComponent,
  },
  data() {
    return {
      pickedCount: 0,
    };
  },
  methods: {
    goHome() {
      this.$router.push({ name: "main" });
    },
    pickMovieCount(count) {
      this.pickedCount = count;
    },
  },
};
</script>

<style></style>
