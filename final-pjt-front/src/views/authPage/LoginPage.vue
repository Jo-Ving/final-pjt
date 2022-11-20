<template>
  <div>
    <h1>Login</h1>
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
      <button @click="onLoginButtonClick">Login</button>
    </form>
    <p>
      Don't have an account?
      <button @click="toSignup">Sign up here</button>
    </p>
  </div>
</template>

<script>
import InputComponent from "../../components/InputComponent.vue";
import { checkEmailValidate } from "../../utils/validators";
import { EMAIL_VALIDATION_FALSE } from "../../assets/constants";
import { toNextRouter } from "../../router/routingLogic";
import axios from "axios";

// const SIGNUP_URL = `http://127.0.0.1:8000/accounts/login/`;

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      emailValidateMessage: "",
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
    onLoginButtonClick(e) {
      console.log(e.target);
      this.getUserInfo();
      this.resetInput();
    },
    resetInput() {
      this.email = "";
      this.password = "post";
    },
    toSignup() {
      toNextRouter(this.$router, "signup");
    },
    getUserInfo() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/accounts/token/`,
        data: {
          username: this.email,
          password: this.password,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>

<style></style>
