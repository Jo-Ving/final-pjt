<template>
  <div class="container">
    <NavBar />
    <div>MainPage</div>
    <FooterComponent />
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import FooterComponent from "../components/FooterComponent.vue";
export default {
  name: "MainPage",
  components: {
    NavBar,
    FooterComponent,
  },
};
</script>

<style scoped>
.container {
  /* background-color: #111827; */
  background-color: var(--gray8);
}
</style>
