import React, { useEffect, useState } from 'react'
import { ClubNavigation } from './ClubNavigation'
import '../styles/scre.css';
import { MainNav } from './MainNav';
import { SubNav } from './SubNav';

import logoImage from '../static/images/pl-main-logo.png'


const Header = ({lists}) => {

    const [isOpen, setIsOpen] = useState(false)
    const [scrolling, setScrolling] = useState(false);



    
    useEffect(() => {
        const handleScroll = () => {
            if (window.scrollY > 110) {
                setScrolling(true);
            } else {
                setScrolling(false);
            }
        };
    
        window.addEventListener('scroll', handleScroll);
        return () => {
          window.removeEventListener('scroll', handleScroll);
        };
    }, []);




    useEffect(() => {
        if (isOpen) {
            document.body.classList.add("mastheadOpen")
        } else {
            document.body.classList = "";
        }
    }, [isOpen])


    return (

        <header className="masthead">

        <a className="skipTo" href="#mainNav">Skip to main navigation</a>
        <a className="skipTo" href="#mainContent">Skip to main content</a>

    
        <ClubNavigation/>
    
    
            
        <div className={scrolling?"fixedContainer js-fixed-container fixed":"fixedContainer js-fixed-container "}>
            <a href="home" className="logoContainer js-logo-container" aria-label="Premier League Home Page on logo link">
                <img className="pl-header-logo" src={logoImage} alt="Premier League Logo"/>
                <div className="logoBackground"></div>
            </a>
            <div className="navContainer"  data-script="pl_global-header">
                <section id="mainNav" className="navBar js-nav-bar" role="menubar">
                    <div className="menuBtn js-hamburger-toggle" role="button" id="hamburgerToggle" aria-expanded="false" onClick={() => setIsOpen(!isOpen)}>
                        <div className="menuBtnContainer">
                            <div></div>
                            <div></div>
                            <div></div>
                        </div>
                    </div>
    
                   <MainNav lists={lists} />
    
    
                    <a href="#!" className="navLink navOption navOption--no-border fantasySignIn nav-sign-in-btn" role="button" tabIndex="0">
                        <span className="fantasySignInLabel">Sign in</span>
                    </a>
                    
                    <a href="#!" className="navLink navOption navOption--no-border fantasySignOut" role="button" tabIndex="0">
                        <span className="fantasyUsername"></span>
                    </a>

                </section>
            </div>
    
    
    
    
            <SubNav options={lists[0].options}/>
        </div>
    
    
    </header>
    )
  }
  
  export default Header