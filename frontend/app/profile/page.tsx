// app/profile/page.tsx
"use client";

import { useEffect, useState } from "react";
import type { AxiosResponse } from "axios";
import axios from "@/lib/api";

export default function ProfilePage() {
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    axios
      .get("/users/me", { headers: { Authorization: `Bearer ${token}` } })
      .then((res: AxiosResponse) => setProfile(res.data))
      .catch(() => alert("Please login again."));
  }, []);

  if (!profile) return <p>Loading...</p>;

  return (
    <div className="max-w-md mx-auto py-20">
      <h2 className="text-2xl font-bold mb-4">Welcome, {profile.name}</h2>
      <p>Email: {profile.email}</p>
    </div>
  );
}
