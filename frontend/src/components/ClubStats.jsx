import axios from "axios"
import { useEffect, useState } from "react"
import { TopClubFilteringStats } from "./TopClubFilteringStats"
import { NATIONALITY_LIST } from "../nationality"
import { IP } from "../CREDENTIALS"

export const ClubStats = () => {


    const [seasonIndex, setSeasonIndex] = useState(-1) // the id which is season_id for filtering
    const [actionIndex, setActionIndex] = useState(0) // the id which is season_id for filtering

    const [order, setOrder] = useState(true) 
    const [chosenActionName, setChosenActionName] = useState("Goal")
    const [fromNumber, setFromNumber] = useState(1)

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
            const response = await axios.get(`http://${IP}:8000/api/stats/top/club?at=${chosenActionName.toLowerCase()}&se=${seasonIndex}&from=${fromNumber}&order=${order?"desc":"asc"}`) // is not complited yet
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
                chosenActionName={chosenActionName}
                setChosenActionName={setChosenActionName}
            />


            <div className="table playerIndex statsTable teamStatsTable stats-table">
                <h1 className="stats-table__header">{chosenActionName}s</h1>
                <table>

                    <thead>
                        <tr>
                            <th className="stats-table__header-rank" scope="col">Rank</th>
                            <th scope="col">Club</th>
                            <th scope="col" className="stats-table__header-stat">Stat</th>
                            <th className="table__order">
                                <span className="table__reorder-stats-button js-reorder-stats-button">
                                    <span className="icn sort"></span>
                                </span>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="statsTableContainer">
                        {clubs.length > 0&& clubs.map((club, index) => (
                        
                        <tr className="table__row " key={index}>
                            <td className="stats-table__rank">{index + 1}.</td>
                            <td className="stats-table__name">
                                <a href="//www.premierleague.com/clubs/1/club/overview" className="stats-table__cell-icon-align">
                                    <span className="badge badge-image-container" data-widget="club-badge-image" data-size="25">
                                        <img className="badge-image badge-image--25 js-badge-image" src={`http://${IP}:8000${club.logo}`} alt="logo"/>
                                    </span>
                                    {club.name}
                                </a>
                            </td>
                            <td className="stats-table__main-stat">
                                {club.stats}
                            </td>
                            <td>&nbsp;</td>
                        </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
