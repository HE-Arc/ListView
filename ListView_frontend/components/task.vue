<template>
  <div class="border border-secondary rounded my-1">
    {{name}}
  </div>
</template>

<script>
  export default {
    name: 'task',
    props: {
      name: String,
      checked: Boolean,
    }
  }
</script>

<style scoped>

</style>
