export default function VulnPanel({ data }) {
  if (!data) return null;

  const vulns = data.results.flatMap(r => r.vulnerabilities || []);

  return (
    <div className="p-4 rounded-xl backdrop-blur-md bg-card border border-red-500">
      <h2 className="text-red-400 font-semibold mb-2">🚨 Detected Vulnerabilities</h2>

      {vulns.length === 0 ? (
        <p className="text-gray-400 text-sm">No known CVEs found.</p>
      ) : (
        <ul className="text-sm space-y-2 max-h-40 overflow-y-auto">
          {vulns.map((v, i) => (
            <li key={i}>
              <span className="text-red-400 font-bold">{v.cve_id}</span> — {v.severity}
              <div className="text-gray-400">{v.description}</div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
