<template>
  <div>
    <team-board v-for="t in teams" :name="t.name" :boards="t.boards"/>
  </div>
</template>

<script>
  import TeamBoard from '../components/teamBoard'

  export default {
    name: 'dashboard',
    components: {
      TeamBoard
    },
    data () {
      return {
        teams: [],
      }
    },
    methods: {
      getAllTeams () {
        this.$axios.get('/api/teams/').then(response => {
          this.teams = response.data
        })
      }
    },
    mounted () {
      this.$nextTick(() => {
        if (this.$store.state.auth.isLogged === true) {
          this.getAllTeams()
        } else {
          this.$store.watch(() => this.$store.getters['auth/logged'], () => {
            this.getAllTeams() //Wait, while checking if session is logged
          })
          setTimeout(() => { //If we aren't logged after 1s redirect to login
            if (this.$store.state.auth.isLogged === false) {
              this.$store.dispatch('auth/login')
            }
          }, 1000)
        }
      })
    }
  }
</script>

<style scoped>

</style>
