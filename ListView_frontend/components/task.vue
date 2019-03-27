<template>
  <div class="border border-secondary rounded my-1 py-1 bg-white" @click="isChecked = !isChecked">
    <div class="row" data-toggle="tooltip" data-placement="bottom" :title="taskO.description">
      <div class="col-auto ml-2">
        <input type="checkbox" v-model="isChecked">
      </div>
      <div class="col pr-5" :style="[isChecked ? {opacity: 0.5} : {opacity : 1}]">
        {{taskO.name}}
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

</style>
