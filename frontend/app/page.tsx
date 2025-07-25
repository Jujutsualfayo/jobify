// app/page.tsx
export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-blue-100 flex items-center justify-center px-4">
      <div className="max-w-2xl text-center">
        <h1 className="text-5xl md:text-6xl font-extrabold text-gray-800 mb-6 leading-tight">
          Welcome to <span className="text-blue-600">Jobify</span>
        </h1>
        <p className="text-lg md:text-xl text-gray-700 mb-8">
          Connect with top professionals. Find your next opportunity. Build your future today.
        </p>
        <div className="flex justify-center gap-4">
          <a
            href="/register"
            className="bg-blue-600 text-white px-6 py-3 rounded-full text-lg font-semibold hover:bg-blue-700 transition"
          >
            Get Started
          </a>
          <a
            href="/login"
            className="bg-white text-blue-600 border border-blue-600 px-6 py-3 rounded-full text-lg font-semibold hover:bg-blue-50 transition"
          >
            Sign In
          </a>
        </div>
      </div>
    </div>
  );
}
