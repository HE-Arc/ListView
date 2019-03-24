export const state = () => ({
  show: false,
})

export const mutations = {
  SETSHOW(state, value) {
    state.show = value
  }
}
