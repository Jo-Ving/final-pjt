// import { toNextRouter } from "@/router/routingLogic";
// import router from "@/router";
import {
  getLocalStorage,
  LOCALSTORAGE_KEYS,
  setLocalStorage,
} from "@/utils/localStorage/LocalStorage";
import axios from "axios";
import { apiEndpoint, backendBaseUrl, movieUrl } from "./endpoints";

const checkAuth = () => {
  const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
  if (jwt) {
    return `Bearer ${jwt}`;
  }
  return "";
};

const instance = axios.create({
  baseURL: backendBaseUrl,
  headers: {
    Authorization: checkAuth(),
  },
  timeout: 50000,
});

instance.interceptors.response.use(
  (response) => {
    const res = response.data;
    console.log(res);
    return res;
    // const token = res.access || res?.token.access;
    // if (token) {
    // setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token);
    // }
  },
  (error) => {
    console.log(error, 16);
  }
);

export const fetchLogin = async ({ username, password }) => {
  try {
    const data = await instance.post("/api/token/", {
      username,
      password,
    });
    const token = data.access;
    setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token);
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
    const token = data.token.access;
    setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token);
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

export const fetchMovies = async (setData) => {
  try {
    const data = await instance.get(apiEndpoint.movies);
    setData(data);
  } catch (err) {
    console.log(err);
  }
};

export const fetchLikeState = async (movieId) => {
  const url = movieUrl(apiEndpoint.movieLikeState, movieId);
  try {
    const data = await instance.post(url, {});
    console.log(data);
  } catch (err) {
    console.log(err);
  }
};

export const fetchLikeMovies = async (setData) => {
  try {
    const data = await instance.get(apiEndpoint.likedMovies);
    console.log(data, "hello");
    setData(data);
  } catch (err) {
    console.log(err);
  }
};
