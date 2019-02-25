const endpoints = {
  obtainToken: 'api/token/',
  refreshToken: 'api/token/refresh/'
}

export const state = () => ({
  accessToken: null,
  refreshToken: null
})

export const mutations = {
  LOADTOKEN (state, tokens) {
    state.accessToken = tokens.accessToken
    state.refreshToken = tokens.refreshToken
  },
  UPDATETOKEN (state, tokens) {
    state.accessToken = tokens.access
    state.refreshToken = tokens.refresh
  },
  REMOVETOKEN (state) {
    state.accessToken = null
    state.refreshToken = null
  }
}

export const actions = {
  obtainToken ({ commit, state }, payload) {
    this.$axios.post(endpoints.obtainToken, payload).then((response) => {
      this.dispatch('http/updateToken', response.data)
    })
  },
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
    sessionStorage.removeItem('accessToken')
    sessionStorage.removeItem('refreshToken')
    this.$axios.setToken(null, 'Bearer')
    this.commit('http/REMOVETOKEN')
  }
}
