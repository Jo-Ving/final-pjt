<template>
  <div>
    <h1>Pick your movies!</h1>
    <PickMoviesComponent />
  </div>
</template>

<script>
import PickMoviesComponent from "../components/PickMoviesComponent.vue";
export default {
  name: "PickRecommendData",
  components: {
    PickMoviesComponent,
  },
};
</script>

<style></style>
