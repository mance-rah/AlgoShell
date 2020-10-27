import React from 'react';

function Landing() {
    return (
        <div>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:wght@800&display=swap"></link>
            <nav style={{backgroundColor: "#9580FF"}} class="navbar navbar-light">
                <div style={{margin: "auto"}} class="navbar-brand">
                    <p>"It's like LeetCode except it doesn't require the internet"</p>
                </div>
            </nav>

            <nav style={{backgroundColor: "#282A36"}} class="navbar navbar-dark">
                <div class="navbar-brand">
                    <h1 style={{fontFamily: 'Alegreya Sans'}}>AlgoShell</h1>
                </div>
            </nav>

            <div style={{backgroundColor:"#373A59", height:"500px"}}>
                <h1 style={{color: "#50FA7B", fontFamily: 'Alegreya Sans'}}>AlgoShell</h1>
                <p style={{color: "white"}}>Shell shock the coding interviews</p>
                <button class="btn" style={{backgroundColor: "#50FA7B"}}>Start coding</button>
            </div>

            <div style={{backgroundColor:"#282A36", color: "white", height:"500px"}}>
                <p>It's like LeetCode except it doesn't require the internet.</p>
            </div>

            <div style={{backgroundColor: "#373A59", height: "150px"}}>
                <p><span style={{color: "white"}}>AlgoShell</span> <span style={{color: "#50FA7B"}}>Version 1.0</span></p>
            </div>
            
        </div>
    )
}

export default Landing;