import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class CollegeMonthItem extends Component {
  constructor(){
    super();
    this.state = {
      datasets: [],
      chartData: {},
      labels: [],
      Total: [],
	  title: 'Sum Confessions of college Per Month'
    }
    this.add = this.add.bind(this)
  }
  componentDidMount() {
  var url = 'https://collegeconffessions.herokuapp.com/getSumCollegeMonth';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart.college, Chart.year, Chart.month, Chart.count)
              //  console.log(Chart)
              });
        for (let ds in this.state.datasets) {
          this.setState(prevState => ({
            Total:[
              ...prevState.Total,
              this.state.datasets[ds]
            ]
          }))
        }
        this.setState(prevState => ({
          chartData:{
            labels: this.state.labels,
            datasets: []//this.state.Total
          }
        }))

})
}
  add(college, year, month, count) {
  //  console.log(college+": "+year+"-"+month+": "+count)
    if (college in this.state.datasets) {
  		this.setState(prevState => ({
        datasets: [
          ...prevState.datasets,
          college.data: [
                college.data,
                count
              ]

        ]
  		}));
    } else {
      this.setState(prevState => ({
        datasets: [
          ...prevState.datasets,
            college: {
                  label: college,
                  data: [count],
                  backgroundColor:[ ],
                  borderWidth:2,
                  borderColor:'#777',
                  hoverBorderWidth:3,
                  fill:false,
                  hoverBorderColor:'#000'
            }
          ]
      }));
    }
    if (!year+"-"+month in this.state.labels) {
      this.setState(prevState => ({
          labels: [
            ...prevState.labels,
              year+"-"+month
            ]
  		}));
    }

	}


	render() {
    console.log(this.state.datasets);
		return (
        <div>
          <Chart chartData={this.state.chartData} title={this.state.title} legendPosition='bottom'/>
        </div>

		);
  }
}
export default CollegeMonthItem;
