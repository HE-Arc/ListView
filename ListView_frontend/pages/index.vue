<template>
  <div>
    <section class="container">
    <div>
      <h1 class="title">ListView_frontend</h1>
    </div>
  </section>
    <div>
      Temporaire, juste pour tester<br />
      <button @click="request">Requête protegé</button>
      {{message}}
    </div>
  </div>

</template>

<script>

export default {
  data() {
    return {
      message: ''
    }
  },
  methods: {
    request() {
      this.$axios.get('api/private').then(response=> {
        this.message = response.data
      })
    }
  }
}
</script>

<style>

</style>
