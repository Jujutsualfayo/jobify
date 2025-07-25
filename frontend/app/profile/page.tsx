export default function ProfilePage() {
  return (
    <div className="min-h-screen p-8 bg-gray-100">
      <div className="max-w-3xl mx-auto bg-white rounded shadow p-6">
        <h1 className="text-3xl font-bold mb-4">Your Profile</h1>
        <p>Full Name: John Doe</p>
        <p>Email: john@example.com</p>
        <p>Skills: React, FastAPI, PostgreSQL</p>
        {/* Later we’ll fetch this from the API */}
      </div>
    </div>
  );
}
