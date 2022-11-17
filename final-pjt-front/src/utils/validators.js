import { EMAIL_REGEXP } from "./regExp";

export const checkEmailValidate = (email) => {
  return EMAIL_REGEXP.test(email);
};
