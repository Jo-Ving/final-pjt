<template>
  <div>
    <nav>
      <router-link to="/">HOME</router-link> |
      <router-link to="/auth">Login</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "BrowserRouter",
};
</script>

<style></style>
