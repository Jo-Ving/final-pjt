import {
  getLocalStorage,
  LOCALSTORAGE_KEYS,
} from "@/utils/localStorage/LocalStorage";
import router from ".";

export const toNextRouter = (currentRoute, name) => {
  currentRoute.push({ name });
};

export const checkUser = () => {
  const jwt = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
  jwt ? "" : router.push({ path: "/login" });
  return;
};
