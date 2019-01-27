import React, { Component } from 'react';
import logo from './logo.svg';
import PostList from './posts/PostList';
import './App.css';
import Chart from './components/Chart';
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
            data:valueArray,
            backgroundColor:[
              'rgba(255, 99, 132, 0.6)',
              
            ]
          }
        ]
      }
    });

    
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to this amazing app </h2>
        </div>
        <Chart chartData={this.state.chartData} location="Massachusetts" legendPosition="bottom"/>
      </div>
    );
  }
}

export default App;