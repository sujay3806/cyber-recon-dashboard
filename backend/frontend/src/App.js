import Navbar from "./components/Navbar";
import ScanForm from "./components/ScanForm";
import ResultsTable from "./components/ResultsTable";
import NewsCarousel from "./components/NewsCarousel";
import VulnPanel from "./components/VulnPanel";
import IPReputationCard from "./components/IPReputationCard";
import VirusTotalCard from "./components/VirusTotalCard";
import { useState } from "react";

function App() {
  const [scanData, setScanData] = useState(null);

  return (
    <div className="min-h-screen p-6 bg-black text-white">
      <Navbar />

      <div className="grid grid-cols-3 gap-6 mt-6">
        <ScanForm setScanData={setScanData} />
        <div className="col-span-2">
          <NewsCarousel />
        </div>
      </div>

      {scanData && <ResultsTable data={scanData} />}

      <div className="grid grid-cols-3 gap-6 mt-6">
        <VulnPanel data={scanData} />
        <IPReputationCard />
        <VirusTotalCard />
      </div>
    </div>
  );
}

export default App;
