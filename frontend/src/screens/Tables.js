import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { TopTableFilter } from '../components/TopTableFilter';
import { TableMatchRow } from '../components/TableMatchRow';

const Tables = () => {

    const [week, setWeek] = useState(20)
    const [homeAway, setHomeAway] = useState(0)
    const [seasonIndex, setSeasonIndex] = useState(0)

    const [table, setTable] = useState([])



    const fetchData = async () => {
        if (seasonIndex !== 0) {
            try {
                let hw = "-1"
                if (homeAway == 1) hw = "H" 
                else if (homeAway == 2) hw = "W"
                const { data } = await axios.get(`http://127.0.0.1:8000/api/overview/tables?se=${seasonIndex}&mw=${week!=20?week:-1}&ha=${hw}`)
                setTable(data)
            } catch (error) {
                console.log("Error fetching stats!", error)
            }
        }
    }

    useEffect(() => {

        fetchData()
    }, [seasonIndex, week, homeAway])






    return (

        <main id="mainContent" tabindex="0">
            <div class="tabbedContent">

                <div class="league-table mainTableTab active"
                    data-ui-tab="First Team" data-script="pl_filtered-list"
                    data-filter-list="FIRST" data-compseason="719"
                    data-widget="table-filtered"
                    data-detail="2"
                    data-live="true"
                    data-tab-aware-default="true">
                    <div class="wrapper">
                        <TopTableFilter
                            week={week}
                            setWeek={setWeek}
                            homeAway={homeAway}
                            setHomeAway={setHomeAway}
                            seasonIndex={seasonIndex}
                            handelSeasonIndex={setSeasonIndex}
                        />
                    </div>

                    <div class="wrapper col-12 league-table__table-header">
                        <div class="league-table__comp-logo-container js-table-logo">
                            <img class="league-table__comp-logo" src="https://resources.premierleague.com/premierleague/competitions/competition_1.png" />
                        </div>

                        <div class="league-table toggle-btn js-live-toggle-container is-active u-hide">
                            <div class="live-animation"><span></span></div>
                            <span><span class="league-table__live toggle-btn__live-text"> Live</span> League Table</span>
                            <button class="toggle-btn__toggle js-live-toggle">
                                <span class="toggle-btn__ball"></span>
                            </button>
                        </div>
                    </div>

                    <div class="league-table__all-tables-container allTablesContainer">
                        <div class="wrapper col-12">

                            <div class="tableContainer" data-round="5851">

                                <div class="table league-table__table wrapper col-12">

                                    <table>
                                        <thead>
                                            <tr>
                                                <th class="league-table__pos-header" scope="col">
                                                    <div class="league-table__thFull thFull">Position</div>
                                                    <div class="league-table__thShort thShort"></div>
                                                </th>
                                                <th class="league-table__team-header" scope="col">Club</th>
                                                <th scope="col"> <div class="league-table__thFull thFull">Played</div>
                                                    <div class="league-table__thShort thShort">Pl </div>
                                                </th>
                                                <th scope="col">
                                                    <div class="league-table__thFull thFull">Won </div>
                                                    <div class="league-table__thShort thShort">W </div>
                                                </th>
                                                <th scope="col">
                                                    <div class="league-table__thFull thFull">Drawn </div>
                                                    <div class="league-table__thShort thShort">D </div>
                                                </th>
                                                <th scope="col">
                                                    <div class="league-table__thFull thFull">Lost </div>
                                                    <div class="league-table__thShort thShort">L </div>
                                                </th>
                                                <th class="hideSmall" scope="col">
                                                    <abbr title="Goals For">GF </abbr>
                                                </th>
                                                <th class="hideSmall" scope="col">
                                                    <abbr title="Goals Against">GA </abbr>
                                                </th>
                                                <th scope="col">
                                                    <abbr title="Goal Difference">GD</abbr>
                                                </th>
                                                <th scope="col" class="points">
                                                    <div class="league-table__thFull thFull">Points </div>
                                                    <div class="league-table__thShort thShort">Pts </div>
                                                </th> <th class="league-table__team-form hideMed" scope="col">Form</th>
                                            </tr>
                                        </thead>
                                        


                                        <tbody class="league-table__tbody isPL">
                                            {table.length > 0 && table.map((row, index) => (

                                                <TableMatchRow data={row} key={index} idx={index}/>
                                            ))}
                                        </tbody>




                                    </table>


                                </div>
                            </div>
                        </div>
                    </div>


                </div>


            </div>


        </main>




    )
};

export default Tables