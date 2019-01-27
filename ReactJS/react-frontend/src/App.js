import React, { Component } from 'react';
import logo from './logo.svg';
import PostList from './posts/PostList';
import './App.css';
import Chart from './components/Chart';
import Device from './components/Device';
import PostData from './data/posts.json';

class App extends React.Component {
  constructor(){
    super();
    this.state = {
      chartData:{}
    }
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
        }
      });
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to myImpact </h2>
        </div>
        <Chart chartData={this.state.chartData} height={200} width={500} options={{ maintainAspectRatio: false }} service="Trash" legendPosition="right"/>
        <Device deviceData={this.state.deviceData} service="Trash"/>
      </div>
    );
  }
}

export default App;
