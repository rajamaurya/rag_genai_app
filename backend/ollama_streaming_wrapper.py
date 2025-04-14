from typing import Optional, Iterator, List
from langchain_core.language_models.llms import LLM
import requests
import json

class OllamaStreamingLLM(LLM):
    model: str = "mistral"
    temperature: float = 0.7

    def _llm_type(self) -> str:
        return "ollama"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "temperature": self.temperature
            }
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()

    def stream(self, prompt: str) -> Iterator[str]:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": True,
                "temperature": self.temperature
            },
            stream=True
        )
        for line in response.iter_lines():
            if line:
                # Remove "data: " prefix and parse JSON
                if line.startswith(b"data:"):
                    data = json.loads(line[6:].decode("utf-8"))
                    token = data.get("response", "")
                    yield token
