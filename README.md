# 📖 Interactive AI Story Generator

An interactive story generation application powered by AI that creates dynamic, choice-driven narratives. Users guide the story's progression by making decisions at key plot points, creating a unique storytelling experience every time.

## ✨ Features

- 🎭 **Dynamic Story Generation**: AI-powered creative storytelling using Groq's LLM models
- 🔀 **Interactive Choices**: Make decisions that shape the narrative direction
- 💾 **Session Persistence**: Story progress is maintained throughout your session
- 🎨 **Modern UI**: Clean, responsive interface built with Streamlit
- 🔄 **Story Continuity**: Seamless story progression based on user choices
- 📝 **Multiple Endings**: Different paths lead to unique story conclusions
- 🚀 **Fast Generation**: Powered by Groq's high-performance inference

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangGraph (LangChain)
- **AI Model**: Groq API (Llama 3.1 8B)
- **State Management**: LangGraph MemorySaver
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://console.groq.com))

## 🚀 Installation

1. **Clone the repository**
```bash
   git clone https://github.com/SayanPal12/Story-Generator.git
   cd story-generator
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   streamlit run frontend.py
```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Enter your Groq API key in the sidebar
   - Start creating stories!

## 📦 Dependencies
```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-groq>=0.0.1
langgraph>=0.0.40
groq>=0.4.0
```

## 🎮 Usage

1. **Enter your Groq API Key** in the sidebar
2. **Input a story topic** (e.g., "space adventure", "mystery mansion")
3. **Read the generated story** segment
4. **Choose from multiple options** to guide the narrative
5. **Continue making choices** until you reach an ending
6. **Start a new story** anytime with the reset button

## 🏗️ Project Structure
```
story-generator/
│
├── frontend.py           # Streamlit UI and user interactions
├── backend.py            # LangGraph agent and story generation logic
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🔑 Configuration

The application requires a Groq API key for operation. You can:
- Enter it directly in the sidebar (recommended for local development)
- Set it as an environment variable: `GROQ_API_KEY=your_key_here`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast LLM inference
- [LangChain](https://langchain.com/) for the agent framework
- [Streamlit](https://streamlit.io/) for the intuitive UI framework

## 🗺️ Roadmap

- [ ] Add story export functionality (PDF/TXT)
- [ ] Implement story history and bookmarks
- [ ] Add multiple genre templates
- [ ] Support for image generation in stories
- [ ] Multi-language support
- [ ] User authentication and cloud storage

---

⭐ If you find this project useful, please consider giving it a star!
