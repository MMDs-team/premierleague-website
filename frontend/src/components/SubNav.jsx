import React, { useEffect, useState } from 'react'
import {NavLink} from 'react-router-dom'

export const SubNav = (props) => {

    let options = props.options

    const [activeIndex, setActiveIndex] = useState(0)

    useEffect(() => {
        console.log(activeIndex)
    }, [activeIndex])
    
  return (
    
    <nav className="subNav js-sub-nav" role="menubar">
        <ul>
            {options.map((option, index) => (
                <li key={index}>
                    <NavLink  to={option.url} 
                        className={index === activeIndex?"active":""} 
                        data-link-index={index} 
                        role="menuitem"
                        onClick={() => setActiveIndex(index)}
                        >

                        {option.name}

                    </NavLink>
                </li>
            ))}
        </ul>
    </nav>
  )
}
