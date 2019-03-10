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
    onNuxtReady(()=>{
      this.$store.dispatch('auth/authenticated')
    })
  }
}
</script>

<style>


</style>
