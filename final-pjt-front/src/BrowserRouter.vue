<template>
  <div>
    <NavBar />
    <div class="mainView">
      <router-view />
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterComponent from "./components/FooterComponent.vue";
export default {
  name: "BrowserRouter",
  components: { NavBar, FooterComponent },
};
</script>

<style scoped>
.mainView {
  min-height: 90vh;
}
</style>
