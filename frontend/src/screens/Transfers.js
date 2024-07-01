import React, { useContext } from 'react'
import { MainContext } from '../App'

const Transfers = () => {


  
  const {heroNameHandler} = useContext(MainContext)
    
    heroNameHandler("Transfer")
    
  return (
    <div>Transfers</div>
  )
}

export default Transfers