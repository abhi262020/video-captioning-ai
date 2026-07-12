import cv2


def extract_frame(video_path):

    cap = cv2.VideoCapture(
        video_path
    )

    ret, frame = cap.read()

    frame_path = "frame.jpg"

    if ret:
        cv2.imwrite(
            frame_path,
            frame
        )

    cap.release()

    return frame_path