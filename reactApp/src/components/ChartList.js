import React, { Component } from 'react';
import IssueMonthItem from './IssueMonthItem';
import CollegeMonthItem from './CollegeMonthItem';
import IssueCollegeItem from './IssueCollegeItem';
import IssueItem from './IssueItem';
import PostItem from './PostItem';
import './chart.css';
//import header from '../header';

class ChartList extends Component {
  constructor(){
    super();
    this.state = {
    }
  }

	render() {
		return (
        <div >
          <h1> ? אתם סטודנטים </h1>
          <h2> ? התוודיתם </h2>
            <h3> ? באיזה מוסד אקדמי אתם לומדים </h3>
            <CollegeMonthItem />
              <h1>! רגע </h1>
          <h3> ? איזה נושא הכי מדובר בכל חודש </h3>

            <IssueMonthItem />
            <h1> ? מצאתם את הנושא שכתבתם עליו </h1>
            <h2> ...זה תלוי איפה אתם לומדים </h2>
          <IssueCollegeItem />
          <IssueItem />
          <PostItem />
        </div>

		);
  }
}
export default ChartList;
