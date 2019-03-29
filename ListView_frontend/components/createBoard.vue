<template>
  <div class="modal fade" id="createBoardModal" tabindex="-1" role="dialog" aria-labelledby="createBoardLabel"
       aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="createBoardLabel">Create board</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form novalidate class="container my-2">
            <div class="form-group">
              <label for="boardName">Board name</label>
              <input type="text" ref="boardName" class="form-control" id="boardName" v-model="boardName">
            </div>
            <div class="form-group">
              <label for="teamSelect">Choose the team</label>
              <select id="teamSelect" class="form-control" v-model="selectedTeam">
                <option disabled value="">Please select a team</option>
                <option :value="t.id" v-for="t in teams">{{t.name}}</option>
              </select>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-success" @click="sendBoard">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'createBoard',
    data () {
      return {
        teams: [],
        boardName: '',
        selectedTeam: '',
      }
    },
    mounted () {
      $('#createBoardModal').on('shown.bs.modal', () => {
        this.$refs.boardName.focus()
      })
      $('#createBoardModal').on('hidden.bs.modal', () => {
        this.closeModal()
      })
    },
    methods: {
      getTeamList () {
        this.$axios.get('/api/teams/').then(result => {
          this.teams = result.data
        })
      },
      closeModal () {
        this.$store.commit('utils/SETSHOWCREATEFORM', false)
      },
      sendBoard () {
        if (this.boardName !== '' && this.selectedTeam !== '') {
          this.$axios.post('/api/boards/', { name: this.boardName, team_id: this.selectedTeam }).then(result => {
            this.closeModal()
            this.$router.push({ name: 'board-boardId', params: { boardId: result.data.id } })
          }).catch(error => {
            this.$swal({
              type: 'error',
              title: 'Oops...',
              text: 'An error occured !'
            })
          })
        }
      }
    },
    computed: {
      showModal () {
        return this.$store.getters['utils/getShowCreateBoard']
      }
    },
    watch: {
      showModal (newValue, oldValue) {
        if (newValue === true) {
          this.getTeamList()
          $('#createBoardModal').modal('show')
        } else {
          $('#createBoardModal').modal('hide')
        }
      }
    }
  }
</script>

<style scoped>

</style>
