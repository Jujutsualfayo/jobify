// app/register/page.tsx
"use client";

import { useState } from "react";
import axios from "@/lib/api";
import { useRouter } from "next/navigation";

export default function RegisterPage() {
  const router = useRouter();
  const [form, setForm] = useState({ name: "", email: "", password: "" });

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      await axios.post("/register", form);
      router.push("/login");
    } catch (err) {
      alert("Registration failed");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto space-y-4 py-20">
      <h2 className="text-2xl font-semibold">Register</h2>
      <input
        type="text"
        placeholder="Full Name"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
        className="w-full border px-4 py-2 rounded"
      />
      <input
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={(e) => setForm({ ...form, email: e.target.value })}
        className="w-full border px-4 py-2 rounded"
      />
      <input
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={(e) => setForm({ ...form, password: e.target.value })}
        className="w-full border px-4 py-2 rounded"
      />
      <button type="submit" className="w-full bg-green-600 text-white py-2 rounded">
        Register
      </button>
    </form>
  );
}
