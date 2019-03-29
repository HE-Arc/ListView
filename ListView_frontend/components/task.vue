<template>
  <div class="border border-secondary rounded my-1 py-1 bg-white task">
    <div class="row" data-toggle="tooltip" data-placement="bottom" :title="taskO.description">
      <div class="col-auto ml-2 pt-1">
        <input type="checkbox" v-model="isChecked">
      </div>
      <div class="col pr-5 pr-sm-1 pl-0 pt-1" :style="[isChecked ? {opacity: 0.5} : {opacity : 1}]" @click="modifyTask">
        {{taskO.name}}
      </div>
      <div class="col-auto mr-2">
        <button class="btn btn-danger" @click.stop="deleteTask"><i class="fal fa-trash-alt"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'task',
    props: {
      taskO: Object
    },
    data () {
      return {
        isChecked: false
      }
    },
    mounted () {
      this.isChecked = this.taskO.checked
    },
    methods: {
      modifyTask () {
        this.$store.commit('utils/SETLISTTOADDTASK', this.id)
        this.$store.commit('utils/SETTASKTOMANAGE', this.taskO)
        this.$store.commit('utils/SETSHOWMANAGETASK', true)
      },
      deleteTask () {
        this.$swal({
          type: 'warning',
          title: `Delete task : ${this.name}`,
          text: `Are you sure you want to delete task ${this.name} ?`,
          confirmButtonText: 'Yes, delete it!',
          showCancelButton: true,
        }).then(result => {
          if (result.value) {
            this.$axios.delete(`api/task/${this.taskO.id}`).then(result => {
              this.$parent.$parent.loadLists()
            })
          }
        })
      }
    },
    watch: {
      isChecked: function (value) {
        let t = this.taskO
        t.checked = value
        this.$axios.patch(`/api/task/${t.id}/`, t)
      }
    }
  }
</script>

<style>
.task:hover{
  background-color: #7F828B !important;
  border-color: blue !important;
  cursor: pointer;
}
</style>
