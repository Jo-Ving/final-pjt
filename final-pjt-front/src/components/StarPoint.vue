<template>
  <div class="inner">
    <div class="star-rating">
      <div class="star" v-for="index in 5" :key="index" @click="check(index)">
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
    check(index) {
      this.score = index + 1;
    },
  },
};
</script>

<style scoped>
.star-rating {
  display: flex;
}

/* .star {
  position: relative;
  font-size: 2rem;
  color: #ddd;
}

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
