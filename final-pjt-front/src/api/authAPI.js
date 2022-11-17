import axios from "axios";

const instance = axios.create({
  baseURL: "",
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
