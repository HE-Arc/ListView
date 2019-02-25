<template>
  <div>
    <navbar />
    <nuxt />
  </div>
</template>

<script>
import navbar from '../components/navbar'

export default {
  components: {
    navbar
  },
  mounted () {
    this.$store.dispatch('http/loadToken')
  }
}
</script>

<style>
  html {
    font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: 16px;
  }

</style>
