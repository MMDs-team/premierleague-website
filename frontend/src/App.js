import React, { createContext, useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate, useNavigate } from "react-router-dom";
import Header from "./components/Header.jsx";
import Auth from './screens/Auth.js';
import HomeScreen from './screens/HomeScreen.js';
import ProfileScreen from './screens/ProfileScreen.js';
import Fixtures from './screens/Fixtures.js';
import Tables from './screens/Tables.js';
import Transfers from './screens/Transfers.js';
import Stats from './screens/Stats.js';
import Tickets from './screens/Tickets.js';
import Clubs from './screens/Clubs.js';
import Players from './screens/Players.js';
import axios from "axios";
import { Footer } from "./components/Footer.jsx";
import { Hero } from "./components/Hero.jsx";
import "./styles/other.css"

export const  MainContext = createContext(null)


function NoPage() {
    const navigate = useNavigate();
    navigate('/');
    return <Navigate to={ '/'} />;
}


export default function App() {


    const [thisSeasonClubs, setThisSeasonClubs] = useState()
    const [seasonOrdered, setSeasonOrdered] = useState([])
    const [actonTypes, setActionTypes] = useState([])
    const [clubs, setClubs] = useState([])
    const savedUser = localStorage.getItem("user")
    const [userInfo, setUserInfo] = useState(savedUser == null?null:savedUser)
    const [heroName, setHeroName] = useState("Home")

    const fetchData = async () => {
        try {
            const response = await axios.get(`http://${IP}:8000/api/club/ex`)
            setThisSeasonClubs(response.data)
        } catch (error) {
            console.log("Error fetching this season's clubs!", error)
        }

        try {
            const response = await axios.get(`http://${IP}:8000/api/season/ordered`)
            setSeasonOrdered(response.data)
        } catch (error) {
            console.log("Error fetching seasons!", error)
        }

        try {
            
            const response = await axios.get(`http://${IP}:8000/api/club/getAll`)
            setClubs(response.data)
        } catch (error) {
            console.log("Error fetching clubs!", error)
        }

        try {
            
            const response = await axios.get(`http://${IP}:8000/api/action/action_type`)
            setActionTypes(response.data)
        } catch (error) {
            console.log("Error fetching action types!", error)
        }

        
    }

    useEffect(() => {
        fetchData();
    },[])



  return (
    <>

        <MainContext.Provider value={{
                thisSeasonClubs : thisSeasonClubs ,
                seasonOrdered : seasonOrdered,
                actionTypes: actonTypes,
                clubs: clubs,
                userInfo: userInfo,
                setUserInfo: setUserInfo,
                heroName: heroName,
                heroNameHandler: setHeroName 
            }}>
            <BrowserRouter>

                <div className="main-wrapper-all">
                    <Header/>
                        <Hero />
                        <Routes>
                            <Route path="*" element={<NoPage/>} />
                            {!userInfo &&<Route path="/auth" element={ <Auth/>} />}
                            {userInfo && <Route path="/profile" element={<ProfileScreen/>} />}
                            <Route path="/fixtures" element={<Fixtures/>} />
                            <Route path="/tables" element={<Tables/>} />
                            <Route path="/transfers" element={<Transfers/>} />
                            <Route path="/stats" element={<Stats/>} />
                            <Route path="/tickets" element={<Tickets/>} />
                            <Route path="/clubs" element={<Clubs />} />
                            <Route path="/players" element={<Players/>} />
                            <Route path="/" element={<HomeScreen/>} />
                            

                        </Routes>
                    <Footer />
                </div>
            </BrowserRouter>
        </MainContext.Provider>
    </>
  );
}




export const lists = [
    {
        name: "Permier League",
        options : [
            { name: "Home", url:"/"},
            { name: "Fixtures", url:"/fixtures"},
            { name: "Tables", url:"/tables"},
            { name: "Transfers", url:"/transfers"},
            { name: "Stats", url:"/stats"},
            { name: "Tickets", url:"/tickets"},
            { name: "Clubs", url:"/clubs"},
            { name: "Players", url:"/players"}
        ]
    },
    {
        name: "Permier League",
        options : [
            { name: "Home", url:"/"},
            { name: "Fixtures", url:"/fixtures"},
            { name: "Tables", url:"/tables"},
            { name: "Transfers", url:"/transfers"},
            { name: "Stats", url:"/stats"},
            { name: "Tickets", url:"/tickets"},
            { name: "Clubs", url:"/clubs"},
            { name: "Players", url:"/players"}
        ]
    },
    {
        name: "Permier League",
        options : [
            { name: "Home", url:"/"},
            { name: "Fixtures", url:"/fixtures"},
            { name: "Tables", url:"/tables"},
            { name: "Transfers", url:"/transfers"},
            { name: "Stats", url:"/stats"},
            { name: "Tickets", url:"/tickets"},
            { name: "Clubs", url:"/clubs"},
            { name: "Players", url:"/players"}
        ]
    },
    {
        name: "Permier League",
        options : [
            { name: "Home", url:"/"},
            { name: "Fixtures", url:"/fixtures"},
            { name: "Tables", url:"/tables"},
            { name: "Transfers", url:"/transfers"},
            { name: "Stats", url:"/stats"},
            { name: "Tickets", url:"/tickets"},
            { name: "Clubs", url:"/clubs"},
            { name: "Players", url:"/players"}
        ]
    }
]