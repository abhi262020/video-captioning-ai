interface UploadBoxProps {
  onFileChange: (file: File | null) => void;
}

export default function UploadBox({
  onFileChange,
}: UploadBoxProps) {
  return (
    <div className="card">
      <h2>Upload Video</h2>

      <input
        type="file"
        accept="video/*"
        onChange={(e) =>
          onFileChange(
            e.target.files ? e.target.files[0] : null
          )
        }
      />
    </div>
  );
}