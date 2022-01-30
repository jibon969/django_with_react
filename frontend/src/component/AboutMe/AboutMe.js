import React from 'react';

const AboutMe =(props)=>{
    const about = props.about;
    const {name, position, about_me} = about;

    return(
        <div>
            <div className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-lg-12 mb-4">
                <h3>{name}</h3>
                <p>{position}</p>
                <p>{about_me}</p>
            </div>
        </div>
    )
};
export default AboutMe;