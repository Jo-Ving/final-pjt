<template>
  <li>
    <div class="userInfoAndStarContainer">
      <p>{{ review.user.username }}</p>
      <div class="applebox">
        <div v-for="index in 5" :key="index">
          <span v-if="index <= review.review_score">🍎</span>
          <span v-if="index > review.review_score">🍏</span>
        </div>
      </div>
    </div>
    <div class="talk-bubble tri-right left-top">
      <div class="talktext">
        <p>
          {{ review.content }}
        </p>
        <p class="timeStamp">
          {{ createdAt() }}
        </p>
      </div>
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
li {
  margin-top: 30px;
  margin-bottom: 10px;
  margin-right: 30px;
}
p {
  margin: 0;
}
.userInfoAndStarContainer {
  display: flex;
  margin-left: 40px;
}
.timeStamp {
  margin-top: 0.5rem;
}
.container {
  margin-top: 1rem;

  padding-top: 0.5rem;
  border: 1px solid pink;
}
.applebox {
  display: flex;
  flex-direction: row;
}

body {
  background-color: lightblue;
  font-family: "Ubuntu-Italic", "Lucida Sans", helvetica, sans;
}

/* container */
.container {
  padding: 5% 5%;
}
.talk-bubble {
  color: black;
  margin-left: 40px;
  display: inline-block;
  position: relative;
  width: 200px;
  height: auto;
  background-color: lightyellow;
}
.border {
  border: 8px solid #666;
}
.round {
  border-radius: 30px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
}
/* General CSS Setup */
body {
  background-color: lightblue;
  font-family: "Ubuntu-Italic", "Lucida Sans", helvetica, sans;
}

/* container */
.container {
  padding: 5% 5%;
}

/* CSS talk bubble */
.talk-bubble {
  margin: 40px;
  margin-top: 0;

  display: inline-block;
  position: relative;
  width: 40vw;
  height: auto;
  background-color: lightyellow;
}
.border {
  border: 8px solid #666;
}
.round {
  border-radius: 30px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
}

/* Right triangle placed top left flush. */
.tri-right.border.left-top:before {
  content: " ";
  position: absolute;
  width: 0;
  height: 0;
  left: -40px;
  right: auto;
  top: -8px;
  bottom: auto;
  border: 32px solid;
  border-color: #666 transparent transparent transparent;
}
.tri-right.left-top:after {
  content: " ";
  position: absolute;
  width: 0;
  height: 0;
  left: -20px;
  right: auto;
  top: 0px;
  bottom: auto;
  border: 22px solid;
  border-color: lightyellow transparent transparent transparent;
}

.talktext {
  padding: 10px;
}
</style>
