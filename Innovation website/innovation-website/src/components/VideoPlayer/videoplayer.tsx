'use client';

import React, { useRef } from 'react';

interface VideoPlayerProps {
  videoSrc: string;  //String name of video to be played
  h2Ref: React.RefObject<HTMLHeadingElement>;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ videoSrc, h2Ref }) => {
  const scrollToH2 = () => {
    if (h2Ref.current) {
      h2Ref.current.scrollIntoView({ behavior: 'smooth' });
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