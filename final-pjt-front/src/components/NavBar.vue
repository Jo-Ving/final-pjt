<template>
  <nav class="container">
    <div class="logo">Logo</div>
    <div class="navBar">
      <nav>
        <ul class="nav-left navItem">
          <li><router-link to="/">HOME</router-link></li>
          <li><router-link to="/myfavorite">내가 찜한 콘텐츠</router-link></li>
        </ul>
        <ul class="nav-right navItem">
          <li>검색</li>
          <li>햄버거바</li>
          <li><router-link to="/login">Login</router-link></li>
        </ul>
      </nav>
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
  background-color: var(--gray8);
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
