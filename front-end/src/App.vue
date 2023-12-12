<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    navbar: Navbar
  }
}

</script>

<style></style>
