<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <n-link class="navbar-brand" :to="{ name: 'index' }"><i class="fal fa-clipboard-list-check"></i> ListView</n-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <n-link :to="{ name: 'index' }" class="nav-item nav-link" active-class="active" exact>
            Home<span class="sr-only">(current)</span>
          </n-link>
          <a class="nav-item nav-link" href="#">Board (todo)</a>
        </ul>
        <ul class="navbar-nav ml-auto">
          <n-link class="nav-item nav-link" :to="{ name: 'login' }" active-class="active" exact>Login</n-link>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: 'navbar'
  }
</script>

<style scoped>

</style>
