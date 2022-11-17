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
      <button>Sign up here</button>
    </p>
  </div>
</template>

<script>
import InputComponent from "../components/InputComponent.vue";
import { checkEmailValidate } from "../utils/validators";
import { EMAIL_VALIDATION_FALSE } from "../assets/constants";

export default {
  name: "MainPage",
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
      this.resetInput();
    },
    resetInput() {
      this.email = "";
      this.password = "";
    },
  },
};
</script>

<style></style>
