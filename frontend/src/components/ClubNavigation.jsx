import React from 'react';

import clubLogo from '../static/images/clubImage.png'

export const ClubNavigation = () => {


    let clubs = [
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
    ]


    return (
        <nav className="clubNavigation js-club-navigation" data-script="pl_global-header" role="menubar">
            <h4 className="clubSitesHeading">
                Club Sites
            </h4>

            <ul className="clubList" role="menu">
                {clubs.map((club, i) => (
                    
                    <li className="clubList__club" key={i}>
                        <a className="clubList__link" target="_blank" href="/" role="menuitem">
                            <div className="badge badge--large badge-image-container" data-widget="club-badge-image" data-size="50">
                                <img className="badge-image badge-image--50 js-badge-image" src={clubLogo} alt='club_logo'/>
                                <span className="visuallyHidden">Arsenal</span>
                            </div>
                            <span className="name">Arsenal</span>
                        </a>
                    </li>

                ))}
                    
            </ul>
        </nav>
    )
}
