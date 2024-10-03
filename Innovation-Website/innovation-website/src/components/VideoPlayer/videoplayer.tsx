'use client';

//import React, { useRef } from 'react';
import YouTube from 'react-youtube';

interface VideoPlayerProps {
  videoSrc: string; // YouTube video ID
  h2Ref: React.RefObject<HTMLHeadingElement>;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ videoSrc, h2Ref }) => {
  const scrollToH2 = () => {
    if (h2Ref.current) {
      const offset = 100; // Adjust the offset value to set the distance between the h2 and the header
      const h2Position = h2Ref.current.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: h2Position, behavior: 'smooth' });
    }
  };

  // Function to be called when the video ends
  const onVideoEnd = () => {
    scrollToH2();
  };

  // YouTube player options
  const videoOptions = {
    height: '500',
    width: '800',
    playerVars: {
      autoplay: 1,
      mute: 1,
      vq: "hd1080",
    },
  };

  return (
    <>
      <YouTube
        videoId={videoSrc} // YouTube video ID
        opts={videoOptions}
        onEnd={onVideoEnd} // Auto-scroll when the video ends
      />
    </>
  );
};

export default VideoPlayer;