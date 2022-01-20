import SyntaxHighlighter from 'react-syntax-highlighter';
import {atomOneDark} from 'react-syntax-highlighter/dist/esm/styles/hljs';
import toast from "react-hot-toast";

export const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text).then(r => console.log(r));
    toast.success('Copied to clipboard!', {
        id: 'clipboard',
    });
}

const Code = (text) => {
    text = text.text;

    return (
        <div className="relative code-snippet px-9 rounded-md
                justify-self-start sm:justify-self-center mb-5 mt-2">
            <button className="copy-btn" onClick={() => copyToClipboard(text)}>
                <div className="btn h-auto min-h-0 border-gray-600 border p-1 rounded-md transition ease-in-out duration-100
                        hover:scale-105 hover:border-slate-300 text-gray-500 hover:text-slate-300">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none"
                         viewBox="0 0 24 24"
                         stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                              d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                    </svg>
                </div>
            </button>
            <SyntaxHighlighter language="python" style={atomOneDark} className="code-pre">
                {text}
            </SyntaxHighlighter>
        </div>
    )
};

export default Code;