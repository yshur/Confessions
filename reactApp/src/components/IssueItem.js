import React, { Component } from 'react';
import './chart.css';
import axios from 'axios'

class IssueItem extends Component {
  constructor(){
    super();
    this.state = {
      issuesArray: []
    }
    this.add = this.add.bind(this)
    this.eachIssue = this.eachIssue.bind(this)
  }
  componentDidMount() {
    var url = 'https://collegeconffessions.herokuapp.com/';
    // console.log(url)
    axios.get(url)
      .then((res) => {
        // console.log(res)
        var self=this;
        res.data.map((Issues) => {
                self.add(Issues)
                // console.log(Issues)
              });
     })
}

  add(Issues) {
    var grouped = Object.create(null);
    // make array of issues with words
    for (var key in Issues) {
      // console.log(key, Issues[key]);
      grouped[Issues[key]] = grouped[Issues[key]] || [];
      grouped[Issues[key]] = grouped[Issues[key]]+", "+key;
    }

      var result = Object.keys(grouped).map(function(key) {
        return [key, grouped[key]];
      });
      delete result[0];
      // console.log(result);
      this.setState(prevState => ({
          issuesArray: result
      }));
    }

    eachIssue(issue) {
    // console.log(issue)
    return (
      <tr>
        <th>
          {issue[0]}
        </th>
        <td>
          {issue[1]}
        </td>
      </tr>
    )
  }
    render() {
      return <div>
        <h1> ? איך הגענו לרשימת הנושאים הזו </h1>
        <table><tbody>
        {this.state.issuesArray.map(this.eachIssue)}
      </tbody></table></div>;
  }
}



export default IssueItem;
