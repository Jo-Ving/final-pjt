import axios from "axios";
import { apiEndpoint, backendBaseUrl } from "./endpoints";

const instance = axios.create({
  baseURL: backendBaseUrl,
  headers: {},
  timeout: 50000,
});

export const fetchLogin = async ({ email, password }) => {
  try {
    const data = await instance.post("/login", { email, password });
    return data;
  } catch (err) {
    console.log(err);
  }
};

export const fetchSignup = async ({ email, password, passwordConfirm }) => {
  try {
    const data = await instance.post(`${apiEndpoint.signUp}`, {
      email,
      password,
      password_confirm: passwordConfirm,
    });
    console.log(data, "🎉");
    return data;
  } catch (err) {
    console.log(err, "🎇");
  }
};
