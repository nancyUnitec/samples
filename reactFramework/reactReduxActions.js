hiahia

export function getXXX(index, xxx_months) {
    let url_path = `${Constants.XXX_URL}`
    let search = `?`
    if (xxx_months !== "") {
      search += `xxx_months=${xxx_months}`
    }
    if (search.length > 1) {
      url_path += search
    }
    console.log("url to get data for condition row: ", url_path)
    return {
      type: Constants.XXX,
      meta: {
        index: index,  
      },//meta save local data, no need to wait the respond from server. will be fetch in reducer
      //in reducer file, we use action.meta.index to fetch this 
      payload: makeRequest({
        headers: { 'Content-Type': 'application/json' },
        method: 'GET',
        url: url_path
      })//payload save the response from the server, we will fetch this in the reducer using: action.payload.response
      //so in reducer, both the 2 will be used:
      //action.meta.index
      //action.payload.response
    }
  }