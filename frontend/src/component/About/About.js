import React, {useEffect, useState} from 'react';
import AboutMe from "../AboutMe/AboutMe";

const About = () => {
    const [about, setAbout] = useState([]);

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/about-me')
            .then(res=>res.json())
            .then(data=> setAbout(data))
    },[]);

    return (
        <div>
            <div className="container mt-2">
                <h3 className="text-center">About Me</h3>
                <hr/>
                <div className="row">
                    {
                        about.map(about => <AboutMe about={about} />)
                    }

                </div>
            </div>
        </div>
    )
};

export default About;