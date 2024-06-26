import React from 'react'



export const MainNav = (props) => {

    let lists = props.lists
    

    return (
        <nav className="mainNav">
            <ul className="pageLinks js-page-links" role="menu">
                {lists.map((option, i) => (
                    
                    <li className=" premierleague"tabIndex="0" aria-haspopup="true" role="menuitem" key={i}>
                            <div role="button" className="navLink active  " tabIndex="index">
                                <span className="navText">Premier League</span>
                                    <span className="chevron-dropdown"></span>
                            </div>

                            <div className="dropdown " aria-hidden="true">
                                <ul role="menu">
                                    {option.options.map((op, index) => (
                                        <li tabIndex="-1" key={index}>
                                            <a tabIndex="0" className="" href="/" role="menuitem">
                                            Home
                                            </a>
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
