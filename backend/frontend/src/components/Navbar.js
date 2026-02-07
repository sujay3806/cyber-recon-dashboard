import { motion } from "framer-motion";

export default function Navbar() {
  return (
    <div className="text-center mb-6">
      
      {/* Title */}
      <motion.div
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl font-bold text-neon"
      >
        🔐 Cyber Recon Dashboard
      </motion.div>

      {/* Demo Notice */}
      <div className="text-sm text-yellow-400 mt-2">
        ⚠️ Demo Mode Enabled — Simulated scan results
      </div>

      {/* Download Button */}
      <a
        href="https://github.com/sujay3806/cyber-recon-dashboard/raw/main/local_port_scanner.zip"
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-block bg-green-500 hover:bg-green-400 text-black font-semibold px-5 py-2 rounded-lg shadow-lg transition transform hover:scale-105"
      >
        ⬇ Download Local Scanner
      </a>

    </div>
  );
}
