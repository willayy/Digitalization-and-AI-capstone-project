import styles from './page.module.css';
import VideoPlayer from '../components/VideoPlayer/videoplayer';

export default function Home() {
  return (
    <div className={styles.homePage}>
      <h1>Welcome to the future of marketing!</h1>
      <VideoPlayer videoSrc="spoderman.mp4" />

      <h2>
      The design behind
      </h2>

      <p>supercool text about design thinking principles and how good we are at making stuff.</p>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <brv />
      <br />
      <br />
      <br />
      <p>hihi</p>
    </div>
  );
}
