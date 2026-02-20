---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYTHNUN7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICF1XOPQUr6ufFpftitL%2Fp09Jw4p8h480iVmzYExWgt8AiBXtAhS83spaEy%2BboIVuVXgHX5aSTO5I3xiPgPIeUYkSyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdyDhPI4uRHkdNscnKtwDO%2FWMidmojcAlUSTLWBso%2FapOOiaKb%2BqTI0nJQEnUGX%2BcfvosYbHXqODZoeXqLyWWWDnG5AbYIZvt2tqzz2xe%2FfSoN7blROrl9xDuJcCY7ZHlsJzh6piigs29fnIaQP0WF289yErPtc64PCnHwgFgknYXQytaRoC8mphJFblUWzV8SRQK466cXCXStMotthiTtp3sA1HAdWqgzlWr%2FE0mzWEHqBahtcKHR9tQhV86LdRzkgr3F9rHg65fEW7Y6ztAMl7wIMX%2Bda6IrfQq9HgQW68cqopPVfG56paGxN6k9mWAzCwBA5LF6Ouq%2BQgVNERniaa46xP7MN5bqR1RCAXR8245iIguSyNq70K6Zk2N4JSn7QZkDhndp%2BFND8mWUz6JnZsgTzM5%2BLGG%2FrZdVco0yL84R0ijWjRf5z%2BCTEkU3BwQFsSoEBgX9jKxAzAhMPf7A6GBxFlodgXvQR1BK1IzNIPV6r1MzKf47B6qJj3bQIH3pgSasGL09PFt0fvzJmavNST5twpMM%2FM23ZOvEDXNWRP2zxx82h8DB7MaEnGoCDpCkceE2l00bPA12pq%2FKo4H5hInwKa7ofF4ns3gF2vNM%2FAqZPp9S9ludV5gEcJ8LRN4SKvAh9SssiQF2vAwwpDfzAY6pgHx24NBgMqmIvMLILeeUz8NjRZDrZke9lu7hND7OFbkYLvqnmQIXpP7DkZzzSMcUx6TYn6J0Sn4EqrHftb996nKdg8s%2B2pVE90zr%2B5tR9qIq48g%2FjysBZlh8yAGGQ8c2ffFEnQUI9FjzeY%2BQZKRUryYViVsgdozBEthE6dRaNJsUwK8sMpXI9OcR%2FREaAhYiS055pzZNjIdRhsASM1tPiqAO5E76Bjb&X-Amz-Signature=e2de6d497f286294ec73e06393c2eb3c1a7dfce2f43ed7dae4a9f81335fc8dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYTHNUN7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICF1XOPQUr6ufFpftitL%2Fp09Jw4p8h480iVmzYExWgt8AiBXtAhS83spaEy%2BboIVuVXgHX5aSTO5I3xiPgPIeUYkSyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdyDhPI4uRHkdNscnKtwDO%2FWMidmojcAlUSTLWBso%2FapOOiaKb%2BqTI0nJQEnUGX%2BcfvosYbHXqODZoeXqLyWWWDnG5AbYIZvt2tqzz2xe%2FfSoN7blROrl9xDuJcCY7ZHlsJzh6piigs29fnIaQP0WF289yErPtc64PCnHwgFgknYXQytaRoC8mphJFblUWzV8SRQK466cXCXStMotthiTtp3sA1HAdWqgzlWr%2FE0mzWEHqBahtcKHR9tQhV86LdRzkgr3F9rHg65fEW7Y6ztAMl7wIMX%2Bda6IrfQq9HgQW68cqopPVfG56paGxN6k9mWAzCwBA5LF6Ouq%2BQgVNERniaa46xP7MN5bqR1RCAXR8245iIguSyNq70K6Zk2N4JSn7QZkDhndp%2BFND8mWUz6JnZsgTzM5%2BLGG%2FrZdVco0yL84R0ijWjRf5z%2BCTEkU3BwQFsSoEBgX9jKxAzAhMPf7A6GBxFlodgXvQR1BK1IzNIPV6r1MzKf47B6qJj3bQIH3pgSasGL09PFt0fvzJmavNST5twpMM%2FM23ZOvEDXNWRP2zxx82h8DB7MaEnGoCDpCkceE2l00bPA12pq%2FKo4H5hInwKa7ofF4ns3gF2vNM%2FAqZPp9S9ludV5gEcJ8LRN4SKvAh9SssiQF2vAwwpDfzAY6pgHx24NBgMqmIvMLILeeUz8NjRZDrZke9lu7hND7OFbkYLvqnmQIXpP7DkZzzSMcUx6TYn6J0Sn4EqrHftb996nKdg8s%2B2pVE90zr%2B5tR9qIq48g%2FjysBZlh8yAGGQ8c2ffFEnQUI9FjzeY%2BQZKRUryYViVsgdozBEthE6dRaNJsUwK8sMpXI9OcR%2FREaAhYiS055pzZNjIdRhsASM1tPiqAO5E76Bjb&X-Amz-Signature=ffa2d3803c47bc371c5e0c5646eb6659ac410a98379b5de9ba8fb6ebb2af7646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

