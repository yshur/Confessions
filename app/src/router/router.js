import React from "react"
import { Route } from "react-router-dom"
import ChartList from "../components/ChartList"
import Header from "../Header"

const ReactRouter =()=>{
    return (
        <React.Fragment>
            <Header/>
            <Route exact path="/" component={ChartList}/>
        </React.Fragment>
        );
}

export default ReactRouter;
