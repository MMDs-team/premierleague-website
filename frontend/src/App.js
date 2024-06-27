import React from "react";
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



function NoPage() {
    const navigate = useNavigate();
    navigate('/');
    return <Navigate to={ '/'} />;
}


export default function App() {


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
    </>
  );
}



