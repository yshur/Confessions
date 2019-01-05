import React, { Component } from 'react'
// import chartDetails from './chartDetails'
import Chart from './Chart';

class ChartItem extends Component {

 constructor(props) {
   super(props)
   console.log(props);

   this.state = {
     chartData: {}
   }
 }

 componentDidMount() {
   this.getChartData(this.props);
   //this.getChartData().then(this.refreshChart)
 }
 getChartData(props){
   this.setState({
     chartData:{
       labels: props.labels,
       datasets:[{
           label:'Frequency',
           data: props.total,
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
   console.log(this.state.chartData)

   }
 render() {
   console.log(this.state.chartData)
     return (
       <div className="App">
          <Chart chartData={this.state.chartData} legendPosition='bottom'/>
      </div>
   )
}
}
export default ChartItem;
