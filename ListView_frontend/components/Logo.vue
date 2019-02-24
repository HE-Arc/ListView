<template>
  <div class="VueToNuxtLogo">
    <button @click="log">
      Login
    </button>
    <button @click="get">
      get
    </button>
    {{ message }}
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: 'steven',
      password: '123',
      message: ''
    }
  },
  methods: {
    log () {
      const username = this.username
      const password = this.password
      this.$store.dispatch('http/obtainToken', { username, password })
    },
    get () {
      this.$axios.get('api/teams/').then((response) => {
        this.message = response.data
      })
    }
  }
}
</script>

<style>

</style>
