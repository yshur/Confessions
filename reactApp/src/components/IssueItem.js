// import React, { Component } from 'react';
// import './chart.css';
// import axios from 'axios'
//
// class IssueItem extends Component {
//   constructor(){
//     super();
//     this.state = {
//       issuesArray: [],
//       issuesTable: ''
//     }
//     this.add = this.add.bind(this)
//     this.setTable = this.setTable.bind(this)
//     this.IssueRow = this.IssueRow.bind(this)
//   }
//   componentDidMount() {
//   var url = 'http://localhost:3000/';
//   console.log(url)
//     axios.get(url)
//       .then((res) => {
//         console.log(res)
//         var self=this;
//         res.data.map((Issues) => {
//                 self.add(Issues)
//                 // console.log(Issues)
//               });
//         this.setState(prevState => ({
//                   issuesTable: self.setTable()
//               }));
//      })
// }
//
//   add(Issues) {
//     var grouped = Object.create(null);
//     // make array of issues with words
//     for (var key in Issues) {
//       console.log(key, Issues[key]);
//       grouped[Issues[key]] = grouped[Issues[key]] || [];
//       grouped[Issues[key]] = grouped[Issues[key]]+", "+key;
//       }
//
//       var result = Object.keys(grouped).map(function(key) {
//         return [key, grouped[key]];
//       });
//       this.setState(prevState => ({
//           issuesArray: [
//             ...prevState.issuesArray,
//               result
//             ]
//       }));
//     }
//     setTable() {
//       var self = this;
//       var rows;
//       // console.log(this.state.issuesArray);
//       this.state.issuesArray.map(issue => {
//           rows = rows + self.IssueRow(issue[0], issue[1]);
//         });
//       return <div>
//         <h1>Issue Array</h1>
//        <table>  < tbody > { rows } < /tbody> < /table>
//        </div>;
//     }
//
//
//     IssueRow(key, value) {
//       return <tr><th>{ key }</th><td>{ value }</td></tr>
//     }
//
// render() {
//     console.log(this.state.issuesTable[0]);
//     return <div>
//       { this.state.issuesTable }
//       </div>
//   }
// }
//
//
//
// export default IssueItem;
