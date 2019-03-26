<template>
  <div>
    <navbar/>
    <nuxt/>
      <create-board/>
  </div>
</template>

<script>
  import navbar from '../components/navbar'
  import CreateBoard from '../components/createBoard'

  export default {
    components: {
      CreateBoard,
      navbar,
    },
    mounted () {
      onNuxtReady(() => {
        this.$store.dispatch('auth/authenticated')
      })
    }
  }
</script>

<style>


</style>
