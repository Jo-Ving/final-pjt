// import { toNextRouter } from "@/router/routingLogic";
// import router from "@/router";
import {
  LOCALSTORAGE_KEYS,
  setLocalStorage,
} from "@/utils/localStorage/LocalStorage";
import axios from "axios";
import { apiEndpoint, backendBaseUrl } from "./endpoints";

const instance = axios.create({
  baseURL: backendBaseUrl,
  headers: {
    Authorization:
      "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MDk1MzM3LCJpYXQiOjE2NjkwMDg5MzcsImp0aSI6IjVkYzc2MTgyNzRjNzRkZWNhMzZjZTY3ZTRhNWVjZTQ1IiwidXNlcl9pZCI6MjN9.zz65gGeFI6zd42Mv_GjYOqasRDSF9zrRwcXv6idch6M",
  },
  timeout: 50000,
});

instance.interceptors.response.use(
  (response) => {
    const res = response.data;
    console.log(res, "🎈🎈🎈🎈");
    // console.log(res.token.access, 13);
    const token = res.access ? res.access : res.token.access;
    setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token);
    // router.beforeEach((to, from, next) => {
    // token ? next("/") : next("/login");
    // });
  },
  (error) => {
    console.log(error, 16);
    // window.history.pushState(null, "", "/signup");
    // toNextRouter(this.$router, "signup");
  }
);

export const fetchLogin = async ({ username, password }) => {
  try {
    const data = await instance.post("/accounts/token/", {
      username,
      password,
    });
    return data;
  } catch (err) {
    console.log(err);
  }
};

export const fetchSignup = async ({ username, password, passwordConfirm }) => {
  try {
    const data = await instance.post(`${apiEndpoint.signUp}`, {
      username: username,
      password: password,
      password_confirm: passwordConfirm,
    });
    console.log(data, "🎉");
    return data;
  } catch (err) {
    console.log(err, "🎇");
  }
};

export const fetchReview = async ({ username, content, reviewScore }) => {
  console.log(username, content, reviewScore);
  try {
    const data = await instance.post(`/movies/19995/reviews/`, {
      content,
      review_score: reviewScore,
    });
    console.log(data);
    return data;
  } catch (err) {
    console.log(err);
  }
};
