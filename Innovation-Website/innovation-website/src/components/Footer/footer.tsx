"use client";

import Link from 'next/link';
import styles from './footer.module.css';

export default function Footer() {



  return (
    <footer className={styles.footerContainer}>

      <h1 className={styles.footerTitle}>
        <Link href="/">SKAPA</Link>
      </h1>

      <div className={styles.containerdiv}>
        <div className={styles.smalldiv}>
          <h3 className={styles.footerh3}>Homepage</h3> 
            <Link href="/" className={styles.navItem}>Home</Link>
        </div>

        <div className={styles.smalldiv}>
          <h3 className={styles.footerh3}>Made by</h3>
            <Link href="/about" className={styles.navItem}>Team 12</Link>
        </div>

        <div className={styles.smalldiv}>
          <h3 className={styles.footerh3}>Why this product</h3> 
            <Link href="/study" className={styles.navItem}>Study</Link>
        </div>

        <div className={styles.smalldiv}>
          <h3 className={styles.footerh3}>Our sources</h3> 
            <Link href="/references" className={styles.navItem}>References</Link>
        </div>

        <div className={styles.smalldiv}>
          <h3 className={styles.footerh3}>More on the product</h3> 
            <Link href="/design" className={styles.navItem}>Design</Link>
        </div>



      </div>
    </footer>
  );
}