import React from 'react';
import './Landing.css';

function Landing() {
    return (
        <div className="Landing">
            <div className="Banner">
                <p>"It's like LeetCode except it doesn't require the internet"</p>
            </div>
            <div className="Navbar">
                <p>🐚AlgoShell</p>
            </div>
            <div className="Headline">
                <p className="Headline-Title">🐚AlgoShell</p>
                <p>Shell shock the coding interviews</p>
                <button className="Button">Start coding</button>
            </div>
            <div className="Subheading">
                <div className="Post">
                    <div className="Post-Header">
                        <p>andrewrobles.io</p>
                        <button className="Button">Follow</button>
                    </div>
                    <div className="Post-Description">
                        <p>It's like leetcode except it doesn't require the internet</p>
                    </div>
                    <div className="Post-Song-Title">
                        <p>Dreams - Fleetwood Mac</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Landing;