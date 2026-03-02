"""
Automated Research Agent v1.0.0

A LangGraph-based autonomous research agent that uses DuckDuckGo search
to gather information and generate structured bilingual reports.

Author: [暇格]
License: MIT
"""

import os
from typing import Annotated, List, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from openai import APIConnectionError

# 1.载入环境变量

load_dotenv()
# 2.定义特工的“记忆”（状态）

class AgentState(TypedDict):
    # ddd_messages 会自动把新对话追加到列表中，保持上下文不断
    messages: Annotated[List[BaseMessage],add_messages]
# 3. 赐予特工武器 免费强大的DuckDuckgo搜索引擎 

search_tool = DuckDuckGoSearchRun()


@tool
def safe_ddg_search(query: str) -> str:
    """DuckDuckGo web search; returns error string instead of raising on failures."""
    try:
        return search_tool.run(query)
    except Exception as e:
        return f"DuckDuckGo search failed: {type(e).__name__}: {e}"


tools = [safe_ddg_search]

# 4.初始化大模型大脑 并绑定武器
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_base_url = os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE")
openai_model = os.getenv("OPENAI_MODEL") or "gpt-4o-mini"

if openai_base_url:
    openai_base_url = openai_base_url.rstrip("/")

llm_kwargs = {
    "model": openai_model,
    "temperature": 0.2,
    "api_key": openai_api_key,
    "timeout": 60,
    "max_retries": 2,
}
if openai_base_url:
    llm_kwargs["base_url"] = openai_base_url

llm = ChatOpenAI(**llm_kwargs)
llm_with_tools = llm.bind_tools(tools)

# 5.定义特工的思考节点
def agent_node(state: AgentState):
    """特工在这个节点查看所有历史信息，决定是去搜索，还是写出最终报告"""
    try:
        response = llm_with_tools.invoke(state["messages"])
    except APIConnectionError as e:
        raise RuntimeError(
            "Failed to connect to OpenAI. This is usually a network/proxy/firewall issue. "
            "If you're in a restricted network, set OPENAI_BASE_URL to your gateway (or enable VPN/proxy), "
            "then retry."
        ) from e
    return {"messages": [response]}


def should_continue(state: AgentState) -> str:
    latest_msg = state["messages"][-1]
    if hasattr(latest_msg, "tool_calls") and latest_msg.tool_calls:
        return "tools"
    return END
# 6. 开始编制 Agent 的工作流网络（LangGraph）    
workflow = StateGraph(AgentState)
# 添加节点
workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))
# 设置起点：一开始先让agent_node思考
workflow.set_entry_point("agent")
# 设置条件分支 特工思考完后 如果他决定调用搜索工具 就去tools节点 如果他不搜索了 就去end输出结果
workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
# 搜完之后 必须强制回到agent节点 让它看到搜索结果并再次思考
workflow.add_edge("tools","agent")
# 编译为可执行的系统
research_agent = workflow.compile()
# =================================================================
# 交互式 CLI (命令行界面)
# =================================================================
if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Missing environment variable OPENAI_API_KEY. Put it in your .env or system environment.")

    print("\n欢迎使用全自动智能调研特工 (powered by LangGraph)")
    print("请输入你的调研需求（输入 'q' / 'quit' / 'exit' 退出）。")

    # 设定特工的人设
    sys_msg = SystemMessage(
        content="你是一个顶尖的商业调研分析师。你的任务是使用 DuckDuckGo 搜索引擎进行网络冲浪，收集最新信息，并写出一份结构清晰、数据详实的 Markdown格式的中英文双语报告"
    )
    while True:
        user_input = input("\n👉 调研需求：")
        if user_input.lower() in ['q','quit','exit']:
            print("特工下线")
            break

        # 组装初始消息并开始运行图
        inputs = {"messages": [sys_msg, HumanMessage(content=user_input)]}
        print("\n⏳ 特工正在上网冲浪并分析数据，请稍后（可能需要 10-30 秒）...\n")

        # stream允许我们看到特工执行的每一个步骤
        last_chunk = None
        for chunk in research_agent.stream(inputs, stream_mode="values"):
            last_chunk = chunk
            latest_msg = chunk["messages"][-1]
            if hasattr(latest_msg, "tool_calls") and latest_msg.tool_calls:
                query = latest_msg.tool_calls[0].get("args", {}).get("query")
                if query:
                    print(f"🔍 [特工动作] 决定调用搜索引擎，关键词：{query}")

        # 拿到最终报告
        if not last_chunk:
            print("\n未获取到任何输出。")
            continue

        final_answer = last_chunk["messages"][-1].content
        print("\n"+"="*50)
        print("📑 最终调研报告:")
        print("="*50)
        print(final_answer)


