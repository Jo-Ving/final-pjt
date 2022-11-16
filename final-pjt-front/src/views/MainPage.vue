<template>
  <div>
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

<style></style>
