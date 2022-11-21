<template>
  <div>
    <h1>Signup</h1>
    <form action="submit" @click.prevent>
      <div>
        <InputComponent
          :userInput="email"
          :labelName="`email*`"
          @inputFromChild="getEmailValue"
        />
        <p>{{ emailValidateMessage }}</p>
      </div>
      <div>
        <InputComponent
          :userInput="password"
          :labelName="`password*`"
          @inputFromChild="getPasswordValue"
        />
      </div>
      <div>
        <InputComponent
          :userInput="passwordConfirm"
          :labelName="`password*`"
          @inputFromChild="getPasswordConfirmValue"
        />
        <p>{{ passwordEqualMessage }}</p>
      </div>
      <button @click="onSignUpButtonClick">Sign up</button>
    </form>
    <p>
      have an account?
      <button @click="toLoginPage">Log in here</button>
    </p>
  </div>
</template>

<script>
import InputComponent from "../../components/InputComponent.vue";
import { checkEmailValidate, checkPasswordEqal } from "../../utils/validators";
import {
  EMAIL_VALIDATION_FALSE,
  PASSWORD_EQUAL_FALSE,
} from "../../assets/constants";
import { toNextRouter } from "../../router/routingLogic";
import { fetchSignup } from "../../api/authAPI";

// import axios from "axios";

// const SIGNUP_URL = `http://127.0.0.1:8000/accounts/signup/`;

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      passwordConfirm: "",
      emailValidateMessage: "",
      passwordEqualMessage: "",
    };
  },
  components: {
    InputComponent,
  },
  methods: {
    getEmailValue(email) {
      this.emailValidateMessage = checkEmailValidate(email)
        ? ""
        : EMAIL_VALIDATION_FALSE;
      this.email = email;
    },
    getPasswordValue(password) {
      this.password = password;
    },
    getPasswordConfirmValue(passwordConfirm) {
      this.passwordConfirm = passwordConfirm;
      this.passwordEqualMessage = checkPasswordEqal(
        this.password,
        this.passwordConfirm
      )
        ? ""
        : PASSWORD_EQUAL_FALSE;
    },
    onSignUpButtonClick(e) {
      console.log(e.target);
      fetchSignup({
        username: this.email,
        password: this.password,
        passwordConfirm: this.passwordConfirm,
      });
      // this.sendUserInfo();
      this.resetInput();
    },
    resetInput() {
      this.email = "";
      this.password = "";
      this.passwordConfirm = "";
    },
    toLoginPage() {
      toNextRouter(this.$router, "login");
    },
    // sendUserInfo() {
    //   axios({
    //     method: "post",
    //     url: SIGNUP_URL,
    //     data: {
    //       username: this.email,
    //       password: this.password,
    //       password_confirm: this.passwordConfirm,
    //     },
    //   })
    //     .then((res) => {
    //       console.log(res);
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },
  },
};
</script>

<style></style>
