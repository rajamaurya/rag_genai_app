# 🤖 RAG GenAI App

> A full-stack, open-source GenAI app for document-based chat using Hugging Face models and FAISS vector store. Built with **FastAPI**, **LangChain**, **FAISS**, and **React + Vite**.

---

## 🚀 Overview

**RAG GenAI** is a Retrieval-Augmented Generation (RAG) application that enables conversational Q&A over user-uploaded documents. It uses **open-source Hugging Face embeddings** and **FAISS** to store and retrieve document chunks, and supports real-time streamed chat replies.

---

## 🔧 Tech Stack

- **Frontend**: React, Vite, TailwindCSS
- **Backend**: FastAPI, LangChain, Python
- **Embeddings**: Hugging Face (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS
- **Other Tools**: PyPDF, Multipart Uploads

---

## ✨ Features

- 📄 Upload **multiple PDFs** and chat with them.
- ⚙️ Uses **LangChain** for document chunking and retrieval.
- 🧠 **Hugging Face** model embeddings (Free & local).
- 🔍 Fast document similarity search with **FAISS**.
- 🧵 Maintains **chat history** context.
- ⏱️ **Streaming** chat response for smoother UX.
- 📚 **Source citation** with each answer.
- 🐳 Optional **Docker** support for deployment.

---

## 📁 Folder Structure

