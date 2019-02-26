import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class IssueCollegeItem extends Component {
  constructor(){
    super();
    this.state = {
      datasets: [],
      labels: [],
      chartData: {},
	     title: 'Sum Confessions of issue Per College'
    }
    this.add = this.add.bind(this)
    this.getRandomColor = this.getRandomColor.bind(this)

  }
  componentDidMount() {
  var url = 'https://collegeconffessions.herokuapp.com/getSumIssuesCollege';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((issue) => {
                self.add(issue[0], issue[1])
              });
        this.setState(prevState => ({
          chartData:{
            labels: this.state.labels,
            datasets: this.state.datasets
          }
        }))

})
}
  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  add(issueName, issueData) {
    console.log(issueName)
      var countArray = []
      var color = this.getRandomColor()
      var self=this;
      issueData.forEach(function (a) {
          countArray.push(a.count);
          if (self.state.labels.indexOf(a.college) < 0) {
            self.setState(prevState => ({
                labels: [
                  ...prevState.labels,
                    a.college
                  ]
            }));
          }
      });
      this.setState(prevState => ({
          datasets: [
            ...prevState.datasets,
            {
                label:issueName,
                data: countArray,
                backgroundColor:[
                  color
                 ],
                borderWidth:2,
                borderColor: color,
                hoverBorderWidth:3,
                fill:false,
                autoSkip: false,
                stepSize: 1,
                hoverBorderColor:'#000'
              }
            ]
          }));
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
export default IssueCollegeItem;
