import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
      chartData: props.chartData,
    }
    console.log(props);
  }

  static defaultProps = {
    displayTitle: true,
    displayLegend: true,
    legendPosition: 'right'
  }
  componentWillReceiveProps(props) {
    this.setState({chartData :props.chartData});
  }

  render(){
    return (
      <div className = 'chart'>
        <Line
            data={this.state.chartData}
            width={100}
            height={50}
            options={{
              title:{
                display: this.props.displayTitle,
                text: this.props.title,
                fontSize:24
              },
              legend:{
                display: this.props.displayLegend,
                position: this.props.legendPosition,
                labels:{
                  fontColor:'#000'
                }
              },
            }}

          />

      </div>
    )
  }
}

export default Chart;
