export default function Message({ msg }) {

    const isUser = msg.role === "user";

    return (
        <div className={`message ${isUser ? "user" : "assistant"}`}>

            <div className="bubble">

                {msg.content}

                {msg.mode && (
                    <div style={{
                        fontSize: 11,
                        opacity: 0.5,
                        marginTop: 6
                    }}>
                        {msg.mode.toUpperCase()}
                    </div>
                )}

                {msg.sources?.length > 0 && (
                    <div style={{
                        fontSize: 11,
                        marginTop: 6,
                        color: "#10a37f"
                    }}>
                        sources: {msg.sources.join(", ")}
                    </div>
                )}

            </div>

        </div>
    );
}