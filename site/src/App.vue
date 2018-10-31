<template>
  <div id="app">
    <TwitterLogin/>
  </div>
</template>

<script>
import TwitterLogin from './components/TwitterLogin.vue'

export default {
  name: 'app',
  components: {
    TwitterLogin
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
