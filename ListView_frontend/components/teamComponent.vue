<template>
  <div class="container my-3 py-2 border border-secondary rounded">
    <h1>{{name}}</h1>
    <div class="table-responsive">
      <table class="table bg-light border rounded">
        <tbody>
        <tr v-for="u in users">
          <td>{{u.username}}</td>
          <td>{{u.email}}</td>
          <td>{{u.name}}</td>
          <td>
            <button class="btn btn-danger" @click="deleteMember(u.id)"><i class="fal fa-trash-alt"></i></button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'teamComponent',
    props: {
      id: Number,
      name: String,
      users: Array,
      boards: Array,
    },
    methods: {
      deleteMember (id_user) {
        const usersFiltered = this.users.filter(u => u.id !== id_user)
        this.$axios.patch(`/api/teams/${this.id}/`, {
          id: this.id,
          name: this.name,
          users_id: usersFiltered,
          boards: this.boards
        }).then(result => {
          this.$parent.getAllTeams()
        }).catch(error=>{
          this.$swal({
              type: 'error',
              title: 'Oops...',
              text: 'An error occured !'
            })
        })
      }
    }
  }
</script>

<style scoped>
</style>
