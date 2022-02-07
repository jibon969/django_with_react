import React, { useEffect, useState } from 'react';
import {Link} from 'react-router-dom';

import image1 from '../../static/images/slider/2000x400.png'
import image2 from '../../static/images/slider/1400x400.png'
import image3 from '../../static/images/slider/800x400.png';
import image4 from '../../static/images/slider/600x400.png'

const Slider = () => {

    const [sliderData, setSliderData] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/slider-list/`)
            .then(res => res.json())
            .then(data => setSliderData(data))
    }, []);

    if (sliderData){
        return(
            <div>
                <div id="carouselExampleControls" className="carousel slide mb-3" data-ride="carousel">
                    <div className="carousel-inner">
                        {
                            sliderData.map((slider, i)=>(
                                slider.url_field == null?
                                    <div className={"carousel-item " + (i===0 ? "active": "")}>
                                        <picture>
                                            <source srcSet={slider.extra_large_url} media="(min-width: 1400px)" />
                                            <source srcSet={slider.large_device_url} media="(min-width: 768px)" />
                                            <source srcSet={slider.medium_device_url} media="(min-width: 576px)" />
                                            <img srcSet={slider.small_device_url} alt="" className="d-block img-fluid" />
                                        </picture>
                                    </div>
                                    :
                                    <div className={"carousel-item " + (i===0 ? "active": "")}>
                                        <Link to={slider.url_field}>
                                            <picture>
                                                <source srcSet={slider.extra_large_url} media="(min-width: 1400px)" />
                                                <source srcSet={slider.large_device_url} media="(min-width: 768px)" />
                                                <source srcSet={slider.medium_device_url} media="(min-width: 576px)" />
                                                <img srcSet={slider.small_device_url} alt="" className="d-block img-fluid" />
                                            </picture>
                                        </Link>
                                    </div>
                            ))
                        }
                    </div>
                    <a className="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                         <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                         <span className="sr-only">Previous</span>
                     </a>
                    <a className="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">                         <span className="carousel-control-next-icon" aria-hidden="true"></span>
                         <span className="sr-only">Next</span>
                     </a>
                </div>
            </div>
        )
    }
    else{
        return(
            <div>
                <div id="carouselExampleControls" className="carousel slide mb-3" data-ride="carousel">
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <picture>
                                <source srcSet={image1} media="(min-width: 1400px)" />
                                <source srcSet={image2} media="(min-width: 768px)" />
                                <source srcSet={image3} media="(min-width: 576px)" />
                                <img srcSet={image4} alt="" className="d-block img-fluid" />
                            </picture>
                        </div>
                        <div className="carousel-item">
                            <picture>
                                <source srcSet={image1} media="(min-width: 1400px)" />
                                <source srcSet={image2} media="(min-width: 768px)" />
                                <source srcSet={image3} media="(min-width: 576px)" />
                                <img srcSet={image4} alt="" className="d-block img-fluid" />
                            </picture>
                        </div>
                    </div>
                    <a className="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                         <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                         <span className="sr-only">Previous</span>
                     </a>
                    <a className="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">                         <span className="carousel-control-next-icon" aria-hidden="true"></span>
                         <span className="sr-only">Next</span>
                     </a>
                </div>
            </div>
        )
    }

};

export default Slider;