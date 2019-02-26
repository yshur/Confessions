import React, { Component } from 'react';
import IssueMonthItem from './IssueMonthItem';
import CollegeMonthItem from './CollegeMonthItem';
import IssueCollegeItem from './IssueCollegeItem';

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
          <IssueMonthItem />
          <CollegeMonthItem />
          <IssueCollegeItem />

        </div>

		);
  }
}
export default ChartList;
