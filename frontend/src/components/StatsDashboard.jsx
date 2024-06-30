import axios from "axios"
import { useEffect, useState } from "react"
import { StatsCard } from "./StatsCard"

export const StatsDashboard = () => {

  
    const [players, setPlayers] = useState([])

    const fetchData = async () => {
        console.log("repeat fetching data...")
        try {
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
    }, [])






    return (
        <>
            <ul data-script="pl_stats" data-widget="top-stats-header" data-header-id="topPerformers" class="block-list-4 mobileScrollList">
                
                    
                        <StatsCard />
                        <StatsCard />
                        <StatsCard />
                        <StatsCard />
            
            </ul>
        </>
    )
}
