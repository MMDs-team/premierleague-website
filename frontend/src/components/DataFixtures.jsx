import React, { useEffect } from 'react'
import { IP } from '../CREDENTIALS';

export const DataFixtures = ({ fixtures }) => {


    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    const Days = ['Sunday', 'Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 'Friday', 'Saturday']; 


    useEffect(() => {
        console.log(fixtures)
        console.log("top was fixtures")
    }, [fixtures])

    return (

        <div className="col-12">
            <section className="fixtures">
                {
                    fixtures.length > 0 && fixtures.map((fixt, index) => (
                        
                        <div className="fixtures__date-container">
                            <div className="fixtures__date-content-container">
                                <time className="fixtures__date fixtures__date--long" datetime="Friday 16 August 2024">
                                    { fixt.date }
                                </time>
                                <time className="fixtures__date fixtures__date--short" datetime="Friday 16 August 2024">
                                    { fixt.date }
                                </time>
                            </div>

                            <div data-competition-matches-list="Friday 16 August 2024" className="fixtures__matches-list">
                                <ul className="matchList" data-comp-id="1">
                                    {
                                        fixt.matches.map((match, ind) => (
                                            <li className="match-fixture" data-home="Man Utd" data-away="Fulham"
                                                data-competition="Premier League" data-venue="Old Trafford, Manchester"
                                                data-comp-match-item="115827" data-comp-match-item-ko="1723834800000"
                                                data-comp-match-item-status="U">
                                                <div data-template-rendered=""
                                                    data-href="//www.premierleague.com/match/115827"
                                                    className="match-fixture__wrapper js-fixture preMatch" data-matchid="115827"
                                                    tabindex="0">
                                                    <span className="match-fixture__container">
                                                        <span className="match-fixture__teams">
                                                            <span className="match-fixture__team">
                                                                <span className="match-fixture__team-name">
                                                                    <span className="match-fixture__short-name">{match.host_club.name}</span>
                                                                    <span className="match-fixture__abbr">{match.host_club.name}</span>
                                                                </span>
                                                                <span className="badge badge-image-container"
                                                                    data-widget="club-badge-image" data-size="50">
                                                                    <img className="badge-image badge-image--32 js-badge-image"
                                                                        src={`http://${IP}:8000${match.host_club.logo}`} alt="host-logo"/>
                                                                </span>
                                                            </span>
                                                            <time datetime={match.time.slice(0,5)}>{match.time.slice(0,5)}</time>
                                                            <span className="match-fixture__team">
                                                                <span className="badge badge-image-container"
                                                                    data-widget="club-badge-image" data-size="50">
                                                                    <img className="badge-image badge-image--32 js-badge-image"
                                                                        src={`http://${IP}:8000${match.guest_club.logo}`} alt="gest-logo"/>
                                                                </span>
                                                                <span className="match-fixture__team-name">
                                                                    <span className="match-fixture__short-name">{match.guest_club.name}</span>
                                                                    <span className="match-fixture__abbr">{match.guest_club.name}</span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                        <span className="match-fixture__stadium-name">
                                                            <span className="match-fixture__stadium-icon">
                                                                <svg className="svg" width="16" height="11" viewBox="0 0 16 11"
                                                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                    <path fill-rule="evenodd" clip-rule="evenodd"
                                                                        d="M15.9846 6.419V6.88792L8.64637 10.3198V9.85089L15.9846 6.419ZM7.27558 9.09389L8.45642 9.84944V10.3098L7.27558 9.55034V9.09389ZM0 6.38323L5.05679 9.68344V10.1523L0 6.83811V6.38323ZM6.73304 9.08212V9.52922L5.33611 10.1523V9.70525L6.73304 9.08212ZM15.9846 5.2896V5.75851L8.64637 9.1904V8.72149L15.9846 5.2896ZM7.27558 7.96608L8.45642 8.72241V9.18274L7.27558 8.4233V7.96608ZM0 5.19779L5.05679 8.49724V8.96693L0 5.65189V5.19779ZM6.73304 7.89669V8.34378L5.33611 8.96691V8.51904L6.73304 7.89669ZM7.5566 0.166687L8.86323 1.02894L10.4778 0.288202L15.912 3.01601L14.2117 3.74974L16 4.61343L8.63254 7.98689L7.00484 6.88708L5.10085 7.78205L0.029439 4.45305L1.96198 3.6905L0.544977 2.84305L7.5566 0.166687ZM8.71869 1.84297L3.86501 3.82296L7.0618 5.71494L12.0467 3.61732L8.71869 1.84297ZM15.9992 3.55344V4.00054L15.621 4.16956L15.1502 3.932L15.9992 3.55344ZM0.544938 3.27306L1.26193 3.70847L0.775702 3.91177L0.54185 3.78091L0.544938 3.27306Z">
                                                                    </path>
                                                                </svg>
                                                            </span>
                                                            {`${match.stadium.name} ${match.stadium.city}`}
                                                        </span>
                                                        <div className="match-fixture__end-container">
                                                            <span
                                                                className="match-fixture__fixture-broadcast broadcastDataContainer"
                                                                data-id="115827"></span>
                                                            <span data-ui-modal="#quickviewModal"
                                                                data-ui-args='{"gameweek":{"id":18390,"compSeason":{"label":"2024/25","competition":{"abbreviation":"EN_PR","description":"Premier League","level":"SEN","source":"","id":1,"altIds":{"opta":"8"}},"id":719},"gameweek":1,"competitionPhase":{"id":7658,"type":"L","gameweekRange":[1,38]}},"kickoff":{"completeness":3,"millis":1723834800000,"label":"Fri 16 Aug 2024, 20:00 BST","gmtOffset":1},"provisionalKickoff":{"completeness":3,"millis":1723834800000,"label":"Fri 16 Aug 2024, 20:00 BST","gmtOffset":1},"teams":[{"team":{"name":"Manchester United","club":{"name":"Manchester United","shortName":"Man Utd","abbr":"MUN","id":12},"teamType":"FIRST","shortName":"Man Utd","id":12,"altIds":{"opta":"t1"}},"opta":"t1","clubBadge":"https://resources.premierleague.com/premierleague/badges/50/t1.png","clubBadgeRetina":"https://resources.premierleague.com/premierleague/badges/50/t1@x2.png","url":"//www.premierleague.com/clubs/12/Manchester-United/overview"},{"team":{"name":"Fulham","club":{"name":"Fulham","shortName":"Fulham","abbr":"FUL","id":34},"teamType":"FIRST","shortName":"Fulham","id":34,"altIds":{"opta":"t54"}},"opta":"t54","clubBadge":"https://resources.premierleague.com/premierleague/badges/50/t54.png","clubBadgeRetina":"https://resources.premierleague.com/premierleague/badges/50/t54@x2.png","url":"//www.premierleague.com/clubs/34/Fulham/overview"}],"replay":false,"ground":{"name":"Old Trafford","city":"Manchester","source":"OPTA","id":42},"neutralGround":false,"status":"U","phase":"0","fixtureType":"REGULAR","extraTime":false,"shootout":false,"goals":[],"penaltyShootouts":[],"behindClosedDoors":false,"id":115827,"altIds":{"opta":"g2444470"},"metadata":{},"matchDate":"Friday 16 August 2024","kickOffTime":"22:30","url":"//www.premierleague.com/match/115827"}'
                                                                className="global-btn global-btn--small match-fixture__quick-view js-quick-view-modal"
                                                                role="button" data-modal-active="true">Quick View</span>
                                                        </div>
                                                    </span>
                                                </div>
                                            </li>
               

                                        ))
                                    }
                                </ul>
                            </div>
                        </div>
                    ))
                }

            </section>
        </div>








    )
}
