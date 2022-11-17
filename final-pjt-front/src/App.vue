<template>
  <div id="app">
    <BrowserRouter />
  </div>
</template>

<script>
import BrowserRouter from "./BrowserRouter.vue";
export default {
  name: "app",
  components: { BrowserRouter },
};
</script>

<style>
@import "./assets/style.css";

body {
  margin: 0;
  color: var(--gray0);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: var(--gray8);
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
