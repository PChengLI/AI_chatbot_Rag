import { useState } from "react";
import { uploadFile } from "../api/client";

export default function UploadPanel() {

    const [file, setFile] = useState(null);
    const [kbName, setKbName] = useState("default");
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {

        if (!file) return;

        setLoading(true);

        try {
            await uploadFile(file, kbName);
            alert("Upload success");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="sidebar-card">

            <div className="sidebar-title">
                Knowledge Base
            </div>

            <div className="sidebar-section">

                <input
                    type="file"
                    onChange={(e) => setFile(e.target.files[0])}
                />

                <input
                    className="sidebar-input"
                    value={kbName}
                    onChange={(e) => setKbName(e.target.value)}
                    placeholder="KB name"
                />

                <button
                    className="sidebar-button"
                    onClick={handleUpload}
                    disabled={loading}
                >
                    {loading ? "Uploading..." : "Upload"}
                </button>

            </div>
        </div>
    );
}