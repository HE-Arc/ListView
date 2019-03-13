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
          <n-link :to="{ name: 'teams' }" class="nav-item nav-link" active-class="active" exact>
            Teams<span class="sr-only">(current)</span>
          </n-link>
          <a class="nav-item nav-link" href="#">Board (todo)</a>
        </ul>
        <div class="navbar-nav ml-auto btn-group">
          <button type="button" class="btn btn-secondary rounded" data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false">
            <i class="fas fa-plus"></i>
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <button class="dropdown-item" type="button" @click="showAlert">Create team</button>
            <button class="dropdown-item" type="button">TODO Create board</button>
          </div>
        </div>
        <ul class="navbar-nav ml-4">
          <li class="nav-item nav-link" @click.prevent="changeLog">{{textLog}}</li>
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
      async showAlert () {
        // Use sweetalert2
        const { value: teamName } = await this.$swal({
          title: 'New team',
          inputPlaceholder: 'Team name',
          input: 'text',
          showCancelButton: true,
        }, isConfirm => {
          if (isConfirm) {
            console.log("COUOCU")
            this.$axios.post('/api/teams/', { name: teamName, part_of: [] }).then(result => {
              this.$router.push({ name: 'team-id', params: { id: result.data.id } })
            })
          }
        })
        console.log("FUCK")
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
