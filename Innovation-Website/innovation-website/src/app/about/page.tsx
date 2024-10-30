import styles from'./page.module.css';
import '../../styles/globals.css';

export default function About() {
  return (
    <div className="page">
      <div className="center">
      <div className='coursediv'>
        <h1>Who are we?</h1>
      </div>

      <div className='coursediv'>
        <h2 className={styles.developersTitle}>Developers</h2>
      </div>

      <div className={styles.peopleSection}>
        <div className={styles.person}>
          <h3>Jonatan Markusson</h3>
          <p>Contact info: jomarkusson@gmail.com</p>
        </div>

        <div className={styles.person}>
          <h3>Max Dreifeldt</h3>
          <p>Contact info: maxdreifeldt02@gmail.com</p>
        </div>

        <div className={styles.person}>
          <h3>William Norland</h3>
          <p>Contact info: williamnorland@gmail.com</p>
        </div>

        <div className={styles.person}>
          <h3>Mandus Högberg</h3>
          <p>Contact info: mandus.hogberg@gmail.com</p>
        </div>

        <div className={styles.person}>
          <h3>Max Levin</h3>
          <p>Contact info: maxle@student.chalmers.se</p>
        </div>

        <div className={styles.person}>
          <h3>Alexander Muhr</h3>
          <p>Contact info: alle.muhr@gmail.com</p>
        </div>
      </div>

      <div className='coursediv'>
        <h2>TEK830 Digitalization and AI in practice</h2>
      </div>

      <div className={styles.imagediv}>
        <img src="chalmers_logo.png" alt="Chalmers Logo" className={styles.responsiveImage} />
      </div>
    </div>
    </div>
  );
}
