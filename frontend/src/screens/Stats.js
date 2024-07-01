import React, { useState } from 'react'
import { PageNav } from '../components/PageNav'
import { PlayerStats } from '../components/PlayerStats'
import { ClubStats } from '../components/ClubStats'
import { StatsDashboard } from '../components/StatsDashboard'


const Stats = () => {


  const menu = [
    {link:"/stats", name:'Dashboard',},
    {link:"/stats", name:'Player Stats',},
    {link:"/stats", name:'Club Stats',},
    {link:"/stats", name:'All-time Stats',},
    {link:"/stats", name:'Milestones',},
    {link:"/stats", name:'Records',},
    {link:"/stats", name:'Head-to-Head',},
    {link:"/stats", name:'Player Comparison',}
  ]


  const [indexTab, setTabIndex] = useState(0)




  return (
   
    <main className="mainContent" style={{padding:"1rem"}}>

      <PageNav menu={menu} tabHandler={setTabIndex} />
      <div className='wrapper'>
        <div data-script="pl_stats" data-widget="stats-table" data-current-size="10" data-stat="goals" data-type="player" data-page-size="10" data-page="0" data-comp-seasons="578" data-num-entries="303">

            <header class="widget-header ">
                    <h2 class="widget-header__title">Premier League {menu[indexTab].name}</h2>
            </header>

            {indexTab===0 && <StatsDashboard />}
            {indexTab===1 && <PlayerStats /> }
             {indexTab===2 && <ClubStats /> }
            {/*indexTab===3 && <AllTimeStats /> }
            {indexTab===4 && <StatsDashboard /> }
            {indexTab===5 && <StatsDashboard /> }
            {indexTab===6 && <StatsDashboard /> }
            {indexTab===7 && <StatsDashboard /> } */}
         </div>
      </div>
    </main>
  )
}

export default Stats