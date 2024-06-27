import React, { useState } from 'react'
import { NavLink } from 'react-router-dom'



export const MainNav = (props) => {

    let lists = props.lists

    const [activeIndex, setActiveIndex] = useState(0)
    const [activeMainIndex, setActiveMainIndex] = useState(0)
    

    return (
        <nav className="mainNav">
            <ul className="pageLinks js-page-links" role="menu">
                {lists.map((option, i) => (
                    
                    <li className=" premierleague"tabIndex="0" aria-haspopup="true" role="menuitem" key={i}>
                            <div role="button" 
                                className={activeMainIndex === i?"navLink active":"navLink"} 
                                tabIndex="index"
                                onClick={() => setActiveMainIndex(i)}
                                >
                                <span className="navText">Premier League</span>
                                    <span className="chevron-dropdown"></span>
                            </div>

                            <div className="dropdown " aria-hidden="true">
                                <ul role="menu">
                                    {option.options.map((op, index) => (
                                        <li tabIndex="-1" key={index}>
                                            <NavLink tabIndex="0" 
                                                className={index === activeIndex?"active":""} 
                                                to={op.url}
                                                role="menuitem"
                                                onClick={() => setActiveIndex(index)}
                                            >
                                                {op.name}
                                            </NavLink>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                    </li>


                ))}

            </ul>
        </nav>
  )
}
