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
        this.$store.commit('utils/SETLISTTOADDTASK', this.id)
        this.$store.commit('utils/SETSHOWMANAGETASK', true)
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
