<template>
  <div class="modal fade show" id="manageTaskModal" tabindex="-1" role="dialog" aria-labelledby="manageTaskLabel"
       aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="manageTaskLabel">{{actionText}} task</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form novalidate class="container my-2">
            <div class="form-group">
              <label for="taskName">Task name</label>
              <input type="text" class="form-control" ref="taskName" id="taskName" v-model="taskName" @keydown.enter="createTask">
            </div>
            <div class="form-group">
              <label for="taskDescription">Task description</label>
              <textarea class="form-control" id="taskDescription" rows="3" v-model="taskDescription"></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-success" @click="createTask">{{actionText}}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'manageTask',
    data () {
      return {
        taskName: '',
        taskDescription: '',
        listId: '',
        taskId: '',
        checked: false,
      }
    },
    mounted () {
      $('#manageTaskModal').on('show.bs.modal', () => {
        this.listId = this.$store.getters['utils/getListToAddTask']
        let task = this.$store.getters['utils/getTaskToManage']
        if (task !== undefined && task !== null) {
          this.taskName = task.name
          this.taskDescription = task.description
          this.taskId = task.id
          this.checked = task.checked
        }
      })

      //Put focus on input when form is loaded
      $('#manageTaskModal').on('shown.bs.modal', () => {
        this.$refs.taskName.focus()
      })

      $('#manageTaskModal').on('hidden.bs.modal', () => {
        this.cleanOnClose()
        this.$store.commit('utils/SETSHOULDREFRESHBOARD', true)
      })
    },
    methods: {
      createTask () {
        const params = {
          name: this.taskName,
          checked: this.checked,
          list_id: this.listId,
          description: this.taskDescription,
        }
        if (this.taskId === '') {
          this.$axios.post('/api/task/', params).then(result => {
            this.refreshClose()
          })
        } else {
          this.$axios.patch(`/api/task/${this.taskId}/`, params).then(result => {
            this.refreshClose()
          })
        }
      },
      refreshClose () {
        //TODO refresh list
        $('#manageTaskModal').modal('hide')
      },
      cleanOnClose () {
        this.$store.commit('utils/SETSHOWMANAGETASK', false)
        this.$store.commit('utils/SETLISTTOADDTASK', null)
        this.$store.commit('utils/SETTASKTOMANAGE', null)
        this.taskName = ''
        this.taskDescription = ''
        this.listId = ''
        this.taskId = ''
        this.checked = false
      }
    },
    computed: {
      showModalTask () {
        return this.$store.getters['utils/getShowManageTask']
      },
      actionText () {
        if (this.taskId === '') {
          return 'Create'
        }
        return 'Modify'
      }
    },
    watch: {
      showModalTask (newValue, oldValue) {
        if (newValue === true) {
          $('#manageTaskModal').modal('show')
        } else {
          $('#manageTaskModal').modal('hide')
        }
      }
    },
  }
</script>

<style scoped>
#taskDescription {
  resize: None;
}
</style>
