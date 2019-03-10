<template>
  <div>
    <team-component :id="t.id" :name="t.name" v-for="t in teams" :key="t.id"/>
  </div>
</template>

<script>
  import teamComponent from '../components/teamComponent'

  export default {
    name: 'teams',
    components: { teamComponent },
    data () {
      return {
        teams: null,
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
      if (this.$store.state.auth.isLogged !== true) {
        this.$store.watch(() => this.$store.getters['auth/logged'], () => {
          this.getAllTeams()
        })
      } else {
        this.getAllTeams()
      }
    }
  }
</script>

<style scoped>

</style>
