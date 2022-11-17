<template>
  <div class="container">
    <div>MainPage</div>
    <FooterComponent />
  </div>
</template>

<script>
import FooterComponent from "../components/FooterComponent.vue";
export default {
  name: "MainPage",
  components: {
    FooterComponent,
  },
};
</script>

<style scoped>
.container {
  /* background-color: #111827; */
}
</style>
