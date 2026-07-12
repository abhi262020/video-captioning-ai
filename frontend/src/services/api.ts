const API_URL = "http://127.0.0.1:8000";


export async function generateCaption(
    video: File
) {

    const formData = new FormData();


    formData.append(
        "video",
        video
    );


    const response = await fetch(
        `${API_URL}/caption`,
        {
            method: "POST",
            body: formData,
        }
    );


    if (!response.ok) {

        throw new Error(
            "Failed to generate caption"
        );
    }


    return await response.json();
}