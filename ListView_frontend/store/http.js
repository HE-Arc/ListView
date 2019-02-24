export const state = () => ({
  accessToken: null,
  refreshToken: null,
  endpoints: {
    obtainToken: 'api/token/',
    refreshToken: 'api/token/refresh/'
  }
})

export const mutations = {
  loadToken (state) {
    state.accessToken = sessionStorage.getItem('accessToken')
    state.refreshToken = sessionStorage.getItem('refreshToken')
    this.$axios.setToken(state.accessToken, 'Bearer')
  },
  updateToken (state, tokens) {
    sessionStorage.setItem('accessToken', tokens.access)
    sessionStorage.setItem('refreshToken', tokens.refresh)
    state.accessToken = tokens.access
    state.refreshToken = tokens.refresh
    this.$axios.setToken(state.accessToken, 'Bearer')
  },
  removeToken (state) {
    sessionStorage.removeItem('accessToken')
    sessionStorage.removeItem('refreshToken')
    state.accessToken = null
    state.refreshToken = null
    this.$axios.setToken(state.accessToken, 'Bearer')
  },
  obtainToken (state, payload) {
    this.$axios.post(state.endpoints.obtainToken, payload).then((response) => {
      this.commit('http/updateToken', response.data)
    })
  }
}
