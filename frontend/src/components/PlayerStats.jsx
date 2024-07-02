import axios from "axios"
import { useEffect, useState } from "react"
import { TopPlayerFilteringStats } from "./TopPlayerFilteringStats"
import { NATIONALITY_LIST } from "../nationality"
import { IP } from "../CREDENTIALS"

export const PlayerStats = () => {


    const [actionIndex, setActionIndex] = useState(0) // the id which is season_id for filtering
    const [seasonIndex, setSeasonIndex] = useState(-1) // the id which is season_id for filtering
    const [clubIndex, setClubIndex] = useState(-1) // the id which is sample_club_id for filtering
    const [nationalityIndex, setNationalityIndex] = useState(-1) // the id which is season_id for filtering
    const [positionIndex, setPositionIndex] = useState(-1) // the id which is season_id for filtering
    
    const [fromNumber, setFromNumber] = useState(1)
    const [order, setOrder] = useState(true) 
    const [chosenActionName, setChosenActionName] = useState("Goal")


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
            const response = await axios.get(`http://${IP}:8000/api/stats/top/player?at=${chosenActionName.toLowerCase()}&se=${seasonIndex}&cl=${clubIndex}&na=${nationalityIndex===-1?-1:NATIONALITY_LIST[nationalityIndex].name}&po=${positionIndex}&from=${fromNumber}&order=${order?"desc":"asc"}`)
            setPlayers(response.data)
        } catch (error) {
            console.log("Error fetching players!", error)
        }
    }

    useEffect(() => {

        fetchData()
    }, [actionIndex, clubIndex, seasonIndex, nationalityIndex, positionIndex, order, fromNumber])






    return (
        <>


            <TopPlayerFilteringStats
                handelActionIndex={setActionIndex}
                handelSeasonIndex={setClubIndex}
                handelClubIndex={setSeasonIndex}
                handelPositionIndex={setPositionIndex}
                hadelNationalityIndex={setNationalityIndex}
                positions={positions}
                chosenActionName={chosenActionName}
                setChosenActionName={setChosenActionName}
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
                            <th className="table__order" onClick={() => setOrder(!order)}>
                                <span className="table__reorder-stats-button js-reorder-stats-button">
                                <i class={`fa fa-sort-amount-${order?'desc':'asc'}`} aria-hidden="true"></i>
                                </span>
                            </th>
                        </tr>
                    </thead>
                    <tbody className="stats-table__container statsTableContainer">

                        {players.length > 0&& players.map((player, index) => (
                            <tr className="table__row " key={index}>
                                <td className="stats-table__rank">{index + 1}.</td>
                                <td className="stats-table__player">
                                    <a href="//www.premierleague.com/players/65970/player/overview" className="playerName">  {player.first_name} {player.last_name}</a>
                                </td> <td className="hide-s">
                                    <a href="//www.premierleague.com/clubs/11/Manchester-City/overview" className="stats-table__cell-icon-align">
                                        <span className="badge badge-image-container" data-widget="club-badge-image" data-size="25">
                                            <img className="badge-image badge-image--25 js-badge-image" src={`http://${IP}:8000${player.sample_club.logo}`}  alt="logo"/>
                                        </span>{player.sample_club.name}
                                    </a>
                                </td>
                                <td className="hide-s">
                                    <div className="stats-table__cell-icon-align">
                                        <img className="stats-table__flag-icon" src={`http://${IP}:8000/images/flags/${getNationality(player.nationality)}.png`} alt="flag"/>
                                        <span className="playerCountry">{player.nationality}</span>
                                    </div>
                                </td>
                                <td className="stats-table__main-stat">{player.stats}</td>
                                <td>&nbsp;</td>
                            </tr>

                        ))
                        }
                    </tbody>
                </table>
            </div>
        </>
    )
}


const getNationality = (name) => {
    for (let index = 0; index < NATIONALITY_LIST.length; index++) {
        if (NATIONALITY_LIST[index].name === name ) return NATIONALITY_LIST[index].code        
    }
    return "XX"
}