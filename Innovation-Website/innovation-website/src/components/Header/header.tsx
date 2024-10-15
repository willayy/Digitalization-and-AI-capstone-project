"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import styles from './header.module.css';

export default function Header() {

  const pathname = usePathname();
  const pathsWithBackButton = ['/references', '/about'];
  const showBackButton = pathsWithBackButton.includes(pathname);

  return (
    <header className={styles.headerContainer}>

      {showBackButton && (
        <div>
          <Link href="/" className={styles.navItem}>←</Link>
        </div>
      )}

      <h1 className={styles.headerTitle}>
        <Link href="/">SKAPA</Link>
      </h1>

      <nav className={styles.nav}>
        <ul style={{ display: 'flex', gap: 0 }}>
          <li>
            <Link href="/references" className={styles.navItem}>References</Link>
          </li>
          <li>
            <Link href="/design" className={styles.navItem}>Design</Link>
          </li>
          <li>
            <Link href="/study" className={styles.navItem}>Study</Link>
          </li>
          <li>
            <Link href="/about" className={styles.navItem}>About us</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}