import React, { useEffect, useState } from 'react';

const Slider = () => {

    const [sliderData, setSliderData] = useState([]);

    // fetching the all AboutUs data from server
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/slider-list/')
            .then(res => res.json())
            .then(data => setSliderData(data))
    }, []);


    return (
        <div>
            <div id="carouselExampleControls" className="carousel slide" data-ride="carousel">
                <div className="carousel-inner">
                    {
                        sliderData.map((slider) => (
                            <div>

                                {
                                    slider.value == 1 ?
                                        <div className="carousel-item active">
                                            <picture>
                                                <source srcSet={slider.extra_large_url} media="(min-width: 1400px)" />
                                                <source srcSet={slider.large_device_url} media="(min-width: 768px)" />
                                                <source srcSet={slider.medium_device_url} media="(min-width: 576px)" />
                                                <img srcSet={slider.small_device_url} alt="" className="d-block img-fluid" />
                                            </picture>
                                        </div>
                                        :
                                        <div className="carousel-item">
                                            <picture>
                                                <source srcSet={slider.extra_large_url} media="(min-width: 1400px)" />
                                                <source srcSet={slider.large_device_url} media="(min-width: 768px)" />
                                                <source srcSet={slider.medium_device_url} media="(min-width: 576px)" />
                                                <img srcSet={slider.small_device_url} alt="" className="d-block img-fluid" />
                                            </picture>
                                        </div>
                                }
                            </div>

                        ))
                    }

                </div>
                <a className="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="sr-only">Previous</span>
                </a>
                <a className="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="sr-only">Next</span>
                </a>
            </div>
        </div>
    );
};

export default Slider;