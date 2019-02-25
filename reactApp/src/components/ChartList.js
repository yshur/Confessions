import React, { Component } from 'react';
import MonthItem from './MonthItem';
import CollegeItem from './CollegeItem';
import CollegeMonthItem from './CollegeMonthItem';

class ChartList extends Component {
  constructor(){
    super();
    this.state = {
    }
  }

	render() {
    console.log(this.state.chartData);
		return (
        <div>
          <MonthItem />
          <CollegeItem />
          <CollegeMonthItem />
        </div>

		);
  }
}
export default ChartList;
