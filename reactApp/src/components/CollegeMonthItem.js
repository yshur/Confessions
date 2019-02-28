import React, { Component } from 'react';
import Chart from './Chart';
import './chart.css';
import axios from 'axios'

class CollegeMonthItem extends Component {
  constructor(){
    super();
    this.state = {
      datasets: [],
      labels: [
        '01/2018','02/2018','03/2018',
        '04/2018','05/2018','06/2018','07/2018',
        '08/2018','09/2018','10/2018','11/2018',
        '12/2018','01/2019'
              ],
      chartData: {},
	     title: ''
    }
    this.add = this.add.bind(this)
    this.getRandomColor = this.getRandomColor.bind(this)

  }
  componentDidMount() {
  var url = 'https://collegeconffessions.herokuapp.com/getSumCollegeMonth';
  // console.log(url)
    axios.get(url)
      .then((res) => {
        // console.log(res)
        var self=this;
        res.data.map((college) => {
                self.add(college[0], college[1])
              //  // console.log(Chart)
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
  add(collegeName, collegeData) {
    // console.log(collegeName)
      var countArray = [0,0,0,0,0,0,0,
                        0,0,0,0,0,0]
      var color = this.getRandomColor()
      collegeData.forEach(function (a) {
          if(a.year < 2018) {
            return;
          }
          if(a.year === 2018) {
            countArray[a.month-1] = a.count
          } else {
            countArray[12] = a.count
          }
      });
      this.setState(prevState => ({
          datasets: [
            ...prevState.datasets,
            {
                label:collegeName,
                data: countArray,
                backgroundColor:[
                  color
                 ],
                borderWidth:2,
                borderColor: color,
                hoverBorderWidth:3,
                fill:false,
                hoverBorderColor:'#000',

              }
            ]
          }));
      }




	render() {
    // console.log(this.state.datasets);
		return (
        <div>
          <Chart chartData={this.state.chartData} title={this.state.title} legendPosition='right'/>
        </div>

		);
  }
}
export default CollegeMonthItem;
