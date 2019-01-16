import React, { Component } from 'react';
import MonthItem from './MonthItem';
import CollegeItem from './CollegeItem';
import DayWeekItem from './DayWeekItem';
import DayItem from './DayItem';

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
          <DayWeekItem />
          <DayItem />
        </div>

		);
  }
}
export default ChartList;
