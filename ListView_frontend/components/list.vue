<template>
  <div class="border border-secondary rounded my-2 px-1 bg-info">
    <h3 class="ml-3 my-2">{{name}}<a @click="deleteList" class=" pl-3 pr-1 text-danger deleteList float-right">Delete list</a></h3>
    <task :taskO="t" v-for="t in tasks" :key="t.id"/>
    <div class="bg-white border border-secondary rounded my-1">
      <div class="bg-secondary createTask py-1" @click="createTask">
        <i class="fas fa-plus"></i>
      </div>
    </div>
  </div>
</template>

<script>
  import Task from '~/components/task'

  export default {
    name: 'list',
    props: {
      id: Number,
      name: String,
      tasks: Array,
    },
    components: {
      Task
    },
    methods: {
      createTask () {
        this.$store.commit('utils/SETLISTTOADDTASK', this.id)
        this.$store.commit('utils/SETSHOWMANAGETASK', true)
      },
      deleteList () {
        this.$swal({
          type: 'warning',
          title: `Delete list : ${this.name}`,
          text: `Are you sure you want to delete list ${this.name} ?`,
          confirmButtonText: 'Yes, delete it!',
          showCancelButton: true,
        }).then(result => {
          if (result.value) {
            this.$axios.delete(`/api/list/${this.id}/`).then(result => {
              //TODO refresh list
            })
          }
        })
      },
    }
  }
</script>

<style scoped>
  .createTask {
    opacity: 0.4;
  }

  .createTask:hover {
    opacity: 1;
    cursor: pointer;
  }
  .deleteList {
    font-size: 10pt;
    cursor: pointer;
  }
</style>
