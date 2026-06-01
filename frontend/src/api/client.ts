const BASE_URL = "http://localhost:8000";

export async function chatRequest(payload) {
    const res = await fetch(`${BASE_URL}/api/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    return await res.json();
}

export async function uploadFile(file, kbName = "default") {
    const form = new FormData();
    form.append("file", file);
    form.append("kb_name", kbName);

    const res = await fetch(`${BASE_URL}/api/upload`, {
        method: "POST",
        body: form
    });

    return await res.json();
}