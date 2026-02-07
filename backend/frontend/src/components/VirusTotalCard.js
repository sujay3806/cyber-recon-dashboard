import { useState } from "react";
import axios from "axios";

export default function VirusTotalCard() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);

  const scanURL = async () => {
  try {
    const res = await axios.get(
      `https://cyber-recon-dashboard.onrender.com/scan-url?url=${url}`
    );
    setData(res.data.analysis);
  } catch (err) {
    if (err.response?.status === 429) {
      alert("VirusTotal API limit reached. Please wait a minute and try again.");
    } else {
      alert("Error scanning URL.");
    }
  }
};


  return (
    <div className="p-4 rounded-xl backdrop-blur-md bg-card border border-purple-500">
      <h2 className="text-purple-400 font-semibold mb-2">🛡️ VirusTotal URL Scan</h2>

      <input
        className="w-full p-2 bg-black border border-purple-500 rounded mb-2"
        placeholder="Enter URL"
        onChange={(e) => setUrl(e.target.value)}
      />
      <button
        onClick={scanURL}
        className="w-full bg-purple-500 text-black p-2 rounded font-bold"
      >
        Scan
      </button>

      {data && (
        <div className="mt-3 text-sm">
          Malicious: {data.malicious}<br/>
          Suspicious: {data.suspicious}<br/>
          Risk Level: <span className="font-bold">{data.risk_level}</span>
        </div>
      )}
    </div>
  );
}
