import React, { useContext, useEffect, useState } from 'react'
import { MainContext } from '../App'

export const TopClubFilteringStats = (props) => {

    const handelActionIndex = props.handelActionIndex
    const handelSeasonIndex = props.handelSeasonIndex

    const clubs = useContext(MainContext).clubs
    const seasonOrdered = useContext(MainContext).seasonOrdered
    const actionTypes = useContext(MainContext).actionTypes

    const [chosenActionName, setChosenActionName] = useState("Goal")
    const [chosenSeasonName, setChosenSeasonName] = useState("All Seasons")
    const [isSeasonFilterOpen, setIsSeasonFilterOpen] = useState(false)
    const [isActionFilterOpen, setIsActionFilterOpen] = useState(false)
    const [isMobileFilter, setIsMobileFilter] = useState(false)


    const choseFilter = (index, name, type) => {
        if (type === 'Action') {
            handelActionIndex(index)
            setChosenActionName(name)
        }  else if (type === 'Season') {
            handelSeasonIndex(index)
            setChosenSeasonName(name)
        } else {          
            handelSeasonIndex()
            setChosenSeasonName("All Seasons")
            setChosenActionName("Goal")
        }
    }



    useEffect(() => {
        if (isMobileFilter) {
            document.body.className = "nav-fixed u-body-no-scroll"
        } else {
            document.body.className = "nav-fixed"
        }

    }, [isMobileFilter])



  return (
    
    
        <section className={isMobileFilter?"pageFilter col-12 fixture-page-filter open":"pageFilter col-12 fixture-page-filter"} 
                    data-widget="results-filtered-list-filter" 
                    data-reset-available="true" 
                    data-use-basic-history="true"
                    >
    
            <header className="mobileHeader js-mobile-header" >
                <h4>Filters</h4>
                <button className="close" onClick={() => setIsMobileFilter(false)}>
                    Cancel
                    <svg width="15" height="15" viewBox="0 0 15 15" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M13.878.304a.98.98 0 0 0-1.418 0L7.09 5.673 1.723.303a.98.98 0 0 0-1.418 0 .98.98 0 0 0 0 1.42L5.673 7.09.303 12.46a.98.98 0 0 0 0 1.418c.203.203.406.304.71.304.304 0 .506-.101.71-.304L7.09 8.509l5.369 5.369c.202.203.506.304.709.304.202 0 .506-.101.709-.304a.98.98 0 0 0 0-1.418L8.509 7.09l5.369-5.368a.98.98 0 0 0 0-1.418z"
                            fillRule="evenodd"></path>
                    </svg>
                </button>
            </header>


                        
            <div className={isActionFilterOpen?"dropDown mobile open":"dropDown mobile"} data-dropdown-block="teams" data-dropdown-default="Goals"
                data-listen-keypress="true" data-listen-click="true" onClick={() => setIsActionFilterOpen(!isActionFilterOpen)}>
                <div className="label js-dropdown-label" id="dd-teams">
                    <span className="u-hide-tablet"> Filter by Actions </span>
                    <span className="u-show-tablet"> Filter by Actions </span>
                </div>
                <div className="current" data-dropdown-current="teams" role="button" tabIndex="0"
                    aria-expanded={isActionFilterOpen?"true":"false"} aria-labelledby="dd-teams">
                    {chosenActionName}s
                </div>
                <div className="dropdownListContainer">
                    <header className="dropdownMobileHeader">
                        <button className="dropdownMobileHeaderButton js-dropdown-close"
                            data-listen-keypress="true" data-listen-click="true">
                            <svg width="16" height="10" viewBox="0 0 16 10" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path fillRule="evenodd" clipRule="evenodd"
                                    d="M0.926016 5.01732C0.938708 4.74167 1.02892 4.45424 1.24084 4.2603C1.24115 4.2603 1.24146 4.25999 1.24177 4.25968L2.41825 3.0832L4.2987 1.20275L4.72967 0.771778C4.92345 0.577997 5.21305 0.458021 5.48669 0.456956C5.74963 0.456976 6.06328 0.573122 6.24376 0.771893C6.42982 0.975935 6.56952 1.24307 6.55869 1.52896C6.54662 1.81361 6.4499 2.07995 6.24387 2.28598L5.06429 3.46556L4.58402 3.94583L6.21051 3.9458C7.41328 3.94589 8.61854 3.94598 9.82007 3.94607C10.8582 3.94615 11.8938 3.94623 12.9329 3.9463C13.4355 3.94634 13.9419 3.94018 14.4445 3.94642L14.4662 3.94642C14.7425 3.94644 15.0278 4.06584 15.2233 4.26135C15.4099 4.44803 15.5486 4.75006 15.5382 5.01842C15.5257 5.29392 15.4355 5.58166 15.2234 5.77544C15.0116 5.96922 14.7541 6.09091 14.4664 6.09026L13.2214 6.09017L10.2539 6.0901L6.64415 6.08967C5.95579 6.08962 5.26743 6.08957 4.57938 6.08952L5.8131 7.32324L6.24444 7.75458C6.43825 7.94839 6.55811 8.23785 6.55938 8.51165C6.55924 8.77443 6.44314 9.08806 6.2444 9.26851C6.04038 9.45454 5.77342 9.59436 5.48753 9.58349C5.20413 9.56889 4.93575 9.47384 4.73047 9.26855L3.55055 8.08864L1.66997 6.20806L1.23878 5.77687C1.12916 5.66725 1.05132 5.5367 1.00031 5.39701C0.95115 5.27282 0.921219 5.14181 0.926016 5.01732Z">
                                </path>
                            </svg>
                            <span>Back</span>
                        </button>
                        <h4>Filter by Actions</h4>
                    </header>
                    <ul className="dropdownList" data-dropdown-list="teams" role="listbox" aria-labelledby="dd-teams" data-listen-keypress="true" data-listen-click="true">
                        {/* the other clubs (action) */}
                        { actionTypes && actionTypes.map((at, index) => (

                            <li key={index} 
                                role="option" 
                                aria-selected='true' 
                                tabIndex={index} 
                                data-option-name={index} 
                                data-option-id={index} 
                                data-option-index={index} 
                                className=""
                                onClick={() => choseFilter(index, at.subtype, "Action")}>

                                {at.subtype}s
                         
                            </li>
                        ))}
                    </ul>
                </div>
            </div>


            <div className={isSeasonFilterOpen?"dropDown mobile open":"dropDown mobile"} data-dropdown-block="compSeasons" data-dropdown-default=""
            data-listen-keypress="true" data-listen-click="true"  onClick={() => setIsSeasonFilterOpen(!isSeasonFilterOpen)}>
            <div className="label js-dropdown-label" id="dd-compSeasons"> Filter by Season </div>
            <div className="current" data-dropdown-current="compSeasons" role="button" tabIndex="0" aria-expanded={isSeasonFilterOpen?"true":"false"}
                aria-labelledby="dd-compSeasons">
                    {
                        chosenSeasonName==="Season"? (seasonOrdered.length>0? seasonOrdered[0].date : "Season") :chosenSeasonName

                    }
            </div>
            <div className="dropdownListContainer">
                <header className="dropdownMobileHeader"> <button className="dropdownMobileHeaderButton js-dropdown-close"
                        data-listen-keypress="true" data-listen-click="true"> <svg width="16" height="10"
                            viewBox="0 0 16 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" clipRule="evenodd"
                                d="M0.926016 5.01732C0.938708 4.74167 1.02892 4.45424 1.24084 4.2603C1.24115 4.2603 1.24146 4.25999 1.24177 4.25968L2.41825 3.0832L4.2987 1.20275L4.72967 0.771778C4.92345 0.577997 5.21305 0.458021 5.48669 0.456956C5.74963 0.456976 6.06328 0.573122 6.24376 0.771893C6.42982 0.975935 6.56952 1.24307 6.55869 1.52896C6.54662 1.81361 6.4499 2.07995 6.24387 2.28598L5.06429 3.46556L4.58402 3.94583L6.21051 3.9458C7.41328 3.94589 8.61854 3.94598 9.82007 3.94607C10.8582 3.94615 11.8938 3.94623 12.9329 3.9463C13.4355 3.94634 13.9419 3.94018 14.4445 3.94642L14.4662 3.94642C14.7425 3.94644 15.0278 4.06584 15.2233 4.26135C15.4099 4.44803 15.5486 4.75006 15.5382 5.01842C15.5257 5.29392 15.4355 5.58166 15.2234 5.77544C15.0116 5.96922 14.7541 6.09091 14.4664 6.09026L13.2214 6.09017L10.2539 6.0901L6.64415 6.08967C5.95579 6.08962 5.26743 6.08957 4.57938 6.08952L5.8131 7.32324L6.24444 7.75458C6.43825 7.94839 6.55811 8.23785 6.55938 8.51165C6.55924 8.77443 6.44314 9.08806 6.2444 9.26851C6.04038 9.45454 5.77342 9.59436 5.48753 9.58349C5.20413 9.56889 4.93575 9.47384 4.73047 9.26855L3.55055 8.08864L1.66997 6.20806L1.23878 5.77687C1.12916 5.66725 1.05132 5.5367 1.00031 5.39701C0.95115 5.27282 0.921219 5.14181 0.926016 5.01732Z">
                            </path>
                        </svg> <span>Back</span> </button>
                    <h4> Filter by Season</h4>
                </header>
                <ul className="dropdownList" data-dropdown-list="compSeasons" role="listbox"
                    aria-labelledby="dd-compSeasons" data-listen-keypress="true" data-listen-click="true">

                        {seasonOrdered.map((season, index) => (
                            <li key={index}
                                role="option" 
                                aria-selected
                                tabIndex={season.season_id}
                                data-option-name={season.date}
                                data-option-id={season.season_id}
                                data-option-index={season.season_id}
                                className=""
                                onClick={() => choseFilter(season.season_id,season.date,"Season")}> 
                                    {season.date}
                            </li>
                        ))

                        }
                </ul>
            </div>
            </div>
  

            <div className="pageFilter__container">
                <div className="pageFilter__filter-btn" tabIndex="0" role="button" onClick={() => setIsMobileFilter(true)}>
                    Filter
                </div>
                <div className="global-btn filter-button filter-button--apply" role="button" tabIndex="0" onClick={() => setIsMobileFilter(false)}>
                    Apply Filters
                </div>
                <div className="global-btn filter-button filter-button--reset js-reset-button" 
                    role="button" 
                    tabIndex="0" 
                    onClick={() => choseFilter(-1, "All", "All")}>
                    <span className="filter-button__text" >Reset Filters</span>
                </div>
            </div>
            <div className="filter-button filter-button--reset u-hide-desktop" 
                role="button" 
                tabIndex="0" 
                onClick={() => choseFilter(-1, "All", "All")}>

                <div className="filter-button__icon">
                    <svg width="24" height="21" viewBox="0 0 24 21" fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd" clipRule="evenodd"
                            d="M14.0796 0.5C8.60097 0.5 4.15932 5.06693 4.15932 10.7C4.15932 11.3213 4.219 11.9261 4.32237 12.5167L0.878126 8.97313L0 9.87602L4.9608 14.9767L4.964 14.9723L5.39987 15.4216L5.83468 14.9723L5.83788 14.9767L10.7987 9.87602L9.92055 8.97313L5.76018 13.2531C5.52147 12.4291 5.39999 11.5733 5.39999 10.7C5.39999 5.77801 9.29301 1.77548 14.0798 1.77548C18.8665 1.77548 22.7595 5.77829 22.7595 10.7C22.7595 15.6218 18.8665 19.6246 14.0798 19.6246V20.9C19.5584 20.9 24 16.3331 24 10.7C24 5.0669 19.5584 0.5 14.0798 0.5">
                        </path>
                    </svg>
                </div>
                <span className="filter-button__text" >Reset Filters</span>

            </div>
        </section>

  )
}
