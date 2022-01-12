import React from 'react';
import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import About from "../About/About";


const RouterHandle = () => {
    return (
        <div>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="about" element={<About />} />
            </Routes>
        </div>
    );
};

export default RouterHandle;