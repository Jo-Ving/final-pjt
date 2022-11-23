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
  height: 90vh;
  width: 100vw;
  margin: 0;
}
</style>
