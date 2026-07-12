import React from "react";

interface Props {
  video: File | null;
}

const VideoPlayer: React.FC<Props> = ({ video }) => {
  if (!video) return null;

  return (
    <video
      controls
      width="700"
      src={URL.createObjectURL(video)}
      style={{
        marginTop: 20,
      }}
    />
  );
};

export default VideoPlayer;