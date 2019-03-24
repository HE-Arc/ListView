<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <n-link class="navbar-brand" :to="{ name: 'index' }"><i class="fal fa-clipboard-list-check"></i> ListView</n-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <n-link :to="{ name: 'index' }" class="nav-item nav-link" active-class="active" exact>
            Home<span class="sr-only">(current)</span>
          </n-link>
          <n-link :to="{ name: 'dashboard' }" class="nav-item nav-link" active-class="active" v-if="isLogged" exact>
            Dashboard<span class="sr-only">(current)</span>
          </n-link>
          <n-link :to="{ name: 'teams' }" class="nav-item nav-link" active-class="active" v-if="isLogged" exact>
            Teams<span class="sr-only">(current)</span>
          </n-link>
        </ul>
        <div class="navbar-nav ml-auto btn-group">
          <button type="button" class="btn btn-secondary rounded" data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false" v-show="isLogged">
            <i class="fas fa-plus"></i>
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <button class="dropdown-item" type="button" @click="createTeam">Create team</button>
            <button class="dropdown-item" type="button" @click="$modal.show('create-board')">Create board
            </button>
          </div>
        </div>
        <ul class="navbar-nav ml-4">
          <li class="nav-item nav-link" @click="changeLog">{{textLog}}</li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: 'navbar',
    methods: {
      changeLog () {
        if (this.isLogged) {
          this.$store.dispatch('auth/logout')
          this.$router.push({ name: 'index' })
        } else {
          this.$store.dispatch('auth/login')
        }
      },
      createTeam () {
        // Use sweetalert2
        this.$swal({
          title: 'New team',
          inputPlaceholder: 'Team name',
          input: 'text',
          showCancelButton: true,
        }).then(teamName => {
          if (teamName) {
            this.$axios.post('/api/teams/', { name: teamName.value, users_id: [] }).then(result => {
              this.$router.push({ name: 'teams' })
            })
          }
        })
      }
    },
    computed: {
      isLogged () {
        return this.$store.state.auth.isLogged
      },
      textLog () {
        if (this.isLogged) {
          return 'logout'
        }
        return 'login'
      }
    }
  }
</script>

<style scoped>

</style>
