import React, { useContext } from 'react'
import { MainContext } from '../App'

export const Hero = () => {

    const {heroName} = useContext(MainContext)
    
    if (heroName == "Stats") return <></>
    return (
        <div class="page-hero">


        <header class="page-header    page-header--small-title ">
            <div class="page-header__wrapper page-header__wrapper--tabs">
                    <h1 class="page-header__title">{heroName}</h1>
                
            </div>
        </header>
        </div>
    )
}
