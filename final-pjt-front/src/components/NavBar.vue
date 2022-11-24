<template>
  <nav class="container">
    <div class="logo">Jo-ving</div>
    <div class="navBar">
      <ul class="nav-left navItem">
        <li><router-link to="/">HOME</router-link></li>
        <li><router-link to="/myfavorite">내가 찜한 콘텐츠</router-link></li>
      </ul>

      <ul class="nav-right navItem">
        <li>
          <router-link to="/search">검색</router-link>
        </li>
        <li v-if="!isUserLoggedIn">
          <router-link to="/login">Login</router-link>
        </li>
        <li v-if="isUserLoggedIn" @click="onLogout">
          <router-link to="/login">Logout</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import {
  getLocalStorage,
  deleteLocalStorage,
  LOCALSTORAGE_KEYS,
} from "../utils/localStorage/LocalStorage";
export default {
  name: "NavBar",
  data() {
    return {
      isUserLoggedIn: false,
    };
  },
  created() {
    const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
    this.isUserLoggedIn = jwt ? true : false;
  },
  methods: {
    onLogout() {
      deleteLocalStorage(LOCALSTORAGE_KEYS.userJWT);
      this.isUserLoggedIn = false;
    },
  },
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
