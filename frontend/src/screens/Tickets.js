import React, { useContext } from 'react'
import { MainContext } from '../App'

const Tickets = () => {

  const {heroNameHandler} = useContext(MainContext)
    
    heroNameHandler("Tickets")
    

  return (
    <div>Tickets</div>
  )
}

export default Tickets