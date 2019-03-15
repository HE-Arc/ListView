<template>
  <div class="container my-3 py-2 border border-secondary rounded">
    <h1>{{name}} <a @click="deleteTeam" class="text-danger deleteTeam float-right mt-3">Delete team</a></h1>
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
        const username = this.users.filter(u => u.id === id_user)[0].name
        this.$swal({
          type: 'warning',
          title: `Delete user : ${username}`,
          text: `Are you sure you want to delete team ${username} ?`,
          confirmButtonText: 'Yes, delete it!',
          showCancelButton: true,
        }).then(result => {
          if (result.value) {
            const usersFiltered = this.users.filter(u => u.id !== id_user)
            this.$axios.patch(`/api/teams/${this.id}/`, {
              id: this.id,
              name: this.name,
              users_id: usersFiltered,
              boards: this.boards
            }).then(result => {
              this.$parent.getAllTeams()
            }).catch(error => {
              this.$swal({
                type: 'error',
                title: 'Oops...',
                text: 'An error occured !'
              })
            })
          }
        })
      },
      deleteTeam () {
        this.$swal({
          type: 'warning',
          title: `Delete team : ${this.name}`,
          text: `Are you sure you want to delete team ${this.name} ?`,
          confirmButtonText: 'Yes, delete it!',
          showCancelButton: true,
        }).then(result => {
            if (result.value) {
              this.$axios.delete(`/api/teams/${this.id}`).then(() => {
                this.$swal({
                  type: 'success',
                  title: 'Success',
                  text: 'The team has been deleted !'
                })
                this.$parent.getAllTeams()
              }).catch(error => {
                this.$swal({
                  type: 'error',
                  title: 'Oops...',
                  text: 'An error occured !'
                })
              })
            }
          }
        )
      }
    }
  }
</script>

<style scoped>
  .deleteTeam {
    font-size: 10pt;
  }
</style>
