haha

//use semantic UI
import { Dropdown, Form, Input, Label, Checkbox } from 'semantic-ui-react'

constructor(props) {
    super(props)
    ...
    this.setXxxDropdown = this.setXxxDropdown.bind(this)
    ...
  }

var options = [...]

const xxxxx_options = [
    { id: shortid.generate(), text: '12', value: 12 },
    { id: shortid.generate(), text: '24', value: 24 },
    { id: shortid.generate(), text: '36', value: 36 },
  ]

handleXxxChange(e, data) {
    this.setState({ demo_xxx: data.value })  
  }

setXxxDropdown(e, data) {
    var option = data.options.find(((item) => item.value === data.value))
    if (!!option) {
        this.props.dispatch(RateReduxActions.setXxx(this.props.index, option.id, option.value))
    }
}

<Label> Selected Xxx </Label>
<Dropdown
value={this.state.demo_xxx} multiple search selection options={options} floated='right'
onChange={this.handleXxxChange}
/>

<Dropdown
options={xxxxx_options}
value={this.props.xxx_item.xxx}
compact
search
selection
onChange={this.setXxxDropdown}
/>
