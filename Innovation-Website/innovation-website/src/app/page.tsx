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
          
          <VideoPlayer videoSrc="SKAPA-Prototype-1.mp4" h2Ref={specificH2Ref} />
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
            access to.
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
            Based on IKEA's key values and goals we want to tailor SKAPA to be as simple as possible and grant use of the powerful 
            technology we have today. We want to highlight that a tool which is capable of generating images and eliminating the needs 
            of hiring set designers, photographers and the like will likely have a negative impact on job availability among those whose 
            expertise lies within any of these fields. In the end, an image generator would enable cut costs which might aid in reducing 
            prices in their goal to be affordable to anyone.
          </p>
          <br />

        </div>
      </div>

      <div className={styles.section}>
        <h2 className={styles.designTitle}>Study</h2>
        <div className={styles.textDiv}>

          <p>In order to make a product as good as possible, we wanted to interview our imagiend end users to aid our design process to make it as usable as 
            possible. We made an attempt to reach out to People & Culture at Inter IKEA AB but weren't able to get a reply within our time frame. Instead, we used
            ChatGPT to make up three different personas of the type of people we would have liked to interview. The three different personas had following jobs:
            Studio Designer, Equipment Technician and Product Stylist and Photogorapher</p>

          <p style={{marginTop: '1rem'}}>We asked the three personas 5 different questions:</p>  
            <ul style={{margin: '1rem'}}>
              <li>What do you work with? What is your role?</li>
              <li>Could you describe your workflow? If your workflow changes a lot, describe best and worst case scenarios.</li>
              <li>Could you describe a typical set of pictures? What backgrounds are used?</li>
              <li>What is the most prelavant problem in your workflow? (Regarding product pictures, if applicable)</li>
              <li>Would you appreciate an easy-to-use tool that allows the marketing team to write a prompt and generate a background using AI,
                onto which the product image can be placed, eliminating the need for a physical production set?
              </li>
            </ul>

          <p style={{marginBottom: '1rem'}}>
            <b>The Studio Designer</b> plans the set to enable smooth workflow for the technician and photographer on set. They communicate with the client
            to make as good as solution possible given the budget. The types of pictures are usually a mixture of plain backdrop and lifestyle photos.
            Space and budget are usually the two factors constraining the workflow balance. Given the last question, the studio designer had mixed feelings,
            expressing their understanding of the possibilites but were also worried about the need of her knowledge and expertise.
          </p>

          <p style={{marginBottom: '1rem'}}>
            <b>The Equipment Technician</b> installs cameras, lightning and similar on the set. The workflow is often great but can falter if something breaks
            or doesn't work as intended. They don't interfer much in regards to the artistic side and let the others decide how the pictures will turn out.
            The technician were positive to the ideas of the tool but emphasized the importance of things looking realisticly.
          </p>

          <p style={{marginBottom: '1rem'}}>
            <b>The Product Stylist and Photographer</b> styles the set by making smaller adjustments and captures the photographs. Sometimes they experience
            difficulties in capturing specific products which might have characteristics interfering with light just to name an example. They usually shoot plain 
            backdrops but also more lifestyle and environmental pictures too if that is what's asked for. Besides lightning interference, time management can also
            be an issue. The stylist also thought of the AI-tool to be useful and enables them to focus on the details. They highlighted the importance of everything 
            looking realisticly.
          </p>

          </div>
      </div>
    </div>
    );

}
