import React from 'react'
import { IP } from '../CREDENTIALS'

export const TableMatchRow = (props) => {

    const {club_id, name, logo, played, won, drawn, lost, goal, goal_conCeded, goal_difference, point, last_matches} = props.data
    const {idx} = props

    return (

        <tr className="tableDark" data-compseason="578" data-position="1" data-filtered-entry-size="20" data-filtered-table-row="11" data-filtered-table-row-name="Manchester City" data-filtered-table-row-abbr="MCI">
            <td className="league-table__pos pos button-tooltip" tabindex="0" id="Tooltip">
                <span className="league-table__value value">{idx+1} </span>
                <span className="league-table__movement none">
                    <span className="league-table__tooltip-container tooltipContainer tooltip-left" role="tooltip">
                        <span className="league-table__tooltip-content tooltip-content">Previous Position
                            <span className="league-table__result-highlight">
                            </span>
                        </span>
                    </span>
                </span>
            </td>
            <td className="league-table__team team" scope="row">
                <a href="//www.premierleague.com/clubs/11/Manchester-City/overview">
                    <span className="badge badge-image-container" data-widget="club-badge-image" data-size="50">
                        <img className="badge-image badge-image--32 js-badge-image" src={`http://${IP}:8000${logo}`}  />
                    </span>
                    <span className="league-table__team-name league-table__team-name--long long">{name}</span>
                    <span className="league-table__team-name league-table__team-name--short short">{name.slice(0,3).toUpperCase()}</span>       {/*the short form for club -------------------------------------------------------*/}
                </a>
            </td>
            <td>{played}</td> 
            <td>{won}</td>
            <td>{drawn} </td>
            <td>{lost}</td>
            <td className="hideSmall">{goal}</td>
            <td className="hideSmall">{goal_conCeded} </td>
            <td>{goal_difference} </td>
            <td className="league-table__points points">{point}</td>
            <td className="league-table__form form hideMed">
                <ul>    {console.log("last_matches", last_matches)}
                    {   
                        last_matches.length > 0 && last_matches.map((match, index) => (

                            <li tabindex="0" className={match[0]>match[3] ? 'win button-tooltip' : match[0] < match[3] ? 'lose button-tooltip' : 'draw button-tooltip'} id="Tooltip" key={index}>
                                <abbr title="Won" className="form-abbreviation">{match[0]>match[3] ? 'W' : match[0] < match[3] ? 'L' : 'D'}
                                </abbr>
                                <a href="//www.premierleague.com/match/93667" className="tooltipContainer linkable tooltip-link tooltip-right" role="tooltip">
                                    <span className="tooltip-content">
                                        <div className="match-fixture match-fixture--small">
                                            <span className="match-fixture__match-info matchInfo"> {/* the date need----------------------------------------------------------------< */}
                                            </span>
                                            <div className="match-fixture__team-score-container">
                                                <div className="match-fixture__team match-fixture__team--home">
                                                    <span className="atch-fixture__team-name"> {match[1].slice(0,3).toUpperCase()} </span>    {/*the short form for club -------------------------------------------------------*/}
                                                    <span className="badge badge--home-team badge-image-container" data-widget="club-badge-image" data-size="50">
                                                        <img className="badge-image badge-image--30 js-badge-image" src={`http://${IP}:8000${match[2]}`} />
                                                    </span>
                                                </div>
                                                <span className="match-fixture__score score"> {match[6]} </span>
                                                <div className="match-fixture__team match-fixture__team--home">
                                                    <span className="badge badge--away-team badge-image-container" data-widget="club-badge-image" data-size="50">
                                                        <img className="badge-image badge-image--30 js-badge-image" src={`http://${IP}:8000${match[5]}`}  />
                                                    </span>
                                                    <span className="match-fixture__team-name"> {match[4].slice(0,3).toUpperCase()} </span>   {/*the short form for club -------------------------------------------------------*/}
                                                </div>
                                                <span className="icn arrow-right">
                                                </span>
                                            </div>
                                        </div>
                                    </span>
                                </a>
                            </li>
                        ))
                    }
                </ul>
            </td>
        </tr>
    )
}
