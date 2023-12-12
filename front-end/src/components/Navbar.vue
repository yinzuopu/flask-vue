<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" style="margin-bottom: 20px">
    <div class="container">
      <router-link to="/" class="navbar-brand">
        <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
        HULKBLOG
      </router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mt-2 mt-lg-0">
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Explore</a>
          </li>
          <li class="nav-item">
            <a v-on:click="handlerLogout" class="nav-link" href="#">Logout</a>
          </li>
        </ul>

        <form class="form-inline navbar-left me-auto">
          <input class="form-control mr-sm-2" type="search" placeholder="Search">
          <!-- 暂时先禁止提交，后续实现搜索再改回submit -->
          <button class="btn btn-outline-success my-2 my-sm-0" type="button">Search</button>
        </form>

        <ul class="nav navbar navbar-right">
          <li class="nav-item">
            <router-link to="/profile" class="nav-link">Profile</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import store from '../store.js'
export default {
  name: 'Navbar',  //this is the name of the component
  data () {
    return {
      sharedState: store.state
    }
  },
  methods: {
    handlerLogout (e) {
      store.logoutAction()
      this.$router.push('/login')
    }
  }
}
</script>
