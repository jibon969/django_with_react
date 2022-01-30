import React from 'react';
import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import About from "../About/About";
import Post from "../Post/Post";
import PostDetail from "../PostDetail/PostDetail";


const RouterHandle = () => {

    return (
        <div>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="post" element={<Post/>} />
                <Route path="post-detail/:slug/" element={<PostDetail/>} />
                <Route path="about-me/" element={<About />} />
            </Routes>
        </div>
    );
};

export default RouterHandle;