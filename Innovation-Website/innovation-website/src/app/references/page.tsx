import styles from './page.module.css';

export default function Discussion() {
  return (
    <div>
        <div className={styles.body}>
          <h1 className={styles.text}>References</h1>
          <ol className={styles.list}>
            <li className={styles.text}>Hage, S., Francl, T., Bardou, E., & Söderqvist, J. (2024). <i>IKEA X Chalmers Kickoff</i> [PowerPoint Slides]. Digitalization and AI in practice, Chalmers Tekniska Högskola. September 5.</li>
            <li className={styles.text}>Teigland, R., & Heathcote-Fumador, I. (2024). <i>Design Thinking</i> [PowerPoint Slides]. Digitalization and AI in practice, Chalmers Tekniska Högskola. September 10.</li>
          </ol>
        </div>
    </div>
  );
}