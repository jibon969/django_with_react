import React from 'react';
import Navbar from "../Navbar/Navbar";
import Slider from '../Slider/Slider';
import Footer from "../Footer/Footer";
import Post from "../Post/Post";

const Home = () =>{
    return(
        <div>
            <Navbar/>
            <Slider/>
            <Post/>
            <Footer/>
        </div>
    )
};

export default Home;