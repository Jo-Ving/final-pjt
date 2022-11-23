<template>
  <li>
    <div>
      <div class="applebox">
        <div v-for="index in 5" :key="index">
          <span v-if="index <= review.review_score">🍎</span>
          <span v-if="index > review.review_score">🍏</span>
        </div>
      </div>
      <h2>hello</h2>
      <div>
        <p>{{ review.user.username }}</p>
        <p>{{ createdAt() }}</p>
      </div>
      <p>
        {{ review.content }}
      </p>
    </div>
  </li>
</template>

<script>
export default {
  name: "ReviewComponent",
  props: {
    review: {},
  },
  components: {},
  methods: {
    createdAt() {
      const createdDate = this.review.created_at.split("T");
      const createdTime = createdDate[1].split(".");
      return `${createdDate[0]} ${createdTime[0]} `;
    },
  },
};
</script>

<style scoped>
.applebox {
  display: flex;
  flex-direction: row;
}
</style>
