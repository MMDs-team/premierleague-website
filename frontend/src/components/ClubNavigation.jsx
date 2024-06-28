import React, { useContext, useEffect } from 'react';
import {ThisSeasonClubs} from '../App.js'



export const ClubNavigation = () => {

    const clubs = useContext(ThisSeasonClubs)

    return (


        <nav className="clubNavigation js-club-navigation" data-script="pl_global-header" role="menubar">
            <h4 className="clubSitesHeading">
                Club Sites
            </h4>

            <ul className="clubList" role="menu">

                {clubs && clubs.map((club, i) => (
                    
                    <li className="clubList__club" key={i}>
                        <a className="clubList__link" target="_blank" href={club.website} role="menuitem">
                            <div className="badge badge--large badge-image-container" data-widget="club-badge-image" data-size="50">
                                <img className="badge-image badge-image--50 js-badge-image" src={`http://127.0.0.1:8000/${club.logo}`} alt='club_logo'/>
                                <span className="visuallyHidden">{club.name}</span>
                            </div>
                            <span className="name">{club.name}</span>
                        </a>
                    </li>

                ))}
                    
            </ul>
        </nav>
    )
}