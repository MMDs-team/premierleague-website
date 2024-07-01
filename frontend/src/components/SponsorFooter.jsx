import axios from 'axios'
import React, { useEffect, useState } from 'react'

export const SponsorFooter = () => {


    const [sponsors, setSponsors] = useState([])
   

    const fetchData = async () => {
        try {
            const {data} = await axios.get("http://127.0.0.1:8000/api/sponsor")
            setSponsors(data)
        } catch (error) {
            console.log("Error fetching sponsors!", error)
        }
    }

    useEffect(() => {

        fetchData()
    }, [])



  return (
    <div class="footer-sponsors">
        <ul class="footer-sponsors__list">
            {
                sponsors.length > 0 && sponsors.map((spon, index) => (

                    <li class="footer-sponsors__sponsor ">
                        <a class="footer-sponsors__link" href={spon.website} target="_blank">
                            <picture class="footer-sponsors__sponsor-image picture ">
                                        <img loading="lazy" class="footer-sponsors__image picture__img" src={`http://127.0.0.1:8000${spon.logo}`} alt="ea_sports_black_435_x_290_360"/>
                            </picture>

                            <span class="footer-sponsors__sponsor-text">{spon.name}</span>
                        </a>                        
                    </li>
                ))
            }
            
        </ul>

    </div>
  )
}
