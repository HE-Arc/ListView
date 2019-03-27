<template>
  <div class="border border-secondary rounded my-2 px-1 bg-info">
    <h3>{{name}}</h3>
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
        this.$swal({
          title: 'New task',
          inputPlaceholder: 'Task name',
          input: 'text',
          showCancelButton: true,
        }).then(taskName => {
          if (taskName.value) {
            this.$axios.post('/api/task/', {
              name: taskName.value,
              checked: false,
              list_id: this.id
            }).then(result => {
              this.$parent.loadLists()
            })
          }
        })
      }
    }
  }
</script>

<style scoped>
  .createTask {
    opacity: 0.4;
  }

  .createTask:hover {
    opacity: 1;
  }
</style>
