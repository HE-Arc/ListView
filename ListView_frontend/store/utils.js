export const state = () => ({
  shouldRefreshTeam: false,
  showCreateBoard: false,
})

export const getters = {
  getShouldRefreshTeam(state) {
    return state.shouldRefreshTeam
  },
  getShowCreateBoard(state) {
    return state.showCreateBoard
  }
}

export const mutations = {
  SETSHOULDREFRESH(state, value) {
    state.shouldRefreshTeam = value
  },
  SETSHOWCREATEFORM(state, value) {
    state.showCreateBoard = value
  }
}
