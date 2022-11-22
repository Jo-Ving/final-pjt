import Vue from "vue";
import VueRouter from "vue-router";
import MainPage from "../views/MainPage.vue";
import DetailPage from "../views/DetailPage.vue";
import MyFavorite from "../views/MyFavorite.vue";
import LoginPage from "../views/authPage/LoginPage.vue";
import SignupPage from "../views/authPage/SignupPage.vue";
import SearchPage from "../views/SearchPage.vue";
// import PickRecommendData from "../views/PickRecommendData.vue";

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
  {
    path: "/search",
    name: "search",
    component: SearchPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
