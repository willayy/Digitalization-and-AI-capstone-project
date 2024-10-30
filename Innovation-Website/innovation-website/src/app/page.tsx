'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className="page">
      <div className="center">

        <div className={styles.section}>
          <h2>Welcome to the future of marketing!</h2>
          <div className={styles.video}>
            <VideoPlayer videoSrc="BTCI5hC2jnQ" h2Ref={specificH2Ref} />
          </div>
        </div>

        <div className={styles.vcon}>
        <h2 ref={specificH2Ref}  style={{ marginBottom: '30px' }}>What is SKAPA?</h2>
        <p className="paragraph">
          SKAPA is an AI-driven tool with the purpose of generating photorealistic images in style with IKEA's catalog to reduce the amount
          of resources needed to create images for new products. The idea is to enable quick generation of environmental and seasonal photos for 
          new product releases or adding seasonal environments for existing products. 
        </p>
        <p className="paragraph">
          To ensure images are within IKEA's style, SKAPA is connected to a database with large amounts of
          sample date already existing from IKEA's current website. When generating an image, the idea is that the user can rate, accept and reject an image 
          which will determine how much the image will be used for further machine learning.
        </p>
        </div>  
        
        <div className={styles.viddiv}>
          <iframe src="Website_pres.pdf" width="600" height="400" ></iframe>

          <VideoPlayer videoSrc="0dcrnavrgHA" h2Ref={specificH2Ref}/>
        </div>

      </div>
    </div>

    );

}
