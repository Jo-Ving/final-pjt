import axios from "axios";
import { apiEndpoint, backendBaseUrl } from "./endpoints";

const instance = axios.create({
  baseURL: backendBaseUrl,
  headers: {},
  timeout: 50000,
});

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
