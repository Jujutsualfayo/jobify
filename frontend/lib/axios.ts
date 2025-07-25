// lib/axios.ts
import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000", // Backend base URL
  withCredentials: true,            // For cookie/session auth (if used)
});

export default instance;
