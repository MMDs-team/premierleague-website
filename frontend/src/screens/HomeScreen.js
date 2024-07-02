import React, { useContext, useEffect, useState } from 'react'
import { MainContext } from '../App'
import axios from 'axios'



const HomeScreen = () => {

  const [fixtures, setFixtures] = useState([])


    

  const fetchData = async () => {
      try {
          const response = await axios.get(`http://127.0.0.1:8000/api/overview/fixtures?s_cl=-1`)
          setFixtures(response.data)
      } catch (error) {
          console.log("Error fetching fixtures!", error)
      }

      
  }

  useEffect(() => {
      fetchData();
  },[])


  const { heroNameHandler } = useContext(MainContext)

  heroNameHandler("Home")

  return (
    <div className='mainContent'>

      <div class="wrapper hasFixedSidebar">
        <div class="tabbedHome">
          <nav class="fixedSidebar" data-ui-tab="Matches">

            <div class="fixtures-abridged-header fixtures-abridged-header--comp-1  ">
              <div class="fixtures-abridged-header__header">

                <img alt="2024/25" class="fixtures-abridged-header__competition-image " src="https://resources.premierleague.com/premierleague/competitions/competition_1_small.png" />
                <div class="fixtures-abridged-header__title">
                  Matchweek 1
                </div>
              </div>
              <div class="fixtures-abridged-header__local-time">
                All times shown are your  <span class="bold">local time</span>
              </div>

              <div class="fixtures-abridged   calendar " data-fixturesids="115827,115830,115828,115829,115831,115832,115833,115834,115835,115836" data-script="pl_club" data-widget="club-matches" data-pagesize="10" data-sort="ASCENDING" data-gameweek="18390" data-start-date="2024-08-16" data-end-date="2024-08-19" data-rendered="true">
                        {fixtures.length > 0 && fixtures.slice(0, Math.min(2, fixtures.length)).map((fixt, index) => (

                <div class="fixtures-abridged__list js-match-list-container">
                  <div class="fixtures-abridged__day-container ">
                    <time class="fixtures-abridged__date"> {fixt.date}
                    </time>


                            {fixt.matches.map((match, ind) => (


                                <a href="//www.premierleague.com/match/115827" class="match-fixture match-fixture--abridged " data-matchid="115827">
                                  <div class="match-fixture__team match-fixture__team--home">
                                    <span class="match-fixture__team-name match-fixture__team-name--abbr u-hide-phablet">{match.host_club.name.slice(0,3).toUpperCase()}
                                    </span>
                                    <span class="match-fixture__team-name match-fixture__team-name--full u-show-phablet">{match.host_club.name}
                                    </span>
                                    <span class="badge badge-image-container" data-widget="club-badge-image" data-size="50">
                                      <img class="badge-image badge-image--30 js-badge-image" src={`http://127.0.0.1:8000${match.host_club.logo}`} />
                                    </span>
                                  </div>
                                  <time>{match.time.slice(0,5)}
                                  </time>
                                  <div class="match-fixture__team match-fixture__team--away">
                                    <span class="badge badge-image-container" data-widget="club-badge-image" data-size="50">
                                      <img class="badge-image badge-image--30 js-badge-image" src={`http://127.0.0.1:8000${match.guest_club.logo}`} />
                                    </span>
                                    <span class="match-fixture__team-name match-fixture__team-name--abbr u-hide-phablet">{match.guest_club.name.slice(0,3).toUpperCase()}}
                                    </span>
                                    <span class="match-fixture__team-name match-fixture__team-name--full u-show-phablet">{match.guest_club.name}
                                    </span>
                                  </div>
                                  <div data-id="115827" class="match-fixture__summary-broadcasters js-match-summary-broadcasters">
                                  </div>
                                  <svg class="match-fixture__icon" xmlns="http://www.w3.org/2000/svg" xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15.085 9.422" space="preserve">
                                    <path d="M15.084,4.709c-0.013-0.285-0.106-0.581-0.325-0.782l-1.215-1.216l-1.941-1.94l-0.445-0.446 c-0.21-0.204-0.489-0.32-0.782-0.325c-0.271,0-0.595,0.12-0.781,0.325C9.403,0.536,9.259,0.812,9.27,1.107 c0.012,0.294,0.112,0.569,0.325,0.781l1.218,1.218l0.495,0.496H2.69c-0.519,0-1.041-0.006-1.56,0H1.107 c-0.285,0-0.58,0.124-0.781,0.326C0.133,4.12-0.01,4.432,0.001,4.709C0.014,4.993,0.107,5.29,0.326,5.49 c0.218,0.2,0.484,0.326,0.781,0.325h10.207L10.04,7.088L9.595,7.533c-0.2,0.2-0.324,0.5-0.325,0.782c0,0.271,0.12,0.595,0.325,0.781 c0.21,0.192,0.486,0.337,0.782,0.325c0.292-0.015,0.57-0.113,0.781-0.325l1.218-1.218l1.941-1.941l0.445-0.445 c0.114-0.113,0.194-0.248,0.247-0.392c0.052-0.124,0.078-0.258,0.076-0.392L15.084,4.709z">
                                    </path>
                                  </svg>
                                </a>


                            ))}




                    <a class="match-fixture__mc-button global-btn" href="//www.premierleague.com/match/115827"> View match centre
                      <svg class="match-fixture__icon icn" xmlns="http://www.w3.org/2000/svg" xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15.085 9.422" space="preserve">
                        <path d="M15.084,4.709c-0.013-0.285-0.106-0.581-0.325-0.782l-1.215-1.216l-1.941-1.94l-0.445-0.446 c-0.21-0.204-0.489-0.32-0.782-0.325c-0.271,0-0.595,0.12-0.781,0.325C9.403,0.536,9.259,0.812,9.27,1.107 c0.012,0.294,0.112,0.569,0.325,0.781l1.218,1.218l0.495,0.496H2.69c-0.519,0-1.041-0.006-1.56,0H1.107 c-0.285,0-0.58,0.124-0.781,0.326C0.133,4.12-0.01,4.432,0.001,4.709C0.014,4.993,0.107,5.29,0.326,5.49 c0.218,0.2,0.484,0.326,0.781,0.325h10.207L10.04,7.088L9.595,7.533c-0.2,0.2-0.324,0.5-0.325,0.782c0,0.271,0.12,0.595,0.325,0.781 c0.21,0.192,0.486,0.337,0.782,0.325c0.292-0.015,0.57-0.113,0.781-0.325l1.218-1.218l1.941-1.941l0.445-0.445 c0.114-0.113,0.194-0.248,0.247-0.392c0.052-0.124,0.078-0.258,0.076-0.392L15.084,4.709z">
                        </path>
                      </svg> 
                      </a>       
                      </div>
                </div>
                        ))}

              </div>

            </div>
          </nav>

        </div>
      </div>





    </div>
  )
}

export default HomeScreen