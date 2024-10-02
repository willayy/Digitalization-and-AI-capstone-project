'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className={styles.homePage}>

      <div className={styles.section}>
        <div className={styles.video}>
          <h1 className={styles.header}>Welcome to the future of marketing!</h1>
          <VideoPlayer videoSrc="spoderman.mp4" h2Ref={specificH2Ref} />
        </div>
      </div>

      <div className={styles.section}>
        <h2 className={styles.designTitle} ref={specificH2Ref}>The design behind</h2>
        <p className={styles.text}>
          When working on this project we have applied the three design thinking principles and tried to solve the
          problem that was given to us. Down below is an explanation on how we reasoned.
        </p>
        <br />
        <div className={styles.textDiv} >
          <h2> Usability </h2>
          <br />
          <p>
          This project deals with a very new technology that is difficult to understand without a deep knowledge of
          software development and AI. The end goal for this project is a product that requires little to no
          programming skills. That is why we in our research have reached out to people who work in design and
          marketing and asked what problems they face when creating ads etc. Our way of solving this have been to
          create a simple and sleek graphical interface that allows users with no prior AI experience to create
          prompts and generate images that are stored in a database and can be used by other clients.
          </p>
          <br />

          <h2> Feasibility </h2>
          <br />
          <p>
          This product is very scalable and therefore works more as a proof of concept than a finished AI tool as we
          are limited by factors such time, money and other resources. While the AI model might not be able to compete
          with the most common models on the market right now, that is something that IKEA very easily can fix with
          their resources. Our product is similar to a computer in a way. By replacing say a graphical component it is
          possible to keep using the same computer. The same is true for our product by replacing the AI model.
          The main cost of this product is the license for the AI itself which is why this product is referred to as a
          proof of concept.
          </p>
          <br />

          <h2> Viability </h2>
          <br />
          <p>
          We have looked at key values for IKEA and worked a lot towards simplicity and staying relevant in a modern
          world. AI is very modern technology and have become a huge part of society. We are trying to make that
          technology more easily accessible for IKEA. IKEA works a lot towards simplicity which is a key element to
          our product. One sustainability issue that we have talked a lot about is the affect that training AI models
          have on the climate. training large models requires a lot of energy and our conclusion is that IKEA sits in
          a position to demand sustainably trained models and try to push in the right direction.
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

          <p>
            <b style={{marginTop: '1rem'}}>The Studio Designer</b> plans the set to enable smooth workflow for the technician and photographer on set. They communicate with the client
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
