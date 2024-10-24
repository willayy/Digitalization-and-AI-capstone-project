'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className={styles.homePage}>

      <div className={styles.section}>
          <h1 className={styles.header}>Welcome to the future of marketing!</h1>
        <div className={styles.video}>
          
          <VideoPlayer videoSrc="VSieaMqd-iY" h2Ref={specificH2Ref} />

          <iframe src="Second_Pitch_Team12.pdf" width="600" height="400"></iframe>

          <VideoPlayer videoSrc="VSieaMqd-iY" h2Ref={specificH2Ref} />
          
        </div>
      </div>


      <div className={styles.section}>
        <h2 className={styles.designTitle} ref={specificH2Ref}>The design behind</h2>
    
        <br />
        <div className={styles.textDiv} >
          <h2> Usability </h2>
          <br />
          <p>
            The idea of SKAPA is to create a tool capable of generating environmental and lifestyle images based on
            an input image or 3D-model. We want to accomplish this as it enables IKEA an ability to adapt their images 
            based on the market which they are meant to be used towards. The main goal of SKAPA is to produce these images 
            in a european environment with focus on living rooms and relaxation areas. However, we believe a tool like 
            this, given enough sample data, would really work for any type of environment. Our goal is to create a very simple
            and straight forward graphical interface so that anyone could use the software regardless of skills in either photography
            or software development. Any images created will be stored in a database which can be accessed by clients IKEA wish
            access to. Temp text.
          </p>
          <br />

          <h2> Feasibility </h2>
          <br />
          <p>
            While our AI model in the current state, and most likely later state for the final delivery, is not able to compete with
            other image generators on the market, we still want to give IKEA an idea of what is feasible, especially considering they
            have additional resources. And like we said before, we believe a model like this could extend beyond our current set of 
            environmental parameters. A lot of sample data already exists as we believe IKEA would appreciate if the model could produce 
            similar images to those already found today on their website. Our key takeaway here is it might not be feasible for us to 
            create something like this with our limited sources in terms of funding and time, but it would most definitely be possible 
            for a sizeable company to do so.
          </p>
          <br />

          <h2> Viability </h2>
          <br />
          <p>
            Based on IKEAs key values and goals we want to tailor SKAPA to be as simple as possible and grant use of the powerful 
            technology we have today. We want to highlight that a tool which is capable of generating images and eliminating the needs 
            of hiring set designers, photographers and the like will likely have a negative impact on job availability among those whose 
            expertise lies within any of these fields. In the end, an image generator would enable cut costs which might aid in reducing 
            prices in their goal to be affordable to anyone.
          </p>
          <br />

        </div>
      </div>
    </div>
    );

}
