interface TranscriptCardProps {
  transcript?: string;
}

export default function TranscriptCard({
  transcript,
}: TranscriptCardProps) {
  if (!transcript) return null;

  return (
    <div className="card">
      <h2>Transcript</h2>

      <pre
        style={{
          whiteSpace: "pre-wrap",
          overflowX: "auto",
        }}
      >
        {transcript}
      </pre>
    </div>
  );
}