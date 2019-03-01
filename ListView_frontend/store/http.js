const endpoints = {
  refreshToken: 'api/token/refresh/'
}

export const state = () => ({
  accessToken: null,
  refreshToken: null,
  isLogged: false
})

export const getters = {
  isLogged(state) {
    return state.isLogged
  }
}

export const mutations = {
  LOADTOKEN (state, tokens) {
    state.accessToken = tokens.accessToken
    state.refreshToken = tokens.refreshToken
    if (tokens.accessToken) {
      state.isLogged = true
    }
  },
  UPDATETOKEN (state, tokens) {
    state.accessToken = tokens.access
    state.refreshToken = tokens.refresh
    if (tokens.access) {
      state.isLogged = true
    }
  },
  REMOVETOKEN (state) {
    state.accessToken = null
    state.refreshToken = null
    state.isLogged = false
  }
}

export const actions = {
  loadToken () {
    const accessToken = sessionStorage.getItem('accessToken')
    const refreshToken = sessionStorage.getItem('refreshToken')
    this.$axios.setToken(accessToken, 'Bearer')
    this.commit('http/LOADTOKEN', { accessToken, refreshToken })
  },
  updateToken ({ commit, state }, tokens) {
    sessionStorage.setItem('accessToken', tokens.access)
    sessionStorage.setItem('refreshToken', tokens.refresh)
    this.$axios.setToken(tokens.access, 'Bearer')
    this.commit('http/UPDATETOKEN', tokens)
  },
  removeToken () {
    return new Promise(() => {
      sessionStorage.removeItem('accessToken')
      sessionStorage.removeItem('refreshToken')
      this.$axios.setToken(null, 'Bearer')
      this.commit('http/REMOVETOKEN')
    })
  }
}
