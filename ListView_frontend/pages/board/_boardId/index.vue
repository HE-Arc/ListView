<template>
  <div class="container-fluid p-4">
    <h1 class="display-3 text-center">{{name}}</h1>
    <div class="row text-center">
      <div class="col-md-2" v-for="l in lists">
        <list :name="l.name" :key="l.id" :tasks="l.tasks" :id="l.id"></list>
      </div>
      <div class="col-md-2">
        <div class="border border-secondary rounded my-2 px-1 bg-secondary createList" @click="createList">
          <i class="fas fa-plus"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import List from '~/components/list'

  export default {
    name: 'index',
    components: {
      List
    },
    data () {
      return {
        lists: [],
        name: "",
      }
    },
    mounted () {
      this.$nextTick(() => {
        if (this.$store.state.auth.isLogged === true) {
          this.loadLists()
        } else {
          this.$store.watch(() => this.$store.getters['auth/logged'], () => {
            this.loadLists() //Wait, while checking if session is logged
          })
          setTimeout(() => { //If we aren't logged after 1s redirect to login
            if (this.$store.state.auth.isLogged === false) {
              this.$store.dispatch('auth/login')
            }
          }, 1000)
        }
      })
    },
    methods: {
      loadLists () {
        this.$axios.get(`/api/boards/${this.$route.params.boardId}`).then(result => {
          this.lists = result.data.lists
          this.name = result.data.name
        })
      },
      createList () {
        this.$swal({
          title: 'New list',
          inputPlaceholder: 'List name',
          input: 'text',
          showCancelButton: true,
        }).then(listName => {
          if (listName) {
            this.$axios.post('/api/list/', {
              name: listName.value,
              board_id: this.$route.params.boardId
            }).then(result => {
              this.loadLists()
            })
          }
        })
      },
    }
  }
</script>

<style scoped>
  i {
    font-size: 4em;
  }
  .createList {
    opacity: 0.4;
  }
  .createList:hover {
    opacity: 1;
  }
</style>
