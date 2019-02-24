<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <n-link class="navbar-brand" :to="{ name: 'index' }">Navbar</n-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <n-link :to="{ name: 'index' }" class="nav-link">
              Home<span class="sr-only">(current)</span>
            </n-link>
          </li>
          <li class="nav-item">
            <n-link class="nav-link" :to="{ name: 'login' }">Login</n-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
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
