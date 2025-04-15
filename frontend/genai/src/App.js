import { useState } from 'react';
import './App.css';
import axios from 'axios'
function App() {

  const [files, setFiles] = useState([])
  const [loading, setLoading] = useState(false)
  const [query, setQuery] = useState("")
  const [answer, setAnswer] = useState('')

  const handleChange = (e) => {
    const files = Array.from(e.target.files);
    setFiles(files);
  }
  const uploadFiles = async () => {
    setLoading(true);
    const data = new FormData();
    for (let file of files) {
      data.append("files", file)
    }
    console.log("files data:: ", data)
    await axios.post("http://localhost:8000/upload", data);
    setLoading(false)
  }
  const ask = async () => {
   setLoading(true)
    const res = await axios.post("http://localhost:8000/ask", { "question": query}, {
      headers: {
        "Content-Type": "application/json",
      },
      timeout: 1000000
    });
    console.log("RES::: ", res)
    const readerStream = res.body.reader();
    const decoder = new TextDecoder();
    let result = '';
    while (true) {
      const { done, value } = await readerStream.read()
      if (done) break;
      const chunks = decoder.decode(value)
      result += chunks
    }
    setAnswer((prev) => prev + result);
   setLoading(false);
  }
  return (
    <div className="App">
      <header>Chat-GPT</header>
      <input type="file" multiple onChange={handleChange} />
      <button onClick={uploadFiles}>Upload</button>
      {loading? 'Loading...': ''}
      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question..."
      />
      <button onClick={ask}>Ask</button>
      <pre>{answer}</pre>
    </div>
  );
}

export default App;
