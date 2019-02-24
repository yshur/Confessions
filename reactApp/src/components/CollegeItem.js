import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class CollegeItem extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {},
      labels: [],
      Total: [],
	  title: 'Sum Confessions Per College'
    }
    this.add = this.add.bind(this)
  }
  componentDidMount() {
  var url = 'https://collegeconfessions.herokuapp.com/getSumPostsByCollege';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart._id.college, Chart.count)
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
                fill:false,
                hoverBorderColor:'#000'
                }]
          }
     }))

})
}
  add(college, count) {
    console.log(college+": "+count)
		this.setState(prevState => ({
        labels: [
          ...prevState.labels,
            college
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
export default CollegeItem;
