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
      </div>
      <button @click="onSignUpButtonClick">Sign up</button>
    </form>
    <p>
      have an account?
      <button>Log in here</button>
    </p>
  </div>
</template>

<script>
import InputComponent from "../../components/InputComponent.vue";
import { checkEmailValidate } from "../../utils/validators";
import { EMAIL_VALIDATION_FALSE } from "../../assets/constants";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      passwordConfirm: "",
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
    getPasswordConfirmValue(passwordConfirm) {
      this.passwordConfirm = passwordConfirm;
    },
    onSignUpButtonClick(e) {
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
