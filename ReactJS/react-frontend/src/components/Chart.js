import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';


class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
      chartData:props.chartData
    }
  }

  static defaultProps = {
    displayTitle:true,
    displayLegend: true,
    legendPosition:'right',
    service:'Service'
  }

  render(){
    return (
      <div className="chart">
        <Line
          width={100}
          height={500}
          data={this.state.chartData}
          options={{
            maintainAspectRatio: false,
            title: {
              display: this.props.displayTitle,
              text: 'Your use of '+ this.props.service,
              fontSize: 25
            },
            legend: {
              display: this.props.displayLegend,
              position: this.props.legendPosition
            },
            responsive: true
          }}
        />
      </div>
    )
  }
}

export default Chart;
