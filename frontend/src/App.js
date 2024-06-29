import React, { createContext, useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate, useNavigate } from "react-router-dom";
import Header from "./components/Header.jsx";
import LoginScreen from './screens/LoginScreen.js';
import RegisterScreen from './screens/RegisterScreen.js';
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
    const [clubs, setClubs] = useState([])

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

        
    }

    useEffect(() => {
        fetchData();
    },[])

    let lists = [
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

  return (
    <>

        <MainContext.Provider value={{
                thisSeasonClubs : thisSeasonClubs ,
                seasonOrdered : seasonOrdered,
                clubs: clubs
            }}>
            <BrowserRouter>


                <Header lists={lists}/>
                    <Routes>
                        <Route path="*" element={<NoPage/>} />
                        <Route path="/login" element={ <LoginScreen/>} />
                        <Route path="/register" element={<RegisterScreen/>} />
                        <Route path="/profile" element={<ProfileScreen/>} />
                        <Route path="/fixtures" element={<Fixtures/>} />
                        <Route path="/tables" element={<Tables/>} />
                        <Route path="/transfers" element={<Transfers/>} />
                        <Route path="/stats" element={<Stats/>} />
                        <Route path="/tickets" element={<Tickets/>} />
                        <Route path="/clubs" element={<Clubs />} />
                        <Route path="/players" element={<Players/>} />
                        <Route path="/" element={<HomeScreen/>} />
                        

                    </Routes>
            </BrowserRouter>
        </MainContext.Provider>
    </>
  );
}



