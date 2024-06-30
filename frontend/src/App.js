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

    const fetchData = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/api/club/ex")
            setThisSeasonClubs(response.data)
            console.log(response.data)
        } catch (error) {
            console.log("Error fetching this season's clubs!", error)
        }

        try {
            const response = await axios.get("http://127.0.0.1:8000/api/season/ordered")
            setSeasonOrdered(response.data)
            console.log(response.data)
        } catch (error) {
            console.log("Error fetching seasons!", error)
        }

        try {
            
            const response = await axios.get(`http://127.0.0.1:8000/api/club/getAll`)
            console.log("clubs:")
            setClubs(response.data)
        } catch (error) {
            console.log("Error fetching clubs!", error)
        }

        try {
            
            const response = await axios.get(`http://127.0.0.1:8000/api/action/action_type`)
            console.log("clubs:")
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
                setUserInfo: setUserInfo
            }}>
            <BrowserRouter>

                <div className="main-wrapper-all">
                    <Header/>
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