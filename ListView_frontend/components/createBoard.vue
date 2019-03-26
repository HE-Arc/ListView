<template>
  <div>
    <modal :adaptive=true name="create-board" transition="pop-out" @before-open="getTeamList">
      <form novalidate class="container my-2">
        <div class="form-group">
          <label for="boardName">Board name</label>
          <input type="text" class="form-control" id="boardName" v-model="boardName">
        </div>
        <div class="form-group">
          <label for="teamSelect">Choose the team</label>
          <select id="teamSelect" class="form-control" v-model="selectedTeam">
            <option disabled value="">Please select a team</option>
            <option :value="t.id" v-for="t in teams">{{t.name}}</option>
          </select>
        </div>
        <div class="form-row mt-5">
          <button class="mx-3 col btn btn-success" @click="sendBoard">Create</button>
          <button class="mx-3 col btn btn-danger" @click="closeModal">Cancel</button>
        </div>
      </form>
    </modal>
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
    methods: {
      getTeamList () {
        this.$axios.get('/api/teams/').then(result => {
          this.teams = result.data
        })
      },
      closeModal () {
        this.$modal.hide('create-board')
      },
      sendBoard () {
        if (this.boardName !== '' && this.selectedTeam !== '') {
          this.$axios.post('/api/boards/', { name: this.boardName, team_id: this.selectedTeam }).then(result => {
            this.closeModal()
            //TODO redirect to board page
          }).catch(error => {
            this.$swal({
              type: 'error',
              title: 'Oops...',
              text: 'An error occured !'
            })
          })
        }
      }
    }
  }
</script>

<style scoped>

</style>
