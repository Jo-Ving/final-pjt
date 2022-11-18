<template>
  <div>
    <label for="labelName">{{ labelName }}</label>
    <input :value="userInput" @input="titleUpdate" type="text" />
  </div>
</template>

<script>
export default {
  name: "InputComponent",
  props: {
    labelName: String,
    userInput: String,
  },
  data() {
    return {};
  },
  methods: {
    titleUpdate(e) {
      const { value } = e.target;
      this.$emit("inputFromChild", value);
    },
  },
};
</script>

<style></style>
