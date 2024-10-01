'use client';

//import React, { useRef } from 'react';

interface VideoPlayerProps {
  videoSrc: string;  //String name of video to be played
  h2Ref: React.RefObject<HTMLHeadingElement>;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ videoSrc, h2Ref }) => {
  const scrollToH2 = () => {
    if (h2Ref.current) {
      const headerHeight = 90; // Change this to the height of your header
      const h2Position = h2Ref.current.getBoundingClientRect().top + window.scrollY;
      const offsetPosition = h2Position - headerHeight; // Subtract the header height for offset
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth' // Smooth scroll animation
      });
    }
  };

   return (
      <>
        <video width="600" controls autoPlay muted onEnded={scrollToH2}>
          <source src={videoSrc} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </>
    );
  };

  export default VideoPlayer;