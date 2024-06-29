import React, { useState } from 'react'

export const AdsFixture = () => {

    const date = new Date()

  return (
    



    <div className="col-12 fixtures-header-info">
        <span className="hublot-watch-container">
            <div id="flashContentHublot">
                <a href="https://www.hublot.com?utm_source=PremierLeague&amp;utm_medium=site&amp;utm_campaign=official-timekeeper"
                    target="_blank" className="global-link">
                    <div className="hublot-timekeeper visible">
                        <div className="hublot-watch">
                            <img className="watch desktop"
                                src="https://www.premierleague.com/resources/rebrand/v7.149.0/i/hublot-watch/watch.png"
                                alt="" />
                            <p className="timer">
                                <span id="timer-hours">{date.getHours()}</span>:<span id="timer-minutes">{date.getMinutes()}</span>
                            </p>
                        </div>
                    </div>
                    <svg className="hublot-logo">
                        <use xmlns="http://www.w3.org/1999/xlink"
                            href="https://www.premierleague.com/resources/rebrand/v7.149.0/i/svg-output/icons.svg#partners-hublot-official-timekeeper">
                        </use>
                    </svg>
                </a>
            </div>
        </span>

        <div className="fixtures-header-info__fixture-key">
            <span className="fixtures-header-info__fixture-key-text text-centre">
                <svg className="fixtures-header-info__fixture-key-icon">
                    <use xlink="http://www.w3.org/1999/xlink"
                        href="https://www.premierleague.com/resources/rebrand/v7.149.0/i/svg-output/icons.svg#icn-info">
                    </use>
                </svg>
                All times shown are your <span className="">local time</span>
            </span>
        </div>
    </div>
  )
}
