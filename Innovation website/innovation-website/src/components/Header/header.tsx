"use client";

import Link from 'next/link';
import styles from './header.module.css';

export default function Header() {
  return (
    <header className={styles.headerContainer}>
      <h1 className={styles.headerTitle}>IkeAI</h1>
      <nav className={styles.nav}>
        <ul style={{ display: 'flex', gap: '1.5rem' }}>
          <li>
            <Link href="/">Demo</Link>
          </li>
          <li>
            <Link href="/references">References</Link>
          </li>
          <li>
            <Link href="/about">About us</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}