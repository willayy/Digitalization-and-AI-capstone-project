import styles from'./page.module.css';

export default function About() {
  return (
    <div className={styles.aboutPage}>
        <div>
          <h1>About Us</h1>
          <p>This is the about page.</p>
        </div>

        <div>
           <h2 className={styles.developersTitle}>Utvecklare</h2>
        </div>

        <div className={styles.peopleSection}>

            <div className={styles.person}>
                <h3>Jonatan Markusson</h3>
                <p>Kontaktinfo: jomarkusson@gmail.com</p>
            </div>

            <div className={styles.person}>
                <h3>Max Dreifeldt</h3>
                <p>Kontaktinfo: maxdreifeldt02@gmail.com</p>
            </div>

            <div className={styles.person}>
                <h3>William Norland</h3>
                <p>Kontaktinfo: williamnorland@gmail.com</p>
            </div>

            <div className={styles.person}>
                <h3>Mandus Högberg</h3>
                <p>Kontaktinfo: mandus.hogberg@gmail.com</p>
            </div>
            <div className={styles.person}>
                <h3>Max Levin</h3>
                <p>Kontaktinfo: ...@gmail.com</p>
            </div>
            <div className={styles.person}>
                <h3>Alexander Muhr</h3>
                <p>Kontaktinfo: alle.muhr@gmail.com</p>
            </div>
        <div className={styles.imagediv}>
            <img src="chalmers_logo.png" alt="Chalmers Logo" />
        </div>

        </div>
    </div>
  );
}
