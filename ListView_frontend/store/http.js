const endpoints = {
  refreshToken: 'api/token/refresh/'
}

const tokenLifeTime = {
  access: 4,
  refresh: 1439 // 1 day - 1 minute
}

function addMinutes (minutes) {
  return new Date(Date.now() + minutes * 60000)
}

function minutesSinceDate (date) {
  return Math.floor((Date.now() - date.getTime()) / 60000) + 1
}

export const state = () => ({
  accessToken: null,
  refreshToken: null,
  accessDate: null,
  refreshDate: null,
  isLogged: false,
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
    state.accessDate = tokens.accessDate
    state.refreshDate = tokens.refreshDate
  },
  REMOVETOKEN (state) {
    state.accessToken = null
    state.refreshToken = null
    state.accessDate = null
    state.refreshDate = null
  },
  SETLOGIN(state, value) {
    state.isLogged = value
  }
}

export const actions = {
  loadToken () {
    const accessToken = sessionStorage.getItem('accessToken')
    const refreshToken = sessionStorage.getItem('refreshToken')
    const accessDate = new Date(Date.parse(sessionStorage.getItem('accessDate')) || null)
    const refreshDate = new Date(Date.parse(sessionStorage.getItem('refreshDate')) || null)
    this.$axios.setToken(accessToken, 'Bearer')
    this.dispatch('http/isTokenValid')
    this.commit('http/LOADTOKEN', {
      accessToken: accessToken,
      refreshToken: refreshToken,
      accessDate: accessDate,
      refreshDate: refreshDate
    })
  },
  updateToken ({ commit, state }, tokens) {
    let accessExpire = addMinutes(tokenLifeTime.access)
    let refreshExpire = addMinutes(tokenLifeTime.refresh)
    sessionStorage.setItem('accessToken', tokens.access)
    sessionStorage.setItem('refreshToken', tokens.refresh)
    sessionStorage.setItem('accessDate', accessExpire)
    sessionStorage.setItem('refreshDate', refreshExpire)
    this.$axios.setToken(tokens.access, 'Bearer')
    this.commit('http/SETLOGIN', true)
    this.commit('http/LOADTOKEN', {
      accessToken: tokens.access,
      refreshToken: tokens.refresh,
      accessDate: accessExpire,
      refreshDate: refreshExpire
    })
  },
  removeToken () {
    return new Promise(() => {
      sessionStorage.removeItem('accessToken')
      sessionStorage.removeItem('refreshToken')
      sessionStorage.removeItem('accessDate')
      sessionStorage.removeItem('refreshDate')
      this.$axios.setToken(null, 'Bearer')
      this.commit('http/SETLOGIN', false)
      this.commit('http/REMOVETOKEN')
    })
  },
  isTokenValid ({ commit, state }) {
    return new Promise((resolve, reject) => {
      if (state.accessDate && minutesSinceDate(state.accessDate) < tokenLifeTime.access) {
        this.commit('http/SETLOGIN', true)
        resolve(true)
      } else if (state.refreshDate && minutesSinceDate(state.refreshDate) < tokenLifeTime.refresh) {
        this.$axios.$post(endpoints.refreshToken, { refresh: state.refreshToken }).then(response => {
          this.$axios.setToken(response.access, 'Bearer')
          sessionStorage.setItem('accessToken', response.access)
          let accessExpire = addMinutes(tokenLifeTime.access)
          sessionStorage.setItem('accessDate', accessExpire)
          this.commit('http/LOADTOKEN', {
            accessToken: response.access,
            refreshToken: state.refreshToken,
            accessDate: accessExpire,
            refreshDate: state.refreshDate
          })
          this.commit('http/SETLOGIN', true)
          resolve(true)
        })
      } else {
        this.commit('http/SETLOGIN', false)
        resolve(false)
      }
    })
  }
}
