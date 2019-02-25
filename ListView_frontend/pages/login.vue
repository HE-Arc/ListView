<template>
  <div class="container login-div">
    <form method="post" class="login-form border border-secondary rounded p-4">
      <div class="form-group row">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control plaintext" id="email" placeholder="email@example.com">
        </div>
      </div>
      <div class="form-group row">
        <label for="password" class="col-sm-2 col-form-label">Password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="password" placeholder="Password">
        </div>
      </div>
      <div class="form-group row">
          <button class="btn btn-outline-primary col-sm-5 mx-auto">Log in</button>
          <button class="btn btn-outline-secondary col-sm-5 mx-auto">Sign up</button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'login'
  }
</script>

<style scoped>
  .login-div {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .login-form {
    width: 500px;
  }
</style>
