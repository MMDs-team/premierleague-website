import axios from "axios"
import { useEffect, useState } from "react"
import { TopClubFilteringStats } from "./TopClubFilteringStats"
import { NATIONALITY_LIST } from "../nationality"

export const ClubStats = () => {


    const [seasonIndex, setSeasonIndex] = useState(1) // the id which is season_id for filtering
    const [actionIndex, setActionIndex] = useState(1) // the id which is season_id for filtering


    const [clubs, setClubs] = useState([])

    const postions = [
        { name: 'All Positions', key: -1 },
        { name: 'Goalkeeper', key: 'GK' },
        { name: 'Defender', key: 'DF' },
        { name: 'Midfielder', key: 'MF' },
        { name: 'Forward', key: 'FW' }
    ]

    const fetchData = async () => {
        console.log("repeat fetching data...")
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/stats/top/club?at=yellow_cards&se=-1`) // is not complited yet
            console.log("stats clubs: ")
            console.log(response.data)
            setClubs(response.data)
        } catch (error) {
            console.log("Error fetching clubs!", error)
        }
    }

    useEffect(() => {

        fetchData()
    }, [actionIndex, seasonIndex])






    return (
        <>


            <TopClubFilteringStats
                handelActionIndex={setActionIndex}
                handelSeasonIndex={setSeasonIndex}
            />


<div class="table playerIndex statsTable teamStatsTable stats-table">
                <h1 class="stats-table__header">Wins</h1>
                <summary class="visuallyHidden">This table ranks teams based on the currently selected stat type</summary><table>

                    <thead>
                        <tr>
                            <th class="stats-table__header-rank" scope="col">Rank</th>
                            <th scope="col">Club</th>
                            <th scope="col" class="stats-table__header-stat">Stat</th>
                            <th class="table__order">
                                <span class="table__reorder-stats-button js-reorder-stats-button">
                                    <span class="icn sort"></span>
                                </span>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="statsTableContainer">
                        <tr class="table__row ">
                            <td class="stats-table__rank">1.</td>
                            <td class="stats-table__name">
                                <a href="//www.premierleague.com/clubs/1/club/overview" class="stats-table__cell-icon-align">
                                    <span class="badge badge-image-container" data-widget="club-badge-image" data-size="25">
                                        <img class="badge-image badge-image--25 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/25/t3.png" />
                                    </span>
                                    Arsenal
                                </a>
                            </td>
                            <td class="stats-table__main-stat">
                                28
                            </td>
                            <td>&nbsp;</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </>
    )
}
