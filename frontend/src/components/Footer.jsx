import React from 'react'
import { SponsorFooter } from './SponsorFooter'
import { lists } from '../App'
import { NavLink } from 'react-router-dom'

export const Footer = () => {

    
  return (
    <footer class="mainFooter">
        <SponsorFooter />

        <div class="footerContent">
            <div class="wrapper">
                <div class="footerCol ">

                    <div class="footerCol ">
                    <h3 class="subHeader">Premier League</h3>
                    <ul class="list--premier-league" role="menu">
                        {lists[0].options.map((item, index) => (

                            <li class="footer-link-wrapper" key={index}>
                                <NavLink to={item.url} class="footer-link" target="_self" role="menuitem">  {item.name} </NavLink>
                            </li>
                        ))}
                    </ul>
            </div>

                </div>
            </div>
    </div>
    </footer>
  )
}
