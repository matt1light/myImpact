import React, { Component } from 'react';
import logo from './logo.svg';
import PostList from './posts/PostList';
import './App.css';
import Chart from './components/Chart';
import PostData from './data/posts.json';
import { Button, ButtonGroup} from 'reactstrap';
import get_rates_by_device_and_time_frame from './components/ApiRequests'

// const PostData = get_rates_by_device_and_time_frame(1, '2019-01-26T16:08:22.656938Z', '2019-01-26T19:08:22.656938Z')
// const PostData = fetch('http://localhost:8000/rates/?time__gte=2019-01-26T16%3A08%3A22.656938Z&time__lte=2019-01-26T20%3A08%3A22.656938Z&device=&name=&name__in=&name__startswith=')


class App extends React.Component {
  constructor(){
    super();
    this.state = {
      chartData:{},
      service: "Trash"
    }
  }
  onRadioBtnClick(rSelected) {
    this.setState({ service: rSelected });
  }

  componentWillMount(){
    this.getChartData();
  }

  getChartData(){

    const valueArray = PostData.map(
      postDetail =>  postDetail.value
    )
    const unit = PostData[0].unit
    const name = PostData[0].name
    const timeArray = PostData.map(
      postDetail => postDetail.time
    )
    var service = "Trash"
    // Ajax calls here
    //const api_call = await fetch();
    //const data = await api_call.json();
    fetch('http://localhost:8000/rates/?time__gte=2019-01-26T16%3A08%3A22.656938Z&time__lte=2019-01-26T20%3A08%3A22.656938Z&device=&name=&name__in=&name__startswith=')
      .then(results => {
        return results.json()
      }).then(PostData => {
      const valueArray = PostData.map(
        postDetail =>  postDetail.value
      )
      const unit = PostData[0].unit
      console.log(unit)
      const name = PostData[0].name
      const timeArray = PostData.map(
        postDetail => postDetail.time
      )

      console.log(timeArray)
      // Ajax calls here
      //const api_call = await fetch();
      //const data = await api_call.json();
      this.setState({
        chartData:{
          labels: timeArray,
          datasets:[
            {
              label: name,
              data: valueArray,
              backgroundColor: ['rgba(49, 198, 83, 0.5)']
            }
          ]
        },
        service: service
      });
    })
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to myImpact </h2>
        </div>
        <div className="chart">
          <Chart chartData={this.state.chartData} service={this.state.service} legendPosition="right"/>
        </div>
        <div className="device_container">
          <ButtonGroup>
            <Button onClick={() => this.onRadioBtnClick("Trash")} active={this.state.rSelected === "Trash"}>Trash</Button>
            <Button onClick={() => this.onRadioBtnClick("Water")} active={this.state.rSelected === "Water"}>Water</Button>
            <Button onClick={() => this.onRadioBtnClick("Electricty")} active={this.state.rSelected === "Electricty"}>Electricty</Button>
            <Button onClick={() => this.onRadioBtnClick("Gas")} active={this.state.rSelected === "Gas"}>Gas</Button>
          </ButtonGroup>
        </div>
      </div>
    );
  }
}

export default App;
