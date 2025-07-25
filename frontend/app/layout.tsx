// app/layout.tsx
import './globals.css';
import Navbar from '@/components/Navbar';

export const metadata = {
  title: 'Jobify',
  description: 'Simple LinkedIn clone with FastAPI + Next.js',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="p-4">{children}</main>
      </body>
    </html>
  );
}
