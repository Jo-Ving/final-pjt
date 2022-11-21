export const setLocalStorage = (key, value) => {
  localStorage.setItem(key, JSON.stringify(value));
};

export const getLocalStorage = (key) => {
  const getLocalStorage = localStorage.getItem(key);
  return JSON.parse(getLocalStorage);
};

export const LOCALSTORAGE_KEYS = Object.freeze({
  userJWT: "userJWT",
});
