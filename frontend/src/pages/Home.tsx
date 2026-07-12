import { useState } from "react";

import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadVideo";
import VideoPreview from "../components/VideoPreview";
import LoadingSpinner from "../components/LoadingSpinner";
import CaptionCard from "../components/CaptionCard";
import TranscriptCard from "../components/TranscriptCard";
import Footer from "../components/Footer";

import { generateCaption } from "../services/api";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const [caption, setCaption] = useState("");
  const [transcript, setTranscript] = useState("");

  const handleGenerate = async () => {
    if (!file) return;

    setLoading(true);

    try {
      const data = await generateCaption(file);

      setCaption(data.caption);
      setTranscript(data.transcript);

    } catch (err) {
      alert("Failed to generate caption.");
    }

    setLoading(false);
  };

  return (
    <>
      <Navbar />

      <div
        style={{
          maxWidth: 900,
          margin: "auto",
        }}
      >
        <UploadBox onFileChange={setFile} />

        <VideoPreview file={file} />

        <button
          onClick={handleGenerate}
          disabled={!file || loading}
          style={{
            marginTop: 20,
            padding: "12px 30px",
            fontSize: 18,
          }}
        >
          {loading ? "Generating..." : "Generate Caption"}
        </button>

        <LoadingSpinner loading={loading} />

        <CaptionCard caption={caption} />

        <TranscriptCard transcript={transcript} />
      </div>

      <Footer />
    </>
  );
}