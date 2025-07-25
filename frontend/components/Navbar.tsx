// components/Navbar.tsx
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow px-6 py-4 flex justify-between items-center">
      <Link href="/" className="text-xl font-bold">Jobify</Link>
      <div className="space-x-4">
        <Link href="/login">Login</Link>
        <Link href="/register">Register</Link>
        <Link href="/profile">Profile</Link>
      </div>
    </nav>
  );
}
