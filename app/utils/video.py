import cv2
import os


def extract_frames(video_path, output_folder="temp_frames", interval=30):

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    count = 0
    saved = []

    while True:

        success, frame = cap.read()

        if not success:
            break

        if count % interval == 0:

            filename = os.path.join(
                output_folder,
                f"frame_{count}.jpg"
            )

            cv2.imwrite(filename, frame)

            saved.append(filename)

        count += 1

    cap.release()

    return saved