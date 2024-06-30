import axios from "axios"
import { useEffect, useState } from "react"
import { TopPlayerFilteringStats } from "./TopPlayerFilteringStats"
import { NATIONALITY_LIST } from "../nationality"

export const PlayerStats = () => {


    const [actionIndex, setActionIndex] = useState(1) // the id which is season_id for filtering
    const [seasonIndex, setSeasonIndex] = useState(1) // the id which is season_id for filtering
    const [clubIndex, setClubIndex] = useState(-1) // the id which is sample_club_id for filtering
    const [nationalityIndex, setNationalityIndex] = useState(-1) // the id which is season_id for filtering
    const [positionIndex, setPositionIndex] = useState(0) // the id which is season_id for filtering

    const [players, setPlayers] = useState([])

    const positions = [
        { name: 'All Positions', key: -1 },
        { name: 'Goalkeeper', key: 'GK' },
        { name: 'Defender', key: 'DF' },
        { name: 'Midfielder', key: 'MF' },
        { name: 'Forward', key: 'FW' }
    ]

    const fetchData = async () => {
        console.log("repeat fetching data...")
        try {
            console.log(`season is ${seasonIndex} and club is ${clubIndex}`)
            const response = await axios.get(`http://127.0.0.1:8000/api/stats/top/player?at=penalties&se=${-1}&cl=${-1}&na=${-1}&po=${-1}`)
            console.log("stats player: ")
            console.log(response.data)
            setPlayers(response.data)
        } catch (error) {
            console.log("Error fetching players!", error)
        }
    }

    useEffect(() => {

        fetchData()
    }, [actionIndex, clubIndex, seasonIndex, nationalityIndex, positionIndex])






    return (
        <>


            <TopPlayerFilteringStats
                handelActionIndex={setActionIndex}
                handelSeasonIndex={setClubIndex}
                handelClubIndex={setSeasonIndex}
                handelPositionIndex={setPositionIndex}
                hadelNationalityIndex={setNationalityIndex}
                positions={positions}
            />


            <div className="table statsTable stats-table">
                <h1 className="stats-table__header">Goals</h1>
                <table>

                    <thead>
                        <tr>
                            <th className="stats-table__header-rank" scope="col">Rank</th>
                            <th scope="col">Player</th>
                            <th className="hide-s" scope="col">Club</th>
                            <th className="hide-s" scope="col">Nationality</th>
                            <th scope="col">Stat</th>
                            <th className="table__order">
                                <span className="table__reorder-stats-button js-reorder-stats-button">
                                    <button className="icn sort"></button>
                                </span>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="stats-table__container statsTableContainer">

                        {
                         players && players.map((player, index) => {
                            <tr class="table__row ">
                                <td class="stats-table__rank">1.</td>
                                <td class="stats-table__player">
                                    <a href="//www.premierleague.com/players/65970/player/overview" class="playerName">  Erling Haaland</a>
                                </td> <td class="hide-s">
                                    <a href="//www.premierleague.com/clubs/11/Manchester-City/overview" class="stats-table__cell-icon-align">
                                        <span class="badge badge-image-container" data-widget="club-badge-image" data-size="25">
                                            <img class="badge-image badge-image--25 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/25/t43.png" />
                                        </span>Manchester City
                                    </a>
                                </td>
                                <td class="hide-s">
                                    <div class="stats-table__cell-icon-align">
                                        <img class="stats-table__flag-icon" src="https://resources.premierleague.com/premierleague/flags/NO.png" />
                                        <span class="playerCountry">Norway</span>
                                    </div>
                                </td>
                                <td class="stats-table__main-stat">27</td>
                                <td>&nbsp;</td>
                            </tr>

                         })   
                        }
                    </tbody>
                </table>
            </div>
        </>
    )
}
