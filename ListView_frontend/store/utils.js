export const state = () => ({
  shouldRefreshTeam: false,
  showCreateBoard: false,
  showManageTask: false,
  taskToManage: null,
  listToAddTask: null,
  shouldRefreshBoard: false,
})

export const getters = {
  getShouldRefreshTeam(state) {
    return state.shouldRefreshTeam
  },
  getShowCreateBoard(state) {
    return state.showCreateBoard
  },
  getShowManageTask(state) {
    return state.showManageTask
  },
  getTaskToManage(state) {
    return state.taskToManage
  },
  getListToAddTask(state) {
    return state.listToAddTask
  },
  getShouldRefreshBoard(state) {
    return state.shouldRefreshBoard
  },
}

export const mutations = {
  SETSHOULDREFRESH(state, value) {
    state.shouldRefreshTeam = value
  },
  SETSHOWCREATEFORM(state, value) {
    state.showCreateBoard = value
  },
  SETSHOWMANAGETASK(state, value) {
    state.showManageTask = value
  },
  SETTASKTOMANAGE(state, value) {
    state.taskToManage = value
  },
  SETLISTTOADDTASK(state,value) {
    state.listToAddTask = value
  },
  SETSHOULDREFRESHBOARD(state, value) {
    state.shouldRefreshBoard = value
  },
}
