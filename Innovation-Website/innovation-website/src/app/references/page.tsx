import styles from './page.module.css';
import '../../styles/globals.css';

export default function References() {
  return (
    <div>
        <div className="page">
          <div className="center" style={{height: '75vh'}}>
            <h1 className={styles.text}><b>References</b></h1>
            <ol className={styles.list}>
              <li className={styles.text}>Hage, S., Francl, T., Bardou, E., & Söderqvist, J. (2024). <i>IKEA X Chalmers Kickoff</i> [PowerPoint Slides]. Digitalization and AI in practice, Chalmers Tekniska Högskola. September 5.</li>
              <li className={styles.text}>Teigland, R., & Heathcote-Fumador, I. (2024). <i>Design Thinking</i> [PowerPoint Slides]. Digitalization and AI in practice, Chalmers Tekniska Högskola. September 10.</li>
              <li className={styles.text}><a href="https://www.vecteezy.com/free-photos/ikea">Ikea Stock photos by Vecteezy</a></li>            
            </ol>
          </div>
        </div>
    </div>
  );
}