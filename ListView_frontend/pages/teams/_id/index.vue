<template>
  <div>
    {{team}}
  </div>
</template>

<script>
  export default {
    name: 'index.vue',
    data () {
      return {
        team: ''
      }
    },
    methods: {
      downloadTeam () {
        this.$axios.get('/api/teams/' + this.$route.params.id).then(response => {
          console.log(response)
          this.team = response.data
        })
      }
    },
    mounted () {
      this.downloadTeam()
    },
  }
</script>

<style scoped>

</style>
