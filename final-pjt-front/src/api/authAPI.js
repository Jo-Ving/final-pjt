// import { toNextRouter } from "@/router/routingLogic";
import router from "@/router";
import {
  LOCALSTORAGE_KEYS,
  setLocalStorage,
} from "@/utils/localStorage/LocalStorage";
import axios from "axios";
import { apiEndpoint, backendBaseUrl } from "./endpoints";

const instance = axios.create({
  baseURL: backendBaseUrl,
  headers: {},
  timeout: 50000,
});

instance.interceptors.response.use(
  (response) => {
    const res = response.data;
    // console.log(res.token.access, 13);
    const token = res.access ? res.access : res.token.access;
    setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token);
    router.beforeEach((to, from, next) => {
      token ? next("/") : next("/login");
    });
  },
  (error) => {
    console.log(error, 16);
    window.history.pushState(null, "", "/signup");
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
