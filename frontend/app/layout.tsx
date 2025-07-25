// app/layout.tsx
import "./globals.css";
import { ReactNode } from "react";
import Navbar from "@/components/Navbar";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-900">
        <Navbar />
        <main className="max-w-4xl mx-auto p-6">{children}</main>
      </body>
    </html>
  );
}
