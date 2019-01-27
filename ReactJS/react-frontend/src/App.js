import React, { Component } from 'react';
import PostList from './posts/PostList';
import './App.css';
import Chart from './components/Chart';
import logo from './impactlogo.svg'; 
import PostData from './data/posts.json';
import { Button, ButtonGroup} from 'reactstrap';


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
      this.setState({
        chartData:{
          labels: timeArray,
          datasets:[
            {
              label: name,
              data: valueArray,
              backgroundColor: ['rgb(92,230,108, 0.6)']
            }
          ]
        },
        service: service
      });
  }

  render() {
    return (
      <div>
        <div className="wrapper">
          <div>
            <div className="container">
              <div className="logo">
              <h1>
                    <img src= {logo} alt="my impact" />
              </h1>
              </div>
              <div>
              <h2>
                Welcome back Carl,
              </h2>
              <p>
                  Here's how you're doing
              </p>
                </div>
              <div className="chart">
                  <Chart chartData={this.state.chartData} service={this.state.service} legendPosition="disabled"/>
              </div>
              <div className="device_container">
            <ButtonGroup>
              <Button onClick={() => this.onRadioBtnClick("Waste")} active={this.state.rSelected === "Waste"}>Waste</Button>
              <Button onClick={() => this.onRadioBtnClick("Water")} active={this.state.rSelected === "Water"}>Water</Button>
              <Button onClick={() => this.onRadioBtnClick("Electricty")} active={this.state.rSelected === "Electricty"}>Electricty</Button>
              <Button onClick={() => this.onRadioBtnClick("Gas")} active={this.state.rSelected === "Gas"}>Gas</Button>
            </ButtonGroup>
                  </div>
                  <div className="chart">
                  <Chart chartData={this.state.chartData} service={this.state.service} legendPosition="disabled"/>
              </div>
              
                </div>
              </div>
              
            </div>
            <footer>

            </footer>
          </div>
      
    /*<div className=".container"    
    <div>
        
          
          
    </div>
          */
      
    );
  }
}

export default App;
