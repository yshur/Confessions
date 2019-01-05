import React, { Component } from 'react';
import './App.css';
import ChartList from './components/ChartList';

class App extends Component {
  constructor(){
    super();
    this.state = {

    }
  }

  render() {
    return (
      <div className="App">
          <ChartList legendPosition='bottom'/>
          <div className="footer">
  					<p style={{marginTop: "20px"}}> &copy; All right reserved to Roi Shmueli & Yair Shur</p>
  				</div>
      </div>
    );
  }
}

export default App;
