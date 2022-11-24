export const setLocalStorage = (key, value) => {
  localStorage.setItem(key, JSON.stringify(value));
};

export const getLocalStorage = (key) => {
  const getLocalStorage = localStorage.getItem(key);
  return JSON.parse(getLocalStorage);
};

export const deleteLocalStorage = (key) => {
  localStorage.removeItem(key);
};

export const LOCALSTORAGE_KEYS = Object.freeze({
  userJWT: "userJWT",
});

export const isLogin = () => {
  const userInfo = getLocalStorage(LOCALSTORAGE_KEYS.userJWT);
  const jwt = userInfo?.token;

  return jwt ? true : false;
};
