<template>
  <div class="container login-div">
    <form method="post" class="login-form border border-secondary rounded p-4">
      <div class="form-group row">
        <label for="username" class="col-sm-2 col-form-label">Username</label>
        <div class="col-sm-10">
          <input type="username" class="form-control plaintext" id="username" placeholder="username" v-model="username">
        </div>
      </div>
      <div class="form-group row" v-if="isRegisterForm">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control plaintext" id="email" placeholder="email" v-model="email">
        </div>
      </div>
      <div class="form-group row">
        <label for="password" class="col-sm-2 col-form-label">Password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
        </div>
      </div>
      <div class="form-group row" v-if="isRegisterForm">
        <label for="password_confirm" class="col-sm-2 col-form-label">Confirm password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="password_confirm" placeholder="Confirme password"
                 v-model="password_confirm">
        </div>
      </div>
      <div class="form-group row">
        <button class="btn btn-outline-primary col-sm-5 mx-auto" @click.prevent="startLogin">{{logText(true)}}</button>
        <button class="btn btn-outline-secondary col-sm-5 mx-auto" @click.prevent="switchForm">{{logText(false)}}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        email: '',
        password: '',
        password_confirm: '',
        isRegisterForm: false

      }
    },
    mounted () {
      let instance = this
      setTimeout(() => {
        //without setTimeout the session aren't already up. We should find another way to fix it
        if (instance.$store.getters['http/isLogged']) {
          instance.$router.push({ 'name': 'index' })
        }
      }, 10)
    },
    methods: {
      startLogin () {
        if (this.isRegisterForm) {
          if(this.username && this.password && this.password_confirm) {
            if(this.password === this.password_confirm) {
              this.$axios.post('api/users/', {username: this.username, password: this.password, email: this.email}).then(response => {
                this.login()
              })
            } else {
              // Password should match
            }
          } else {
            // Missing information
          }
        } else {
          this.login()
        }
      },
      login () {
        if (this.username && this.password) {
          this.$axios.post('api/token/', { username: this.username, password: this.password }).then((response) => {
            this.$store.dispatch('http/updateToken', response.data)
            this.$router.push({ 'name': 'index' })
          })
        }
      },
      switchForm () {
        this.isRegisterForm = ! this.isRegisterForm
      },
      logText (isPrimary) {
        if (isPrimary) {
          return this.isRegisterForm ? 'Sign up' : 'Log in'
        }
        return this.isRegisterForm ? 'Log in' : 'Sign up'
      }
    },

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
