import '../styles/globals.css'; // Import your global styles
import type { Metadata } from 'next'; // Import Metadata type
import Header from '../components/Header/header'; // Import the Header component
import Footer from '../components/Footer/footer';
import { Analytics } from "@vercel/analytics/react"

export const metadata: Metadata = {
  title: 'SKAPA',
  description: 'Information about events, statistics, and more.', // Description for SEO
};

// Root layout component
export default function RootLayout({
  children,
}: {
  children: React.ReactNode; // Children prop to render page content
}) {
  return (
    <html lang="en"> {/* Set the language of the document */}
      <body>
        <Header /> {/* Render the Header */}
        <main className="content">{children}</main> {/* Render the main content of the page */}
        <Footer />
      </body>
    </html>
  );
}