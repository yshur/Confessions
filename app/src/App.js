import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Chart from './components/Chart';

class App extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {}
    }
  }

  componentWillMount(){
    this.getChartData();
  }
  getChartData(){
    this.setState({
      chartData:{
        labels: ['Tel aviv1', 'Haifa', 'Bat-Yam', 'Holon', 'Eilat'],
        datasets:[{
            label:'Popolation',
            data:[
              56755,
              45344,
              23123,
              26565,
              34444,
              34523
            ],
            backgroundColor:[
                   'rgba(255,99,132,1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
                   'rgba(75, 192, 192, 1)',
                   'rgba(153, 102, 255, 1)',
                   'rgba(255, 159, 64, 1)'
                ],
            borderWidth:2,
            borderColor:'#777',
            hoverBorderWidth:3,
            hoverBorderColor:'#000'
            }]
    }});
    }

  render() {
    return (
      <div className="App">
          <Chart chartData={this.state.chartData} legendPosition='bottom'/>
          <Chart chartData={this.state.chartData} legendPosition='right'/>
      </div>
    );
  }
}

export default App;
