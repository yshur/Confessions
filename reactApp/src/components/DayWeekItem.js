import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class DayWeekItem extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {},
      labels: [],
      Total: [],
	  title: 'Sum Confessions Per Week Day'
    }
    this.add = this.add.bind(this)
  }
  componentDidMount() {
  var url = 'https://collegeconfessions.herokuapp.com/getSumPostsByWeekDay';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart._id.day, Chart.count)
                console.log(Chart)
              });
        this.setState(prevState => ({
          chartData:{
            labels: this.state.labels,
            datasets:[{
                label:'Count of Posts',
                data: this.state.Total,
                backgroundColor:[ ],
                borderWidth:2,
                borderColor:'#777',
                hoverBorderWidth:3,
                hoverBorderColor:'#000'
                }]
          }
     }))

})
}
  add(day, count) {
    console.log(day+": "+count)
		this.setState(prevState => ({
        labels: [
          ...prevState.labels,
            day
          ],
          Total: [
            ...prevState.Total,
              count
            ]
		}));

	}


	render() {
    console.log(this.state.chartData);
		return (
        <div>
          <Chart chartData={this.state.chartData} title={this.state.title} legendPosition='bottom'/>
        </div>

		);
  }
}
export default DayWeekItem;