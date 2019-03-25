<template>
  <div class="container border rounded mt-5">
    <h1>{{name}}</h1>
    <div class="row">
      <div class="col-md-3 boardPane text-center py-5 border border-secondary rounded m-2 bg-light" v-for="b in boards"
           @click="$router.push({name: 'board-boardId', params: {boardId: b.id}})">{{b.name}}
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'teamBoard',
    props: {
      name: String,
      boards: Array,
    }
  }
</script>

<style scoped>
  .boardPane {
    height: 130px;
  }

  .boardPane:hover {
    background-color: #7f828b !important;
    border-color: blue !important;
  }
</style>
