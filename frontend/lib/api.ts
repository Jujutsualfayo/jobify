// lib/api.ts
import axios from "axios";

const instance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
});

export default instance;
