<template>
  <div class="container border rounded mt-5 text-center">
    <h1 class="display-4">{{name}}</h1>
    <div class="row">
      <div class="col-md-3 p-2" v-for="b in boards"
           @click="$router.push({name: 'board-boardId', params: {boardId: b.id}})">
        <div class="float-right pr-2 pt-2">
          <button class="btn btn-danger deleteBoard" @click.stop="deleteBoard(b)"><i class="far fa-trash-alt"></i>
          </button>
        </div>
        <div class="boardPane border border-secondary rounded py-5 bg-light">
          {{b.name}}
        </div>
      </div>
      <div class="col-md-3 p-2">
        <div class="boardPane border border-secondary rounded py-5 bg-light createBoard" @click="createBoard">
          <i class="fas fa-plus"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'teamBoard',
    props: {
      name: String,
      boards: Array,
      teamId: Number,
    },
    methods: {
      createBoard () {
        this.$swal({
          title: 'New board',
          inputPlaceholder: 'Board name',
          input: 'text',
          showCancelButton: true,
        }).then(boardName => {
          if (boardName.value) {
            this.$axios.post('/api/boards/', { name: boardName.value, team_id: this.teamId }).then(result => {
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
      deleteBoard (b) {
        this.$swal({
          type: 'warning',
          title: `Delete board : ${b.name}`,
          text: `Are you sure you want to delete board ${b.name} ?`,
          confirmButtonText: 'Yes, delete it!',
          showCancelButton: true,
        }).then(result => {
          if (result.value) {
            this.$axios.delete(`/api/boards/${b.id}`).then(result => {
              this.$parent.getAllTeams()
            })
          }
        })
      }
    }
  }
</script>

<style scoped>
  .boardPane {
    height: 130px;
  }

  .boardPane:hover {
    background-color: #7f828b !important;
    border-color: blue !important;
    cursor: pointer;
  }

  .createBoard {
    opacity: 0.4;
  }

  .createBoard:hover {
    opacity: 1;
  }

  .deleteBoard {
    font-size: 10pt;
    opacity: 0.5;
  }

  .deleteBoard:hover {
    opacity: 1;
  }
</style>
