import axios from "axios"
import { useEffect, useState } from "react"
import { StatsCard } from "./StatsCard"

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

        console.log(stats)
    }, [stats])



    if (stats != null) return (
        <>
            
            <ul data-script="pl_stats" data-widget="top-stats-header" data-header-id="topPerformers" class="block-list-4 mobileScrollList">
                
           {stats.player_stats.map((ps, index) => (

                <StatsCard data={ps.players} name={ps.action_type} key={index} type="Player" />
            ))}
            
            </ul>

            <ul data-script="pl_stats" data-widget="top-stats-header" data-header-id="topPerformers" class="block-list-4 mobileScrollList">
                
               {/* <StatsCard data={stats.club_stats.win } name="Win" type="Club" />
               <StatsCard data={stats.club_stats.lose } name="Lose" type="Club" />
               <StatsCard data={stats.club_stats.goal } name="Goal" type="Club" />
               <StatsCard data={stats.club_stats.tackle } name="Tackle" type="Club" /> */}

                
            
            </ul>
            
        </>
    ) 
}
