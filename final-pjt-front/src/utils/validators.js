import { EMAIL_REGEXP } from "./regExp";

export const checkEmailValidate = (email) => {
  return EMAIL_REGEXP.test(email);
};

export const checkPasswordEqal = (password, passwordComfirm) => {
  return password === passwordComfirm;
};
