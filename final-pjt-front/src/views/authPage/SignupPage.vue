<template>
  <div>
    <div class="login-box">
      <h1>Signup</h1>
      <form action="submit" @click.prevent>
        <div class="user-box">
          <InputComponent
            :userInput="email"
            :labelName="`email*`"
            :type="`text`"
            @inputFromChild="getEmailValue"
          />
          <div class="message-box">
            <p class="validate-message">{{ emailValidateMessage }}</p>
          </div>
        </div>
        <div class="user-box">
          <InputComponent
            :userInput="password"
            :labelName="`password*`"
            :type="`password`"
            @inputFromChild="getPasswordValue"
          />
        </div>
        <div class="user-box">
          <InputComponent
            :userInput="passwordConfirm"
            :labelName="`password confirm*`"
            :type="`password`"
            @inputFromChild="getPasswordConfirmValue"
          />
          <div class="message-box">
            <p class="validate-message">{{ passwordEqualMessage }}</p>
          </div>
        </div>
        <ButtonComponent
          :disabled="isEmailValidate === false || isPasswordValidate === false"
          @onButtonClick="onSignUpButtonClick"
          :buttonName="`Sign up`"
        />
      </form>
      <p>
        have an account?
        <span class="changepage-link" @click="toLoginPage">Log in here</span>
      </p>
    </div>
    <!-- <div class="pickmovie"> -->
    <!-- <PickMoviesComponent /> -->
    <!-- </div> -->
  </div>
</template>

<script>
import InputComponent from "../../components/InputComponent.vue";
// import PickMoviesComponent from "../../components/PickMoviesComponent.vue";
import ButtonComponent from "../../components/ButtonComponent.vue";
import { checkEmailValidate, checkPasswordEqal } from "../../utils/validators";
import {
  EMAIL_VALIDATION_FALSE,
  PASSWORD_EQUAL_FALSE,
} from "../../assets/constants";
import { toNextRouter } from "../../router/routingLogic";
import { fetchSignup } from "../../api/authAPI";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      passwordConfirm: "",
      mockPassword: "",
      mockPasswordConfirm: "",
      emailValidateMessage: "",
      passwordEqualMessage: "",
      submitButtonState: false,
      isEmailValidate: false,
      isPasswordValidate: false,
    };
  },
  components: {
    InputComponent,
    ButtonComponent,
  },
  methods: {
    getEmailValue(email) {
      this.email = email;
      if (checkEmailValidate(this.email)) {
        this.isEmailValidate = true;
        this.emailValidateMessage = "";
        return;
      }
      this.emailValidateMessage = EMAIL_VALIDATION_FALSE;
      this.isEmailValidate = false;
    },
    getPasswordValue(password) {
      this.password = password;
      this.mockPassword = "*".repeat(password.length);
      console.log(this.mockPassword);
      if (checkPasswordEqal(this.password, this.passwordConfirm)) {
        this.passwordEqualMessage = "";
        this.isPasswordValidate = true;
        return;
      }
      this.passwordEqualMessage = PASSWORD_EQUAL_FALSE;
      this.isPasswordValidate = false;
    },
    getPasswordConfirmValue(passwordConfirm) {
      this.passwordConfirm = passwordConfirm;
      if (checkPasswordEqal(this.password, this.passwordConfirm)) {
        this.passwordEqualMessage = "";
        this.isPasswordValidate = true;
        return;
      }
      this.passwordEqualMessage = PASSWORD_EQUAL_FALSE;
      this.isPasswordValidate = false;
    },
    onSignUpButtonClick() {
      fetchSignup({
        username: this.email,
        password: this.password,
        passwordConfirm: this.passwordConfirm,
      });
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
  },
};
</script>

<style scoped>
@import "../../assets/style.css";

.changepage-link {
  cursor: pointer;
  color: var(--gray6);
}
.changepage-link:hover {
  color: #7ee5eb;
}

html {
  height: 100%;
}
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: linear-gradient(#141e30, #243b55);
}

.login-box {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
  border-radius: 10px;
}

.login-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}

.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 10px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}
.login-box .user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: 0.5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #7ee5eb;
  font-size: 12px;
}

/* my job  */
.changepage-link {
  cursor: pointer;
  color: var(--gray6);
}
.changepage-link:hover {
  color: #7ee5eb;
}
.message-box {
}
.validate-message {
  text-align: right;
  font-size: 10px;
  margin: 0;
  color: red;
}
button {
  border: none;
  outline: none;
  background: transparent;
}
.pickmovie {
  margin-top: 90vh;

  /* position: absolute; */
  width: 100vw;
}
</style>
