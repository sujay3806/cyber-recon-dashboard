import { motion } from "framer-motion";
import { useState } from "react";

export default function ScanForm({ setScanData }) {
  const [ip, setIp] = useState("");

  const handleScan = () => {
    // 🔥 Demo Mode fake scan results
    const demoResults = [
      { port: 22, status: "OPEN" },
      { port: 80, status: "OPEN" },
      { port: 443, status: "OPEN" },
      { port: 21, status: "CLOSED" },
      { port: 25, status: "CLOSED" },
      { port: 3389, status: "CLOSED" },
    ];

    setScanData({
      target: ip,
      os_guess: "Linux/Unix",
      results: demoResults,
    });
  };

  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="p-5 rounded-xl backdrop-blur-md bg-card border border-neon shadow-xl"
    >
      <h2 className="text-neon text-xl mb-3">Port Scanner (Demo)</h2>

      <input
        className="w-full p-2 bg-black border border-neon rounded mb-3"
        placeholder="Enter IP (demo only)"
        onChange={(e) => setIp(e.target.value)}
      />

      <button
        onClick={handleScan}
        className="w-full p-2 bg-neon text-black rounded font-bold"
      >
        Scan
      </button>
    </motion.div>
  );
}
