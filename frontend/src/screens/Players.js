import React, { useEffect, useState } from 'react'
import { TopPlayerFiltering } from '../components/TopPlayerFilter'
import axios from 'axios'
import imageMissing from '../static/i/elements/Photo-Missing.png';

const Players = () => {

    const [clubIndex, setClubIndex] = useState(-1) // the id which is sample_club_id for filtering
    const [seasonIndex, setSeasonIndex] = useState(1) // the id which is season_id for filtering

    const [players, setPlayers] = useState([])


    const fetchData = async () => {
        try {
            console.log(`season is ${seasonIndex} and club is ${clubIndex}`)
            const response = await axios.get(`http://127.0.0.1:8000/api/overview/players?se=${seasonIndex}&cl=${clubIndex}`)
            console.log("players:")
            console.log(response.data)
            setPlayers(response.data)
        } catch (error) {
            console.log("Error fetching players!", error)
        }
        
    }

    useEffect(() => {
        console.log("repeat fetching data...")
        fetchData();
    },[clubIndex, seasonIndex ])


    return (
        <main className="mainContent" style={{ padding: "1rem" }}>
            <div className="tabbedContent">

                <div data-widget="list-data" data-type="player" data-comp-seasons="578" data-script="pl_filtered-list" data-page-size="10" className="playerIndex">

                    <div className="wrapper">


                        <TopPlayerFiltering 
                            handelClubIndex={setClubIndex} 
                            handelSeasonIndex={setSeasonIndex}
                        />


                        <div className="col-12">


                            <div className="table playerIndex player-listing">

                                <table>
                                    <thead className="u-hide-mobile-lg">
                                        <tr>
                                            <th scope="col">Player</th>
                                            <th className="player-listing__header-item" scope="col">Position</th>
                                            <th className="player-listing__header-item" scope="col">Nationality</th>
                                        </tr>
                                    </thead>

                                    <tbody className="dataContainer indexSection">
                                        {
                                            players && players.map((player, index) => (
                                                <tr className="player" key={index}> 
                                                    <td> 
                                                        <a href="//www.premierleague.com/players/19970/Max-Aarons/overview" className="player__name">
                                                        
                                                            <img className="img player__name-image" data-player="p232980" data-size="40x40" src={player.image!==""?`http://127.0.0.1:8000${player.image}`:imageMissing} alt="Photo for Max Aarons"/>
                                                            {`${player.first_name} ${player.last_name}`}
                                                        </a> 
                                                    </td> 
                                                    <td className="u-hide-mobile-lg player__position">{player.position}</td>
                                                    <td className="u-hide-mobile-lg"> 
                                                        <span className="player__nationality">  
                                                            <span className="flag player__flag GB-ENG"> 
                                                                <img className="player__flag-icon" src="https://resources.premierleague.com/premierleague/flags/GB-ENG@x2.png" alt="flag-img"/> 
                                                            </span> 
                                                            <span className="player__country">{player.nationality}</span> 
                                                        </span> 
                                                    </td> 
                                                </tr>
                                            ))
                                        }
                                        





                                    </tbody>


                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    )
}

export default Players