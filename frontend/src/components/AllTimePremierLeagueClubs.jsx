import axios from "axios";
import React, { useEffect, useState } from "react";

export const AllTimePremierLeagueClubs = () => {
    const [clubs, setClubs] = useState([]);

    const fetchData = async () => {
        try {
            const response = await axios.get(
                `http://127.0.0.1:8000/api/overview/allClubs`
            );
            setClubs(response.data);
        } catch (error) {
            console.log("Error fetching clubs!", error);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div class="indexAllTime">
            <h2 class="team-index__title">All-time Premier League Clubs</h2>
            <div class="table">
                <table class="team-index">
                    <thead class="team-index__header">
                        <tr class="u-hide-mob">
                            <th class="team">Club</th>
                            <thc class="venue">Stadium</thc>
                        </tr>
                    </thead>

                    <tbody class="allTimeDataContainer js-all-time-data-container team-index__body">
                        {clubs.map((club, index) => (
                            <tr>
                                <td class="team">
                                    <a href="//www.premierleague.com/clubs/1/Arsenal/overview">
                                        <span class="badge badge-image-container" data-widget="club-badge-image" data-size="50" >
                                            <img class="badge-image badge-image--50 js-badge-image" src={`http://127.0.0.1:8000${club.logo}`} alt="club logo"/>
                                        </span>
                                        <div class="team-index__name">
                                            <div class="team-index__club-name">{club.name}</div>
                                            <div class="team-index__stadium-name u-show-mob">
                                                {club.main_stadium}
                                            </div>
                                        </div>
                                        <div class="team-index__arrow team-index__arrow--icon u-show-mob">
                                            <svg class="svg">
                                                <use xlink="http://www.w3.org/1999/xlink"
                                                    href="https://www.premierleague.com/resources/rebrand/v7.149.0/i/svg-output/icons.svg#icn-arrow-right"
                                                ></use>
                                            </svg>
                                        </div>
                                    </a>
                                </td>
                                <td class="venue u-hide-mob">
                                    <a href="//www.premierleague.com/clubs/1/Arsenal/stadium">
                                        <span class="icon__stadium venue__stadium-icon">
                                            <svg class="svg" width="16" height="11" viewBox="0 0 16 11" fill="none" xmlns="http://www.w3.org/2000/svg" >
                                                <path fill-rule="evenodd" clip-rule="evenodd"
                                                    d="M15.9846 6.419V6.88792L8.64637 10.3198V9.85089L15.9846 6.419ZM7.27558 9.09389L8.45642 9.84944V10.3098L7.27558 9.55034V9.09389ZM0 6.38323L5.05679 9.68344V10.1523L0 6.83811V6.38323ZM6.73304 9.08212V9.52922L5.33611 10.1523V9.70525L6.73304 9.08212ZM15.9846 5.2896V5.75851L8.64637 9.1904V8.72149L15.9846 5.2896ZM7.27558 7.96608L8.45642 8.72241V9.18274L7.27558 8.4233V7.96608ZM0 5.19779L5.05679 8.49724V8.96693L0 5.65189V5.19779ZM6.73304 7.89669V8.34378L5.33611 8.96691V8.51904L6.73304 7.89669ZM7.5566 0.166687L8.86323 1.02894L10.4778 0.288202L15.912 3.01601L14.2117 3.74974L16 4.61343L8.63254 7.98689L7.00484 6.88708L5.10085 7.78205L0.029439 4.45305L1.96198 3.6905L0.544977 2.84305L7.5566 0.166687ZM8.71869 1.84297L3.86501 3.82296L7.0618 5.71494L12.0467 3.61732L8.71869 1.84297ZM15.9992 3.55344V4.00054L15.621 4.16956L15.1502 3.932L15.9992 3.55344ZM0.544938 3.27306L1.26193 3.70847L0.775702 3.91177L0.54185 3.78091L0.544938 3.27306Z"
                                                ></path>
                                            </svg>
                                        </span>
                                        <div class="team-index__stadium-name">{club.main_stadium}</div>
                                        <span class="icon__arrow venue__arrow-icon">
                                            <svg class="svg">
                                                <use xlink="http://www.w3.org/1999/xlink"
                                                    href="https://www.premierleague.com/resources/rebrand/v7.149.0/i/svg-output/icons.svg#icn-arrow-right"
                                                ></use>
                                            </svg>
                                        </span>
                                    </a>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};
