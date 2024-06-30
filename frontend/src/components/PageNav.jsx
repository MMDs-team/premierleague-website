import React, { useState } from 'react'
import {NavLink} from 'react-router-dom'


export const PageNav = ({menu, tabHandler}) => {

    const [idx, setIdx] = useState(0)


    const handler = (index) => {
        setIdx(index)
        return tabHandler(index)
    }

  return (
    <>
    <header className="page-header page-header--stats">
    
    </header>
          <nav className="generic-tabs-nav generic-tabs-nav--page-header wrapper  "
                  data-widget="generic-tabs-nav" data-script="pl_tabs" >
              <ul className="tablist generic-tabs-nav__nav" role="tablist">
    
                {
                  menu.map((oprion, index) => (
    
                          <li className={index===idx?"tab generic-tabs-nav__tab is-active":"tab generic-tabs-nav__tab"} key={index} onClick={() => handler(index)}>
                              <NavLink to={oprion.link} data-text="Dashboard" className={index===idx?"generic-tabs-nav__link is-active":"generic-tabs-nav__link"} data-link-index="0" role="tab">
                                  {oprion.name}
                              </NavLink>
                          </li>
                  ))
                }
                </ul>
          </nav>
    </>
  )
}
