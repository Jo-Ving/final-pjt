<template>
  <div class="movieCard">
    <img
      src="https://www.movieflavor.com/images/10/101946ac09ca78ff19303144fe2e5676.jpeg"
      alt=""
    />
    <div>
      <h6 class="title">Title</h6>
      <div>
        <div>
          <p>2022</p>
          <p>TMDB 7.7</p>
        </div>
        <p>❤</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
};
</script>

<style scoped>
.movieCard {
  width: 183px;
  height: 275px;
  border: 1px solid white;
}
img {
  width: 80%;
  height: 80%;
}
p {
  margin: 0;
  font-size: 10px;
}
.title {
  margin: 0;
}
</style>
