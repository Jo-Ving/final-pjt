<template>
  <div>
    <h1>Pick your movies!</h1>
    <button @click="goHome"> pick!! </button>
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
  methods: {
    goHome() {
      this.$router.push({ name:'main' })
    },
  },  
};
</script>

<style></style>
