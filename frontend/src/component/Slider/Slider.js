import React from 'react';
import image1 from '../../static/images/slider/2000x400.png'
import image2 from '../../static/images/slider/1400x400.png'
import image3 from '../../static/images/slider/800x400.png';
import image4 from '../../static/images/slider/600x400.png'
import image5 from '../../static/images/slider/mac1920x597.jpg'
import image6 from '../../static/images/slider/mac1400x400.jpg'
import image7 from '../../static/images/slider/mac800x400px.jpg'
import image8 from '../../static/images/slider/mac600x400.jpg'


const Slider = () => {
    return (
        <div>
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <picture>
                            <source srcSet={image1} media="(min-width: 1400px)" />
                            <source srcSet={image2} media="(min-width: 768px)" />
                            <source srcSet={image3} media="(min-width: 576px)" />
                            <img srcSet={image4} alt="" className="d-block img-fluid" />
                        </picture>
                    </div>
                    <div class="carousel-item">
                        <picture>
                        <source srcSet={image5} media="(min-width: 1400px)" />
                            <source srcSet={image6} media="(min-width: 768px)" />
                            <source srcSet={image7} media="(min-width: 576px)" />
                            <img srcSet={image8} alt="" className="d-block img-fluid" />
                        </picture>
                    </div>
                    <div class="carousel-item">
                        <picture>
                            <source srcSet={image1} media="(min-width: 1400px)" />
                            <source srcSet={image2} media="(min-width: 768px)" />
                            <source srcSet={image3} media="(min-width: 576px)" />
                            <img srcSet={image4} alt="" className="d-block img-fluid" />
                        </picture>
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
    );
};

export default Slider;