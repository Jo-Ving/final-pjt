<template>
  <div class="login-box">
    <h1>Login</h1>
    <form action="submit" @click.prevent>
      <InputComponent
        :userInput="email"
        :labelName="`email*`"
        :type="`text`"
        @inputFromChild="getEmailValue"
      />
      <div class="message-box">
        <p class="validate-message">{{ emailValidateMessage }}</p>
      </div>
      <InputComponent
        :userInput="password"
        :labelName="`password*`"
        :type="`password`"
        @inputFromChild="getPasswordValue"
      />
      <ButtonComponent
        :disabled="isValidate === false"
        @onButtonClick="onLoginButtonClick"
        :buttonName="`Login`"
      />
    </form>
    <p>
      Don't have an account?
      <span class="changepage-link" @click="toSignup">Sign up here</span>
    </p>
  </div>
</template>

<script>
import InputComponent from "../../components/InputComponent.vue";
import ButtonComponent from "../../components/ButtonComponent.vue";
import { checkEmailValidate } from "../../utils/validators";
import { EMAIL_VALIDATION_FALSE } from "../../assets/constants";
import { toNextRouter } from "../../router/routingLogic";
import { fetchLogin } from "../../api/authAPI";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      emailValidateMessage: "",
      isValidate: false,
    };
  },
  components: {
    InputComponent,
    ButtonComponent,
  },
  methods: {
    getEmailValue(email) {
      this.email = email;

      if (checkEmailValidate(email)) {
        this.isValidate = true;
        this.emailValidateMessage = "";
        this.email = email;

        return;
      }
      this.emailValidateMessage = EMAIL_VALIDATION_FALSE;
      this.isValidate = false;
      this.email = email;
    },
    getPasswordValue(password) {
      this.password = password;
    },
    onLoginButtonClick() {
      fetchLogin({
        username: this.email,
        password: this.password,
      });
      this.resetInput();
    },
    resetInput() {
      this.email = "";
      this.password = "";
    },
    toSignup() {
      toNextRouter(this.$router, "signup");
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
/* 
.login-box form button {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #7ee5eb;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: 0.5s;
  margin-top: 40px;
  letter-spacing: 4px;
}

.login-box button:hover {
  background: #7ee5eb;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #7ee5eb, 0 0 25px #7ee5eb, 0 0 50px #7ee5eb,
    0 0 100px #7ee5eb;
}

.login-box button span {
  position: absolute;
  display: block;
}

.login-box button span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #7ee5eb);
  animation: btn-anim1 1s linear infinite;
}

@keyframes btn-anim1 {
  0% {
    left: -100%;
  }
  50%,
  100% {
    left: 100%;
  }
}

.login-box button span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #7ee5eb);
  animation: btn-anim2 1s linear infinite;
  animation-delay: 0.25s;
}

@keyframes btn-anim2 {
  0% {
    top: -100%;
  }
  50%,
  100% {
    top: 100%;
  }
}

.login-box button span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #7ee5eb);
  animation: btn-anim3 1s linear infinite;
  animation-delay: 0.5s;
}

@keyframes btn-anim3 {
  0% {
    right: -100%;
  }
  50%,
  100% {
    right: 100%;
  }
}

.login-box button span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #7ee5eb);
  animation: btn-anim4 1s linear infinite;
  animation-delay: 0.75s;
}

@keyframes btn-anim4 {
  0% {
    bottom: -100%;
  }
  50%,
  100% {
    bottom: 100%;
  }
} */

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
</style>
