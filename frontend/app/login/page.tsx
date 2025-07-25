// app/login/page.tsx
"use client";

import { useState } from "react";
import axios from "@/lib/api";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [form, setForm] = useState({ email: "", password: "" });

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const res = await axios.post("/login", form);
      localStorage.setItem("token", res.data.access_token);
      router.push("/profile");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto space-y-4 py-20">
      <h2 className="text-2xl font-semibold">Login</h2>
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
      <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded">
        Login
      </button>
    </form>
  );
}
