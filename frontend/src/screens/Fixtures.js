import React, { useContext, useEffect, useState } from 'react'
import { TopFixturesFilter } from '../components/TopFixturesFilter'
import { MainContext } from '../App'
import axios from 'axios'
import { AdsFixture } from '../components/AdsFixture'
import { DataFixtures } from '../components/DataFixtures'

const Fixtures = () => {


    const [clubIndex, setClubIndex] = useState(-1) // the index which is sample_club_id for filtering

    const clubsOfThisSeason = useContext(MainContext).thisSeasonClubs
    const {heroNameHandler} = useContext(MainContext)
    
    heroNameHandler("Fixtures")

    const [fixtures, setFixtures] = useState([])


    

    const fetchData = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/overview/fixtures?s_cl=${clubIndex}`)
            setFixtures(response.data)
        } catch (error) {
            console.log("Error fetching fixtures!", error)
        }

        
    }

    useEffect(() => {
        console.log("here club index became", clubIndex)
        fetchData();
    },[clubsOfThisSeason, clubIndex])


    return (


        <main className="mainContent" >
            <div className="tabbedContent">
                <div className="league-table mainTableTab active" data-ui-tab="First Team" data-script="pl_filtered-list"
                    data-filter-list="FIRST" data-compseason="719" data-widget="table-filtered" data-detail="2"
                    data-live="true" data-tab-aware-default="true">
                    <div className="wrapper">

                        <TopFixturesFilter handelClubIndex={setClubIndex} />   {/* top filtering*/}

                        <AdsFixture />

                        <DataFixtures fixtures={fixtures}/>

                    </div>
                </div>
            </div>
        </main>

        
    )
}

export default Fixtures