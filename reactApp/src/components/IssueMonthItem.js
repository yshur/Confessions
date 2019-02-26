import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class IssueMonthItem extends Component {
  constructor(){
    super();
    this.state = {
      datasets: [],
      labels: [],
      chartData: {},
	     title: 'Sum Confessions of issue Per Month'
    }
    this.add = this.add.bind(this)
    this.getRandomColor = this.getRandomColor.bind(this)

  }
  componentDidMount() {
  var url = 'http://localhost:3000/getSumIssuesMonth';
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
            labels: this.state.labels.sort(),
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
        if(a.year < 2018) {
          return;
        }
          countArray.push(a.count);
          if(a.month < 10) {
            a.month = "0"+a.month
          }
          if (self.state.labels.indexOf(a.year+"-"+a.month) < 0) {
            self.setState(prevState => ({
                labels: [
                  ...prevState.labels,
                    a.year+"-"+a.month
                  ]
                  //labels: labels.sort()
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
export default IssueMonthItem;
