'use client'
import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';
import React, { useRef } from 'react';

export default function Home() {

  const specificH2Ref = useRef<HTMLHeadingElement | null>(null);
  return (
    <div className={styles.homePage}>
          <h1>Welcome to the future of marketing!</h1>
          <VideoPlayer videoSrc="spoderman.mp4" h2Ref={specificH2Ref} />

          <h2 ref={specificH2Ref}>The design behind</h2>

          <p>
            Supercool text about design thinking principles and how good we are at making stuff.
          </p>
          <p>hihi</p>
        </div>
      );

}
