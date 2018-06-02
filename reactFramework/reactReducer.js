never commit lc code

switch (action.type) {
    case Constants.XXX_PENDING: {
      state.xxx_items[action.meta.index].save_loading = true
      return {
        ...state,
       xxx_error: {},
      }
    }

    case Constants.XXX_REJECTED: {
      state.xxx_items[action.meta.index].save_loading = false
      return {
        ...state,
        xxx_error: action.payload.response,
      }
    }

    case Constants.XXX_FULFILLED: {
      console.log("XXX_FULFILLED state.xxx_items = ", state.xxx_items)
      state.xxx_items[action.meta.index].data = action.payload.data
      return {
        ...state,
        xxx_error: {},
        // data_for_condition_row: action.payload.data,
      }
    }