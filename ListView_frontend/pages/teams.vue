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
      this.$nextTick(() => {
        if (this.$store.state.auth.isLogged === true) {
          this.getAllTeams()
        } else {
          this.$store.watch(()=> this.$store.getters['auth/logged'], () => {
            this.getAllTeams() //Wait, while checking if session is logged
          })
          setTimeout(()=>{ //If we aren't logged after 1s redirect to login
            if(this.$store.state.auth.isLogged === false) {
              this.$store.dispatch('auth/login')
            }
          }, 1000)
        }
      })
    },
    computed: {
      shouldRefresh() {
        return this.$store.getters['utils/getShouldRefreshTeam']
      }
    },
    watch: {
      shouldRefresh(newValue, oldValue) {
        if(newValue===true) {
          this.getAllTeams()
          this.$store.commit('utils/SETSHOULDREFRESH', false)
        }
      }
    },
  }
</script>

<style scoped>

</style>
