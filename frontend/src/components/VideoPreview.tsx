interface VideoPreviewProps {
  file?: File | null;
}

export default function VideoPreview({
  file,
}: VideoPreviewProps) {
  if (!file) return null;

  return (
    <div className="card">
      <h2>Video Preview</h2>

      <video
        controls
        width="100%"
        src={URL.createObjectURL(file)}
      />
    </div>
  );
}