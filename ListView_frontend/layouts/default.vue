<template>
  <div>
    <navbar/>
    <nuxt/>
    <create-board/>
    <manage-task />
  </div>
</template>

<script>
  import navbar from '../components/navbar'
  import CreateBoard from '../components/createBoard'
  import ManageTask from '../components/manageTask'

  export default {
    components: {
      CreateBoard,
      navbar,
      ManageTask,
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
