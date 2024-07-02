import React, { useContext, useState } from "react";
import "../styles/registerLogin.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { MainContext } from "../App";
import { IP } from "../CREDENTIALS";

const Auth = () => {

    
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [userName, setUserName] = useState("")
    const {userInfo, setUserInfo} = useContext(MainContext)

    const navigate = useNavigate();

    

    const registerHandler = async (e) => {
        e.preventDefault();
        try {
            const {data} = await axios.post(`http://${IP}:8000/api/user/register`, {
                name: email,
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password,
            }, {  headers: { 'Content-Type': 'application/json'  } })

            console.log("registerd")
            localStorage.setItem("user", JSON.stringify({userInfo:data}))
            setUserInfo(data)
            
            navigate('/profile');
        } catch (error) {
            console.log("Can not register", error)
        }
    }



    const loginHandler = async (e) => {
        e.preventDefault();
        try {
            const {data} = await axios.post(`http://${IP}:8000/api/user/login`, {
                username: userName,
                password: password,
            }, {  headers: { 'Content-Type': 'application/json'  } })

            console.log("registerd")
            localStorage.setItem("user", JSON.stringify({username: data.username, token: data.token}))
            setUserInfo(data)
            
            navigate('/profile');
        } catch (error) {
            console.log("Can not login", error)
        }
    }



    return (
        <div className="register-login-wrapper">
            <div class="register-login-main">
                <input type="checkbox" id="chk" aria-hidden="true" />

                <div class="signup">
                    <form>
                        <label for="chk" aria-hidden="true">
                            Sign up
                        </label>
                        <input type="text" name="txt" placeholder="first name" required="" onChange={(e) => setFirstName(e.target.value)}/>
                        <input type="text" name="txt" placeholder="last name" required="" onChange={(e) => setLastName(e.target.value)}/>
                        <input type="email" name="email" placeholder="Email" required="" onChange={(e) => setEmail(e.target.value)}/>
                        
                        <input
                            type="password"
                            name="pswd"
                            placeholder="Password"
                            required=""
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <button onClick={(e) => registerHandler(e)}>Sign up</button>
                    </form>
                </div>

                <div class="login">
                    <form>
                        <label for="chk" aria-hidden="true">
                            Login
                        </label>
                        <input type="email" name="email" placeholder="Email" required="" onChange={(e) => setUserName(e.target.value)}/>
                        <input
                            type="password"
                            name="pswd"
                            placeholder="Password"
                            required=""
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <button onClick={(e) => loginHandler(e)}>Login</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Auth;
