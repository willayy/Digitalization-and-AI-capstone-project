'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className={styles.homePage}>

      <div className={styles.sectionOne}>
        <div className={styles.video}>
          <h1 className={styles.header}>Welcome to the future of marketing!</h1>
          <VideoPlayer videoSrc="spoderman.mp4" h2Ref={specificH2Ref} />
        </div>
      </div>

      <div className={styles.sectionTwo}>
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
          possible to keep using the same computer. The main cost of this product is the license for the AI itself
          which is why this product is referred to as a proof of concept.
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
    </div>
    );

}
