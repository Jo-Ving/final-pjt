<template>
  <div class="inner">
    <div class="star-rating">
      <div
        class="star"
        v-for="index in 5"
        :key="index"
        @click="starCheck(index)"
      >
        <span v-if="index < score">🍎</span>
        <span v-if="index >= score">🍏</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StarPoint",
  data() {
    return {
      score: 0,
    };
  },
  methods: {
    starCheck(index) {
      this.score = index + 1;
      this.$emit("starCheck", this.score);
    },
  },
};
</script>

<style scoped>
.star-rating {
  display: flex;
}

.star {
  cursor: pointer;
}
/*
.star input {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  opacity: 0;
  cursor: pointer;
}

.star span {
  width: 0;
  position: absolute;
  left: 0;
  color: red;
  overflow: hidden;
  pointer-events: none;
} */
</style>
