<template>
  <div class="container">
    <!-- header1  -->
    <CoverMovie />
    <!-- movies you must watch  -->
    <SliderComponent />
    <SliderComponent />
    <SliderComponent />
  </div>
</template>

<script>
import SliderComponent from "../components/SliderComponent.vue";
import CoverMovie from "../components/CoverMovie.vue";

export default {
  name: "MainPage",
  components: { SliderComponent, CoverMovie },
};
</script>

<style scoped>
ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
}
li {
  width: 183px;
  height: 275px;
  border: 1px solid white;
}
.slider {
  display: flex;
  justify-content: center;
}
</style>
