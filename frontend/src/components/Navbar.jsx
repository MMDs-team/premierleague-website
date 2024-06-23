import React from 'react';
import {Container} from 'react-bootstrap';
import clubImage from '../static/images/clubImage.png'
import mainLogo from '../static/images/pl-main-logo.png'
import './styles/header.css'

export const Navbar = () => {



    return (
        <div className='nav-wrapper'>
            <Container className="top-nav">
                <div className="club-sites">
                    Club Sites
                    <i className="fa-solid fa-arrow-up-right-from-square"></i>
                    </div>
                <ul className="clubs-logo">
                    {Array.from(Array(20)).map((club, i) => (
                        <li key={i}>
                            <a href='/'>
                                <img src={clubImage} alt='club-image'/>
                            </a>
                        </li>
                    ))}
                </ul>
            </Container>

            <div className="bottom-nav">
                <div className="main-nav">
                    <a href='/'>
                        <img src={mainLogo} alt='premier logo'/>
                    </a>
                    <div className="navv">
                        <ul>
                            <li><a href='/'>Premier League</a></li>
                            <li><a href='/'>Fantasy</a></li>
                            <li><a href='/'>Football & Community</a></li>
                            <li><a href='/'>About</a></li>
                            <li><a href='/'>More</a></li>
                        </ul>
                        <button className="sign-in-btn">Sign in</button>
                    </div>
                </div>

                <div className="prem-nav">
                    <div className='nav-bar'>
                        <div>Home</div>
                        <div>Fixtures</div>
                        <div>Results</div>
                        <div>Tables</div>
                        <div>Transfers</div>
                        <div>Stats</div>
                        <div>News</div>
                        <div>Tickets</div>
                        <div>Clubs</div>
                        <div>Players</div>
                        <div>Awards</div>
                        <div>Pre-season-friendlies</div>
                    </div>
                </div>

            </div>
        </div>
    )
}
