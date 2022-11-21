import Vue from "vue";
import VueRouter from "vue-router";
import MainPage from "../views/MainPage.vue";
import DetailPage from "../views/DetailPage.vue";
import MyFavorite from "../views/MyFavorite.vue";
import LoginPage from "../views/authPage/LoginPage.vue";
import SignupPage from "../views/authPage/SignupPage.vue";

import {
  getLocalStorage,
  LOCALSTORAGE_KEYS,
} from "../utils/localStorage/LocalStorage";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "main",
    component: MainPage,
  },
  {
    path: "/login",
    name: "login",
    component: LoginPage,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupPage,
  },
  {
    path: "/detail/:id",
    name: "detail",
    component: DetailPage,
  },
  {
    path: "/myfavorite",
    name: "myfavorite",
    component: MyFavorite,
  },

  // {
  //   path: "/login",
  //   name: "login",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/authPage/LoginPage.vue"),
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// router.beforeEach((to, from, next) => {
//   next();

//   const storageJWT = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
//   if (storageJWT) {
//     next("/");
//   } else {
//     next("/login");
//   }
//   next();
// });

export default router;
