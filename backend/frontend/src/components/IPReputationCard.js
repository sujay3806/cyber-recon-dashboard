import { useState } from "react";
import axios from "axios";

export default function IPReputationCard() {
  const [ip, setIp] = useState("");
  const [data, setData] = useState(null);

  const checkIP = async () => {
    const res = await axios.get(
      `https://cyber-recon-dashboard.onrender.com/ip-reputation?ip=${ip}`
    );
    setData(res.data.reputation);
  };

  return (
    <div className="p-4 rounded-xl backdrop-blur-md bg-card border border-yellow-500">
      <h2 className="text-yellow-400 font-semibold mb-2">🌍 IP Reputation</h2>

      <input
        className="w-full p-2 bg-black border border-yellow-500 rounded mb-2"
        placeholder="Enter IP"
        onChange={(e) => setIp(e.target.value)}
      />
      <button
        onClick={checkIP}
        className="w-full bg-yellow-500 text-black p-2 rounded font-bold"
      >
        Check
      </button>

      {data && (
        <div className="mt-3 text-sm">
          Risk Level: <span className="font-bold">{data.risk_level}</span><br/>
          Reports: {data.reports}<br/>
          Confidence: {data.confidence_score}%
        </div>
      )}
    </div>
  );
}
