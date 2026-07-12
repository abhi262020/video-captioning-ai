interface LoadingSpinnerProps {
  loading: boolean;
}

export default function LoadingSpinner({
  loading,
}: LoadingSpinnerProps) {
  if (!loading) return null;

  return (
    <div
      style={{
        marginTop: 30,
        textAlign: "center",
      }}
    >
      <h3>⏳ Processing Video...</h3>

      <p>
        Extracting audio, analyzing frames and generating
        caption...
      </p>
    </div>
  );
}