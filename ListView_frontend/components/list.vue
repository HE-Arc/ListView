<template>
  <div class="border border-secondary rounded my-2 px-1">
    <h1>{{name}}</h1>
    <task :name="t.name" v-for="t in tasks" :key="i"/>
    <div class="border border-secondary rounded my-1 bg-secondary createTask" @click="createTask">
      <i class="fas fa-plus"></i>
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
          if (taskName) {
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
