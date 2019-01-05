import React, { Component } from 'react';
import Chart from './Chart';
import axios from 'axios'

class ChartList extends Component {
  constructor(){
    super();
    this.state = {
      chartData: {},
      labels: [],
      Total: []
    }
    this.add = this.add.bind(this)
  }

  componentDidMount() {
  var url = 'https://wordsover3000.herokuapp.com/wordsOver3000';
  console.log(url)
    axios.get(url)
      .then((res) => {
        console.log(res)
        var self=this;
        res.data.map((Chart) => {
                self.add(Chart._id, Chart.word, Chart.total)
                console.log(Chart)
              });
        this.setState(prevState => ({
          chartData:{
            labels: this.state.labels,
            datasets:[{
                label:'Frequency',
                data: this.state.Total,
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
          }
     }))

})
}
  add(_id, word, total) {
    console.log(_id+", "+word+", "+total)
		this.setState(prevState => ({
        labels: [
          ...prevState.labels,
            word
          ],
          Total: [
            ...prevState.Total,
              total
            ]
		}));

	}


	render() {
    console.log(this.state.chartData);
		return (
        <div>
          <Chart chartData={this.state.chartData} legendPosition='bottom'/>
        </div>

		);
  }
}
export default ChartList;
