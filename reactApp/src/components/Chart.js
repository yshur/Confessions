import React, {Component} from 'react';
import {Line} from 'react-chartjs-2';
// import {Bar, Pie} from 'react-chartjs-2';

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
      chartData: props.chartData,
    }
    // console.log(props);
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
                fontSize:24,
                fontFamily: 'Arial',
                fontStyle: 'bold',
                position: 'top',
                lineHeight: 1
              },
              legend:{
                display: this.props.displayLegend,
                position: this.props.legendPosition,
                labels:{
                  fontColor:'#000'
                }
              },
              layout: {
                padding: {
                    left: 150,
                    right: 50,
                    top: 0,
                    bottom: 90
            }
        }
            }}

          />

      </div>
    )
  }
}

export default Chart;
