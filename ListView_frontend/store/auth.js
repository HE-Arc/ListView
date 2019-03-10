import auth0 from 'auth0-js'

const webAuth = new auth0.WebAuth({
  domain: 'stevenj.eu.auth0.com',
  redirectUri: 'http://localhost:3000/callback',
  clientID: 'eNA0OohCw2UYecKukT05w5bbC4rzKdqE',
  audience: 'https://django-vue.com',
  responseType: 'token id_token',
})

export const state = () => ({
  isLogged: false,
})

export const mutations = {
  SETLOGGED (state, value) {
    state.isLogged = value
  }
}

export const actions = {
  handleAuthentication () {
    webAuth.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken) {
        this.$axios.setToken(authResult.accessToken, 'Bearer')
        const expiresAt = JSON.stringify(authResult.expiresIn * 1000 + new Date().getTime())
        localStorage.setItem('access_token', authResult.accessToken)
        localStorage.setItem('expires_at', expiresAt)
        this.commit('auth/SETLOGGED', true)
        this.$axios.get('/api/users/').then(response=>{
          this.$axios.patch(`/api/users/${response.data}/`, {
            name: authResult.idTokenPayload.name,
            email: authResult.idTokenPayload.email
          })
        })
      }
      this.$router.replace('/')
    })
  },
  requireAuth ({ commit, state }, { to, from, next }) {
    if (state.isLogged === true) {
      next()
    } else {
      next({
        path: '/',
        query: { redirect: to.fullPath }
      })
    }
  },
  login () {
    webAuth.authorize()
  },
  logout () {
    localStorage.removeItem('access_token')
    localStorage.removeItem('expires_at')
    this.commit('auth/SETLOGGED', false)
    this.$router.push('/')
  },
  authenticated () {
    const expiresAt = JSON.parse(localStorage.getItem('expires_at'))
    if(new Date().getTime() < expiresAt) {
      this.commit('auth/SETLOGGED', true)
      this.$axios.setToken(localStorage.getItem('access_token'), 'Bearer')
    } else {
      this.commit('auth/SETLOGGED', false)
    }
  }

}