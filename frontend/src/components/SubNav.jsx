import React from 'react'

export const SubNav = () => {
  return (
    
    <nav className="subNav js-sub-nav" role="menubar">
        <ul>
            <li><a href="/" className ="  active" data-link-index="0" role="menuitem">Home</a></li>
            <li><a href="/fixtures" className ="  " data-link-index="1" role="menuitem">Fixtures</a></li>
            <li><a href="/results" className ="  " data-link-index="2" role="menuitem">Results</a></li>
            <li><a href="/tables" className ="  " data-link-index="3" role="menuitem">Tables</a></li>
            <li><a href="/transfers" className ="  " data-link-index="4" role="menuitem">Transfers</a></li>
            <li><a href="/stats" className =" hideNavDropdown " data-link-index="5" role="menuitem">Stats</a></li>
            <li><a href="/tickets" className ="  " data-link-index="9" role="menuitem">Tickets</a></li>
            <li><a href="/clubs" className ="  " data-link-index="10" role="menuitem">Clubs</a></li>
            <li><a href="/players" className ="  " data-link-index="11" role="menuitem">Players</a></li>
            <li><a href="/awards" className ="  " data-link-index="12" role="menuitem">Awards</a></li>
        </ul>
    </nav>
  )
}
