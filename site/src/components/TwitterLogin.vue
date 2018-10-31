<template>
  <div class="hello">
    <button class="twitter-login">Sign in</button>
  </div>
</template>

<script>
export default {
  name: 'TwitterLogin'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: blueviolet;
}
.twitter-login {
  background-image: url('./../assets/twitter.svg');
  background-repeat: no-repeat;
  background-color: #1da1f2;
  border: 0;
  padding: 2em;
  width: 20em;
  color: white;
  cursor: pointer;
  border-radius: 1em;
}
</style>
