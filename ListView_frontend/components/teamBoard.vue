<template>
  <div class="container border rounded mt-5">
    <h1>{{name}}</h1>
    <div class="row">
      <div class="col-md-3 text-center p-2" v-for="b in boards"
           @click="$router.push({name: 'board-boardId', params: {boardId: b.id}})">
        <div class="boardPane border border-secondary rounded py-5 bg-light">
          {{b.name}}
        </div>
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
