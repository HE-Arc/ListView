<template>
  <div>
    <section class="container">
    <div>
      <h1 class="title">ListView_frontend</h1>
      <h2 class="subtitle">Frontend of ListView project</h2>
      <div class="links">
        <a href="https://nuxtjs.org/" target="_blank" class="button--green">Documentation</a>
        <a href="https://github.com/nuxt/nuxt.js" target="_blank" class="button--grey">GitHub</a>
      </div>
    </div>
  </section>
    <div>
      Temporaire, juste pour tester<br />
      <button @click="request">Requête protegé</button>
      {{message}}
    </div>
  </div>

</template>

<script>

export default {
  data() {
    return {
      message: ''
    }
  },
  methods: {
    request() {
      this.$store.dispatch('http/isTokenValid').then(response=>{
        if(response === true) {
          this.$axios.$get('api/teams/').then(response=> {
            this.message = response
          })
        } else {
          this.$router.push({'name': 'login'})
        }
      })
    }
  }
}
</script>

<style>

</style>
