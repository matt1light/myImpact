import React, { Component } from 'react';
import logo from './logo.svg';
import PostList from './posts/PostList';
import './App.css';
import Chart from './components/Chart';
import Device from './components/Device';
import PostData from './data/posts.json';
import get_rates_by_device_and_time_frame from './components/ApiRequests'

// const PostData = get_rates_by_device_and_time_frame(1, '2019-01-26T16:08:22.656938Z', '2019-01-26T19:08:22.656938Z')
// const PostData = fetch('http://localhost:8000/rates/?time__gte=2019-01-26T16%3A08%3A22.656938Z&time__lte=2019-01-26T20%3A08%3A22.656938Z&device=&name=&name__in=&name__startswith=')


class App extends React.Component {
  constructor(){
    super();
    this.state = {
      chartData:{}
    }
  }

  componentDidMount(){
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
        }
      });
    })
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
