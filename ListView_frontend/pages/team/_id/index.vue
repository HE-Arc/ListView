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
      if (this.$store.state.auth.isLogged !== true) {
        this.$store.watch(() => this.$store.getters['auth/logged'], () => {
          this.downloadTeam()
        })
      } else {
        this.downloadTeam()
      }
    },
  }
</script>

<style scoped>

</style>
