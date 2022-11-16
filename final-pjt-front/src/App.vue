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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

:root {
  --gray8: "#111827";
  --gray7: "#374151";
  --gray6: "#4B5563";
  --gray5: "#6B7280";
  --gray4: "#9CA3AF";
  --gray3: "#D1D5DB";
  --gray2: "#E5E7EB";
  --gray1: "#E5E7EB";
  --gray0: "#F9FAFB";
}
</style>
