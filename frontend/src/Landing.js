import React from 'react';

function Landing() {
    return (
        <div>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:wght@800&display=swap"></link>
            <nav style={{backgroundColor: "#9580FF"}} class="navbar navbar-light">
                <div style={{margin: "auto"}} class="navbar-brand">
                    <p><em>"It's like LeetCode except it doesn't require the internet"</em></p>
                </div>
            </nav>

            <nav style={{backgroundColor: "#282A36"}} class="navbar navbar-dark">
                <div class="navbar-brand">
                    <h1 style={{fontFamily: 'Alegreya Sans'}}><img id="shelly" src="/sea-snail.png" /> AlgoShell</h1>
                </div>
            </nav>

            <div id="main" style={{backgroundColor:"#373A59", height:"500px"}}>
                <div>
                <h1 style={{color: "#50FA7B", fontFamily: 'Alegreya Sans'}}><img src="/sea-snail.png" />AlgoShell</h1>
                <p style={{color: "white"}}>Shell shock the coding interviews</p>
                <button class="btn-lg" style={{backgroundColor: "#50FA7B"}}>Start Coding</button>
                </div>
            </div>

            <div id="under-main" style={{backgroundColor:"#282A36", color: "white", height:"720px"}}>
                <div>
                <p><em>It's like LeetCode except it doesn't require the internet.</em></p>
                <iframe width="300" height="500" src="https://www.youtube.com/embed/k-famToMuqY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <div id="footer" style={{backgroundColor: "#373A59", height: "120px"}}>
                <div>
                <p><span style={{color: "white"}}><img src="/sea-snail.png" />AlgoShell</span> <span style={{color: "#50FA7B"}}>Version 1.0</span></p>
                </div>
            </div>
            
        </div>
    )
}

export default Landing;