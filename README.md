# Automated Research Agent

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.38-orange.svg)

一个基于 LangGraph + LangChain 构建的全自动智能调研特工，能够自主使用 DuckDuckGo 搜索引擎进行网络调研，并生成结构化的中英文双语报告。

An autonomous AI research agent built with LangGraph + LangChain that automatically searches the web using DuckDuckGo and generates structured bilingual reports.

## ✨ Features

- 🤖 **自主决策** - Agent 自动决定何时搜索、搜索什么关键词
- 🔍 **智能搜索** - 集成 DuckDuckGo 搜索引擎，无需 API key
- 📊 **结构化输出** - 生成 Markdown 格式的专业调研报告
- 🌐 **双语支持** - 中英文双语报告输出
- 🔄 **流式执行** - 实时显示 Agent 的思考和执行过程
- 🛡️ **错误处理** - 完善的异常处理和网络代理支持

## 🎯 Use Cases

- 市场调研与竞品分析
- 技术选型与方案调研
- 行业趋势分析
- 学术资料收集
- 产品需求研究

## Requirements

- Python 3.10+ (recommended)
- OpenAI API key or compatible API endpoint

## 🚀 Quick Start

1) Create a virtual environment

```powershell
py -3.10 -m venv .venv310
```

2) Install dependencies

```powershell
.\.venv310\Scripts\python -m pip install -U pip
.\.venv310\Scripts\python -m pip install -r requirements.txt
```

3) Configure environment variables

- Copy `.env.example` to `.env`
- Fill in `OPENAI_API_KEY`
- (If you use an OpenAI-compatible gateway) set `OPENAI_BASE_URL`
- Select a model via `OPENAI_MODEL`

## 🚀 Quick Start

1) **Create a virtual environment**

```powershell
py -3.10 -m venv .venv310
```

2) **Install dependencies**

```powershell
.\.venv310\Scripts\python -m pip install -U pip
.\.venv310\Scripts\python -m pip install -r requirements.txt
```

3) **Configure environment variables**

- Copy `.env.example` to `.env`
- Fill in your `OPENAI_API_KEY`
- (Optional) Set `OPENAI_BASE_URL` for OpenAI-compatible endpoints
- (Optional) Select a model via `OPENAI_MODEL` (default: gpt-4o-mini)

4) **Run the agent**

```powershell
.\.venv310\Scripts\python agent.py
```

## 📖 Usage Example

```
欢迎使用全自动智能调研特工 (powered by LangGraph)
请输入你的调研需求（输入 'q' / 'quit' / 'exit' 退出）。

👉 调研需求：分析2026年AI Agent的发展趋势

⏳ 特工正在上网冲浪并分析数据，请稍后（可能需要 10-30 秒）...

🔍 [特工动作] 决定调用搜索引擎，关键词：AI Agent 2026 trends

==================================================
📑 最终调研报告:
==================================================
# 2026年AI Agent发展趋势分析

## 概述
...
```

## 🛠️ Tech Stack

- **LangGraph** - Agent workflow orchestration
- **LangChain** - LLM framework and tool integration
- **OpenAI API** - Language model (supports compatible endpoints)
- **DuckDuckGo Search** - Free web search without API key

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | ✅ Yes | - | Your OpenAI API key |
| `OPENAI_MODEL` | ❌ No | `gpt-4o-mini` | Model to use |
| `OPENAI_BASE_URL` | ❌ No | - | Custom API endpoint |
| `HTTP_PROXY` | ❌ No | - | HTTP proxy for DuckDuckGo |
| `HTTPS_PROXY` | ❌ No | - | HTTPS proxy for DuckDuckGo |

### Supported Models

- OpenAI: `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`
- Compatible endpoints: Any OpenAI-compatible API

## 🔧 Troubleshooting

### DuckDuckGo Timeout

If DuckDuckGo search times out on your network:

1. Set proxy in `.env`:
```env
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

2. Or use a VPN

### API Connection Error

If you see `Failed to connect to OpenAI`:

- Check your `OPENAI_API_KEY` is correct
- Verify `OPENAI_BASE_URL` if using custom endpoint
- Check network/firewall settings

## 📁 Project Structure

```
.
├── agent.py              # Main agent implementation
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── LICENSE              # MIT License
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain)
- Search powered by [DuckDuckGo](https://duckduckgo.com/)

## 📧 Contact

For questions or collaboration opportunities, feel free to reach out!

---

**Note:** This is a demonstration project showcasing AI agent development capabilities with LangGraph. Suitable for portfolio and learning purposes.
