<template>
  <nav class="container">
    <div class="logo">Logo</div>
    <div class="navBar">
      <ul class="nav-left navItem">
        <li>HOME</li>
        <li>내가 찜한 콘텐츠</li>
      </ul>
      <ul class="nav-right navItem">
        <li>검색</li>
        <li>햄버거바</li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
.container {
  border: 1px solid black;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 3rem;
  padding: 0;
}
.logo {
  width: 10vw;
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
li {
  padding-left: 1rem;
}
.navBar {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 90vw;
}
.nav-left {
}
.nav-right {
}
.navItem {
  display: flex;
}
</style>
