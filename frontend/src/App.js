import React from "react";
import { BrowserRouter, Routes, Route, Navigate, useNavigate } from "react-router-dom";
import LoginScreen from './screens/LoginScreen.js';
import RegisterScreen from './screens/RegisterScreen.js';
import HomeScreen from './screens/HomeScreen.js';
import ProfileScreen from './screens/ProfileScreen.js';


function NoPage() {
    const navigate = useNavigate();
    navigate('/');
    return <Navigate to={ '/'} />;
}


export default function App() {

  return (
    <BrowserRouter>
        <Routes>
            <Route path="*" element={<NoPage/>} />
            <Route path="/login" element={ <LoginScreen/>} />
            <Route path="/register" element={<RegisterScreen/>} />
            <Route path="/profile" element={<ProfileScreen/>} />
            <Route exact path="/" element={<HomeScreen />}>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}



