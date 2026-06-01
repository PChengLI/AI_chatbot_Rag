import ChatWindow from "./components/ChatWindow";
import UploadPanel from "./components/UploadPanel";
import "./styles.css";

export default function App() {
    return (
        <div className="layout">

            {/* 左侧上传 */}
            <div className="sidebar">
                <UploadPanel />
            </div>

            {/* 右侧聊天 */}
            <ChatWindow />

        </div>
    );
}