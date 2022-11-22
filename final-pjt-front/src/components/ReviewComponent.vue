<template>
  <li>
    <div>
      <img src="" alt="" />
    </div>
    <div>
      <p>⭐⭐⭐⭐⭐</p>
      <div>
        <p>{{ review.user }}</p>
        <p>{{ review.created_at }}</p>
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
};
</script>

<style></style>
