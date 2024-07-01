import axios from "axios"
import { useEffect, useState } from "react"
import { PlayerStatsCard } from "./PlayerStatsCard"
import { ClubStatsCard } from "./ClubStatsCard"

export const StatsDashboard = () => {

  
    const [stats, setStats] = useState(null)

    const fetchData = async () => {
        console.log("repeat fetching data...")
        try {
            const {data} = await axios.get("http://127.0.0.1:8000/api/stats")
            console.log("stats player: ")
            setStats(data)
        } catch (error) {
            console.log("Error fetching stats!", error)
        }
    }

    useEffect(() => {

        fetchData()
    }, [])


    useEffect(() => {

        console.log("stats=", stats)
    }, [stats])



    if (stats != null) return (
        <>
            
            <ul data-script="pl_stats" data-widget="top-stats-header" data-header-id="topPerformers" className="block-list-4 mobileScrollList">
                
           {stats.player_stats.map((ps, index) => (
                <PlayerStatsCard data={ps.players} name={ps.action_type}type="Player" />
            ))}
            
            </ul>

            <ul data-script="pl_stats" data-widget="top-stats-header" data-header-id="topPerformers" className="block-list-4 mobileScrollList">
                
               <ClubStatsCard data={stats.club_stats.win } name="Win" />
               <ClubStatsCard data={stats.club_stats.goal } name="Goal" />
               <ClubStatsCard data={stats.club_stats.lose } name="Lose" />
               <ClubStatsCard data={stats.club_stats.tackle } name="Tackle" />
            
            
            </ul>
            
        </>
    ) 
}
