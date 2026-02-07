export default function ResultsTable({ data }) {
  if (!data) return null;

  // Important ports to show even if closed
  const importantClosed = [21, 25, 3389];

  const filtered = data.results.filter(r =>
    r.status === "OPEN" || importantClosed.includes(r.port)
  );

  return (
    <div className="mt-6 p-5 rounded-xl backdrop-blur-md bg-card border border-neon">
      <h2 className="text-neon mb-3">Scan Results (Demo Mode)</h2>

      <div className="max-h-64 overflow-y-auto pr-2">
        <table className="w-full text-left">
          <thead className="sticky top-0 bg-black">
            <tr>
              <th>Port</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((r, i) => (
              <tr key={i} className="border-b border-gray-700">
                <td>{r.port}</td>
                <td className={r.status === "OPEN" ? "text-green-400" : "text-red-400"}>
                  {r.status}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
