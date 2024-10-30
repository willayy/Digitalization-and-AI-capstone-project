"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import styles from './header.module.css';

const navItems = [
  { name: 'Design', path: '/design' },
  { name: 'Study', path: '/study' },
  { name: 'References', path: '/references' },
  { name: 'About us', path: '/about' }
];

export default function Header() {
  const pathname = usePathname();

  // Dynamically create the list of paths that should show the back button
  const pathsWithBackButton = navItems.map(item => item.path);
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
          {navItems.map((item, index) => (
            <li key={index}>
              <Link href={item.path} className={styles.navItem}>
                {item.name}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}