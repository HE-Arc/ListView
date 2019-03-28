export const state = () => ({
  shouldRefreshTeam: false,
})

export const getters = {
  getShouldRefreshTeam(state) {
    return state.shouldRefreshTeam
  }
}

export const mutations = {
  SETSHOULDREFRESH(state, value) {
    state.shouldRefreshTeam = value
  }
}
