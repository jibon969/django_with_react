import React from 'react';
import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import About from "../About/About";
import Post from "../Post/Post";
import PostDetail from "../PostDetail/PostDetail";
import ContactMe from "../ContactMe/ContactMe";
import Blog from "../Blog/Blog";
import Navbar from "../Navbar/Navbar";
import Footer from "../Footer/Footer";
import BlogCategory from "../BlogCategory/BlogCategory";

const RouterHandle = () => {

    return (
        <div>
            <Routes>
                <Route path="/" element={
                    <div>
                        <Navbar/>
                        <Home />
                        <Footer/>
                    </div>
                } />
                <Route path="post" element={
                    <div>
                        <Navbar/>
                        <Post/>
                        <Footer/>
                    </div>
                } />
                <Route path="post-detail/:slug/" element={
                    <div>
                        <Navbar/>
                        <PostDetail/>
                        <Footer/>
                    </div>
                } />
                <Route path="about-me/" element={
                    <div>
                        <Navbar/>
                        <About />
                        <Footer/>
                    </div>
                } />
                <Route path="contact-me/" element={
                    <div>
                        <Navbar/>
                        <ContactMe />
                        <Footer/>
                    </div>
                } />
                <Route path="blog/" element={
                    <div>
                        <Navbar/>
                        <Blog />
                        <Footer/>
                    </div>
                } />
                <Route path="blog-category/" element={
                    <div>
                        <Navbar/>
                        <BlogCategory/>
                        <Footer/>
                    </div>
                } />
            </Routes>
        </div>
    );
};

export default RouterHandle;