import React, {useEffect, useState} from 'react';
import Navbar from "../Navbar/Navbar";

const About = () => {
    const [about, setAbout] = useState([]);

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/about-me')
            .then(res=>res.json())
            .then(data=> setAbout(data))
    },[]);

    return (
        <div>
            <Navbar/>
            <div className="container mt-2">
                <h3 className="text-center">About Me</h3>
                <hr/>
                <div className="row">
                    {about.map((about) => (
                        <div className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-lg-12 mb-4">
                            <h3 className="">{about.name}</h3>
                            <p>{about.position}</p>
                            <p>{about.about_me}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
};

export default About;