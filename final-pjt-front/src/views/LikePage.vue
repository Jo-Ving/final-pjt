<template>
  <div>
    <ul>
      <li v-for="movies in LikeMovies" :key="movies">{{ movies }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "LikePage",
  data() {
    return {
      likeMovies: [],
    };
  },
};
</script>

<style></style>
