<template>
  <div class="container my-3 py-2 border border-secondary rounded">
    <div>{{name}}</div>
    <n-link :to="{name: 'team-id', params: {id: id}}" class="nax-item nav-link">{{name}}</n-link>
    <h3>Show team member and add member</h3>
  </div>
</template>

<script>
  export default {
    name: 'teamComponent',
    props: {
      id: Number,
      name: String,
    }
  }
</script>

<style scoped>
</style>
