<template>
  <div class="container mt-3 py-2 border border-secondary rounded">
    <h1>{{name}} <a @click="deleteTeam" class="text-danger deleteTeam float-right mt-3">Delete team</a></h1>
    <div class="table-responsive">
      <table class="table bg-light border rounded">
        <tbody>
        <tr v-for="u in users">
          <td>{{u.email}}</td>
          <td>
            <button v-if="users.length > 1" class="btn btn-danger" @click="deleteMember(u.id)"><i class="fal fa-trash-alt"></i></button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <hr>
    <small>Add user to the team</small>
    <div class="mb-1"></div>
    <div>
      <input type="text" class="form-control" placeholder="Username" v-model="textSearch">
    </div>
    <div class="table-responsive mt-3">
      <table class="table bg-light border rounded">
        <tbody>
        <tr v-for="u in userFound">
          <td>{{u.email}}</td>
          <td>
            <button class="btn btn-primary" @click="addMember(u.id)"><i class="fal fa-user-plus"></i></button>
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
    data () {
      return {
        textSearch: '',
        userFound: [],
      }
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
      },
      addMember (id_user) {
        const usersAll = this.users
        usersAll.push(this.userFound.filter(u => u.id === id_user)[0])
        this.$axios.patch(`/api/teams/${this.id}/`, {
          id: this.id,
          name: this.name,
          users_id: usersAll,
          boards: this.boards
        }).then(result => {
          this.$parent.getAllTeams()
          this.refreshUserFound()
        }).catch(error => {
          this.$swal({
            type: 'error',
            title: 'Oops...',
            text: 'An error occured !'
          })
        })
      },
      refreshUserFound () {
        const ids = this.users.map(u => u.id)
        this.userFound = this.userFound.filter(u => ids.indexOf(u.id) < 0)
      }
    },
    watch: {
      textSearch: function (val) {
        this.$axios.get(`/api/user?name=${val}`).then(result => {
          this.userFound = result.data
          this.refreshUserFound()
        })
      }
    }
  }
</script>

<style scoped>
  .deleteTeam {
    font-size: 10pt;
  }
</style>
