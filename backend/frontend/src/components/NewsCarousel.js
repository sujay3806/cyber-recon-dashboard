import { useEffect, useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";

export default function NewsCarousel() {
  const [news, setNews] = useState([]);
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    axios
      .get("https://cyber-recon-dashboard.onrender.com/news")
      .then((res) => setNews(res.data.news));
  }, []);

  if (news.length === 0) return null;

  return (
    <div className="rounded-xl backdrop-blur-md bg-card border border-neon p-4">

      {/* Heading */}
      <div className="text-neon text-lg font-semibold mb-1">
        📰 Latest Cybersecurity Threat News (Live Feed)
      </div>

      {/* Description */}
      <p className="text-xs text-gray-400 mb-3">
        Live cyber threat headlines from global security news sources. Hover to pause and click to read.
      </p>

      {/* Scrolling News */}
      <div
        className="overflow-hidden h-32 flex items-center relative"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <motion.div
          className="flex gap-16 text-lg"
          animate={{ x: isHovered ? 0 : ["0%", "-100%"] }}
          transition={{
            duration: 45,  // slower readable speed
            repeat: Infinity,
            ease: "linear",
          }}
        >
          {news.concat(news).map((item, i) => (
            <a
              key={i}
              href={item.url}
              target="_blank"
              rel="noreferrer"
              className="min-w-max hover:text-neon transition duration-300"
            >
              📰 {item.title}
              <span className="ml-2 text-xs text-gray-400">({item.source})</span>
            </a>
          ))}
        </motion.div>

        <div className="absolute top-1 right-2 text-xs text-gray-500">
          Hover to pause
        </div>
      </div>
    </div>
  );
}
