<template>
  <li>
    <div>
      <img src="" alt="" />
    </div>
    <div>
      <p>⭐⭐⭐⭐⭐</p>
      <div>
        <p>{{ review.user }}</p>
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
  methods: {
    createdAt() {
      const createdDate = this.review.created_at.split("T");
      const createdTime = createdDate[1].split(".");
      return `${createdDate[0]} ${createdTime[0]} `;
    },
  },
};
</script>

<style></style>
