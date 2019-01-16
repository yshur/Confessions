import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class MonthItem extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {},
      labels: [],
      Total: [],
	  title: 'Sum Confessions Per Month'
    }
    this.add = this.add.bind(this)
  }
  componentDidMount() {
  var url = 'https://collegeconfessions.herokuapp.com/getSumPostsByMonth';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart._id.year, Chart._id.month, Chart.count)
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
  add(year, month, count) {
    console.log(year+"-"+month+": "+count)
		this.setState(prevState => ({
        labels: [
          ...prevState.labels,
            year+"-"+month
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
export default MonthItem;