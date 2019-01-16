import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class DayItem extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {},
      labels: [],
      Total: [],
	  title: 'Sum Confessions Per Day'
    }
    this.add = this.add.bind(this)
  }
  componentDidMount() {
  var url = 'https://collegeconfessions.herokuapp.com/getSumPostsByDay';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart._id.year, Chart._id.month, Chart._id.day, Chart.count)
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
  add(year, month, day, count) {
    console.log(year+"-"+month+"-"+day+": "+count)
		this.setState(prevState => ({
        labels: [
          ...prevState.labels,
            year+"-"+month+"-"+day
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
export default DayItem;