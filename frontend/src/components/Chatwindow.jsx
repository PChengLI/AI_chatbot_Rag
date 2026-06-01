import { useEffect, useRef, useState } from "react";
import Message from "./Message.tsx";
import { chatRequest } from "../api/client";

export default function ChatWindow() {

    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const boxRef = useRef(null);

    const send = async () => {

        if (!input.trim()) return;

        const userText = input;   // ⭐ 先缓存

        // ⭐ 1. 立刻清空输入框（你要的功能）
        setInput("");

        // 用户消息（右边）
        setMessages(prev => [...prev, {
            role: "user",
            content: userText
        }]);

        const res = await chatRequest({
            query: userText,
            conversation_id: "1"
        });

        // 模型消息（左边）
        setMessages(prev => [...prev, {
            role: "assistant",
            content: res.answer,
            mode: res.mode,
            sources: res.sources
        }]);
    };

    // 自动滚动到底部
    useEffect(() => {
        boxRef.current?.scrollTo(0, boxRef.current.scrollHeight);
    }, [messages]);

    return (
        <div className="main">

            <div className="chat-box" ref={boxRef}>
                {messages.map((m, i) => (
                    <Message key={i} msg={m} />
                ))}
            </div>

            <div className="input-box">
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && send()}
                    placeholder="Message..."
                />

                <button onClick={send}>
                    Send
                </button>
            </div>

        </div>
    );
}