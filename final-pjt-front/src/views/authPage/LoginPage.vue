<template>
  <div>
    <h1>Login</h1>
    <form action="submit" @click.prevent>
      <InputComponent
        :userInput="email"
        :labelName="`email*`"
        @inputFromChild="getEmailValue"
      />
      <p>{{ emailValidateMessage }}</p>
      <InputComponent
        :userInput="password"
        :labelName="`password*`"
        @inputFromChild="getPasswordValue"
      />
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
// import axios from "axios";
import { fetchLogin } from "../../api/authAPI";

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
    // getUserInfo() {
    //   axios({
    //     method: "post",
    //     url: `http://127.0.0.1:8000/accounts/token/`,
    //     data: {
    //       username: this.email,
    //       password: this.password,
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

<style scoped>
@import "../../assets/style.css";

* {
  box-sizing: border-box;
}

/* basic stylings ------------------------------------------ */
body {
  background: url(https://scotch.io/wp-content/uploads/2014/07/61.jpg);
}
.container {
  font-family: "Roboto";
  width: 600px;
  margin: 30px auto 0;
  display: block;
  background-color: var(--gray0);
  padding: 10px 50px 50px;
}
h2 {
  text-align: center;
  margin-bottom: 50px;
}
h2 small {
  font-weight: normal;
  color: #888;
  display: block;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.footer {
  text-align: center;
}
.footer a {
  color: #53b2c8;
}

/* form starting stylings ------------------------------- */
.group {
  position: relative;
  margin-bottom: 45px;
}
input {
  font-size: 18px;
  padding: 10px 10px 10px 5px;
  display: block;
  margin: auto;
  width: 300px;
  border: none;
  border-bottom: 1px solid #757575;
}
input:focus {
  outline: none;
}

/* LABEL ======================================= */
label {
  color: #999;
  font-size: 18px;
  font-weight: normal;
  position: absolute;
  pointer-events: none;
  left: 5px;
  top: 10px;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}

/* active state */
input:focus ~ label,
input:valid ~ label {
  top: -20px;
  font-size: 14px;
  color: #5264ae;
}

/* BOTTOM BARS ================================= */
.bar {
  position: relative;
  display: block;
  width: 300px;
}
.bar:before,
.bar:after {
  content: "";
  height: 2px;
  width: 0;
  bottom: 1px;
  position: absolute;
  background: #5264ae;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.bar:before {
  left: 50%;
}
.bar:after {
  right: 50%;
}

/* active state */
input:focus ~ .bar:before,
input:focus ~ .bar:after {
  width: 50%;
}

/* HIGHLIGHTER ================================== */
.highlight {
  position: absolute;
  height: 60%;
  width: 100px;
  top: 25%;
  left: 0;
  pointer-events: none;
  opacity: 0.5;
}

/* active state */
input:focus ~ .highlight {
  -webkit-animation: inputHighlighter 0.3s ease;
  -moz-animation: inputHighlighter 0.3s ease;
  animation: inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@-moz-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
</style>
