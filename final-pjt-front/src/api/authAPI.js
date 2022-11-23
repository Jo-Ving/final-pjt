// import { toNextRouter } from "@/router/routingLogic";
// import router from "@/router";
import router from "@/router";
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
  },
  (error) => {
    console.log(error, 16);
    // alert("에러가 발생했습니다, 다시 시도해 주세요");
  }
);

const authResponseLogic = (token) => {
  token ? setLocalStorage(LOCALSTORAGE_KEYS.userJWT, token) : "";
  router.push({ path: "/" });
  location.reload();
};

export const fetchLogin = async ({ username, password }) => {
  try {
    const data = await instance.post("/api/token/", {
      username,
      password,
    });
    console.log(data, "🎈");
    const token = data.access;
    authResponseLogic(token);
    // router.push({ path: "/" });
    // location.reload();

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
    authResponseLogic(token);
    // router.push({ path: "/pickRecommendData" });
    // location.reload();
  } catch (err) {
    console.log(err, "🎇");
  }
};

export const createReview = async ({ content, reviewScore, movieId }) => {
  const url = movieUrl(apiEndpoint.movieReviewCreate, movieId);
  console.log(url);
  try {
    const data = await instance.post(url, {
      content,
      review_score: reviewScore,
    });
    console.log(data);
    return data;
  } catch (err) {
    console.log(err);
  }
};

export const fetchReview = async ({ movieId }, setData) => {
  const url = movieUrl(apiEndpoint.movieReviewCreate, movieId);
  console.log(url);
  try {
    const data = await instance.get(url);
    console.log(data);
    setData(data);
    return data;
  } catch (err) {
    console.log(err);
  }
};

export let cachedMovies = [];

export const fetchMovies = async (setData) => {
  if (cachedMovies.length > 0) {
    setData(cachedMovies);
    return;
  }
  try {
    const data = await instance.get(apiEndpoint.movies);
    setData(data);
    cachedMovies = data;
  } catch (err) {
    console.log(err);
  }
};

export const fetchMovieDetail = async (setData, movieId) => {
  const url = movieUrl(apiEndpoint.movieDetail, movieId);

  try {
    const data = await instance.get(url);
    setData(data);
  } catch (err) {
    console.log(err);
  }
};

export const fetchLikeState = async (movieId) => {
  const url = movieUrl(apiEndpoint.movieLikeState, movieId);
  try {
    const data = await instance.post(url);
    console.log(data, "🎈");
  } catch (err) {
    console.log(err);
  }
};

export const fetchLikeMovies = async (setData) => {
  try {
    const data = await instance.get(apiEndpoint.likedMovies);
    setData(data);
  } catch (err) {
    console.log(err);
  }
};

export const pickRecommendMovies = async () => {
  try {
    const data = await instance.post();
    console.log(data);
  } catch (err) {
    console.log(err);
  }
};
