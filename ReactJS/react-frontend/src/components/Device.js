import React, {Component} from 'react';

class Device extends Component{

  constructor(props){
    super(props);
    this.state = {
      deviceData:props.deviceData
    }
  }

  static defaultProps = {
    device:'Service'
  }

  render(){
    return(
      <div class="device_container">
        <h1 className="title-container__title"> Weather Finder</h1>
        <p className="title-container__subtitle"> Find out temperature, conditions and more.. </p>
      </div>
    )
  }
}

export default Device;
