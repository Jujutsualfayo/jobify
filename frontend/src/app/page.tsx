// app/page.tsx

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-6 bg-gray-100">
      <h1 className="text-4xl font-bold text-gray-800 mb-4">Welcome to Jobify</h1>
      <p className="text-gray-600 text-lg mb-6">
        Your career journey starts here.
      </p>

      <div className="flex gap-4">
        <a
          href="/login"
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
        >
          Login
        </a>
        <a
          href="/register"
          className="bg-gray-300 text-gray-800 px-6 py-2 rounded hover:bg-gray-400 transition"
        >
          Register
        </a>
      </div>
    </div>
  );
}
