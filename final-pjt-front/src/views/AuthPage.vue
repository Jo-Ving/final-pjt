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
      </div>
      <div>
        <InputComponent
          :userInput="password"
          :labelName="`password*`"
          @inputFromChild="getPasswordValue"
        />
      </div>
      <button @click="onLotinButtonClick">Login</button>
    </form>
    <p>
      Don't have an account?
      <button>Sign up here</button>
    </p>
  </div>
</template>

<script>
import InputComponent from "../components/InputComponent.vue";

export default {
  name: "MainPage",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  components: {
    InputComponent,
  },
  methods: {
    getEmailValue(email) {
      console.log(email, "🍕");
    },
    getPasswordValue(password) {
      console.log(password, "🥖");
    },
    onLotinButtonClick(e) {
      console.log(e.target);
    },
  },
};
</script>

<style></style>
