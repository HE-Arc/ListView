<template>
  <div class="border border-secondary rounded my-1">
    <div class="row">
      <div class="col-auto ml-2">
        <input type="checkbox" v-model="isChecked">
      </div>
      <div class="col pr-5">
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

<style scoped>

</style>
