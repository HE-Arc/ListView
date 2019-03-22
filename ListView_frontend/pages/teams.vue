<template>
  <div>
    <team-component :id="t.id" :name="t.name" :users="t.users_id" :boards="t.boards" v-for="t in teams" :key="t.id"/>
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
      onNuxtReady(()=>{
        if (this.$store.state.auth.isLogged === true) {
          this.getAllTeams()
        } else {
          this.$store.dispatch('auth/login')
        }
      })
    }
  }
</script>

<style scoped>

</style>
