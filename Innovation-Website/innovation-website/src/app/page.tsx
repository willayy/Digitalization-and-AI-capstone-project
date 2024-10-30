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
        <h2 ref={specificH2Ref}  style={{ marginBottom: '30px' }}>The design behind</h2>
        <p className="paragraph">
          SKAPA is an AI-driven tool with the purpose of generating photorealistic images in style with IKEA's catalog to reduce the amount
          of resources needed to create images for new products. Continue writing
        </p>
        </div>  
        
        <div className={styles.viddiv}>
          <iframe src="Website_pres.pdf" width="600" height="400" ></iframe>

          <VideoPlayer videoSrc="VSieaMqd-iY" h2Ref={specificH2Ref}/>
        </div>

      </div>
    </div>

    );

}
