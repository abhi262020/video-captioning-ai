interface CaptionCardProps {
  caption?: string;
}

export default function CaptionCard({
  caption,
}: CaptionCardProps) {
  if (!caption) return null;

  return (
    <div className="card">
      <h2>Generated Caption</h2>

      <p
        style={{
          fontSize: 18,
          lineHeight: 1.7,
        }}
      >
        {caption}
      </p>
    </div>
  );
}