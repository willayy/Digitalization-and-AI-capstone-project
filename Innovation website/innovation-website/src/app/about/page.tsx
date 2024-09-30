import styles from'./page.module.css';

export default function About() {
  return (
    <div className={styles.aboutPage}>
      <div>
        <h1>Who are we?</h1>
      </div>

      <div>
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

      <div>
        <h2>TEK830</h2>
      </div>

      <div className={styles.imagediv}>
        <img src="chalmers_logo.png" alt="Chalmers Logo" />
      </div>
    </div>
  );
}
