'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className={styles.homePage}>

        <div className={styles.video}>
          <h1>Welcome to the future of marketing!</h1>
          <VideoPlayer videoSrc="spoderman.mp4" h2Ref={specificH2Ref} />
        </div>

        <div>
          <h2 className={styles.designTitle} ref={specificH2Ref}>The design behind</h2>
          <p>
            Supercool text about design thinking principles and how good we are at making stuff.
          </p>
          <br />
          <div >
            <h2> Design 1 </h2>
            <br />
            <p>
            thing about design 1
            </p>
            <br />

            <h2> Design 2 </h2>
            <br />
            <p>
            thing about design 2
            </p>
            <br />

            <h2> Design 3 </h2>
            <br />
            <p>
            thing about design 3
            </p>
            <br />

          </div>
        </div>
    </div>
    );

}
