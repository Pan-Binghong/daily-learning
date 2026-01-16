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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBRJO3UN%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGBYCy50oGXsgEk%2F7oGBCv9I0lR%2BeBw%2BLwGUSj1szO9gAiEAjSYijrl6y8236JBxPAaDGiK784HmQmBkfyOmrwXEDSoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNMFjxHXUWcowEsE5SrcA5IFJ79rYYwAg5pPXHifoEfXJrfQ4PKQfW5FZ2yLSzGT3432QyWK90kKbSFaKIV3Nq%2BMb1PST0m7LucPBFP0AIpArhU0jogQaQd8ue863AZmTGVLV6vFlOY6mQIwKolQh4ZDd3fK0%2F6wBvt07K%2BklhDOLAwcnDWmgWm0mwNYEpCU%2FOtdmFAHVvsjKxJZ%2BVy98WgPLyfUAo7NyiI7qxB%2B4OuOIqM9D4cZh8Q53yFyplgPjwtd2hiFRvjTrY3NMIVRixo2UNfLbimv4UvuoKuFTpUVZLaC5pTw9kmXObB3VmBrwVx4YQwHBRPrC52Xr%2FKYFOSfDhfobA78UnTZw7dhzUdv4vwNaVZvM95X7Zu0E1cIvHAyqtHY1%2Fs8koc9UZwhcdPOUMN7LyXKCGZVr5VxXjxSO3aFuiFwomD0krtj71RP3nxDp95uLny2UvOh5uu25aRaWLsCewNumNW5FXrjXC4cQ6w0dgVLqDVtDaYPJMb%2BIw0ix2n%2BvcMxwuYU6VbVmimi0NabJxs032kMAZH9zNbZ1Sj96iWU%2Ff1JV8%2FZsndxm5DgfdTSfLBSx0BK9YbWD468RuLBanoukFBfMMGvjM1k60mECR9U9jKDqGo6ItMvccMssXW1GEgl4Ws4MM6%2FpssGOqUBX950CdHIndDfALUMlZaCwat%2B6y%2FW86NPdt8jGmXBNxXdrY5azfZqGZddJvEqwgveC%2B2QkIbl55llsTHBBd1ZS6f2iQwv4FI9dOkWQP3y1JWAfZOG%2FhMLcD49uOyAkI3K1th%2BGMBJ5D%2FaAvqgak9nOdmwY8JuFfmTyH%2FjRKWoz4NDeffbOKOidsa3xVTFoS6ImC0vzun81zCuorE9d5dRqICI%2Bhoo&X-Amz-Signature=1d9fd14d3f3f78d9ca9aba917ac092103051a622ab93dfd211941bf53edd532f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBRJO3UN%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGBYCy50oGXsgEk%2F7oGBCv9I0lR%2BeBw%2BLwGUSj1szO9gAiEAjSYijrl6y8236JBxPAaDGiK784HmQmBkfyOmrwXEDSoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNMFjxHXUWcowEsE5SrcA5IFJ79rYYwAg5pPXHifoEfXJrfQ4PKQfW5FZ2yLSzGT3432QyWK90kKbSFaKIV3Nq%2BMb1PST0m7LucPBFP0AIpArhU0jogQaQd8ue863AZmTGVLV6vFlOY6mQIwKolQh4ZDd3fK0%2F6wBvt07K%2BklhDOLAwcnDWmgWm0mwNYEpCU%2FOtdmFAHVvsjKxJZ%2BVy98WgPLyfUAo7NyiI7qxB%2B4OuOIqM9D4cZh8Q53yFyplgPjwtd2hiFRvjTrY3NMIVRixo2UNfLbimv4UvuoKuFTpUVZLaC5pTw9kmXObB3VmBrwVx4YQwHBRPrC52Xr%2FKYFOSfDhfobA78UnTZw7dhzUdv4vwNaVZvM95X7Zu0E1cIvHAyqtHY1%2Fs8koc9UZwhcdPOUMN7LyXKCGZVr5VxXjxSO3aFuiFwomD0krtj71RP3nxDp95uLny2UvOh5uu25aRaWLsCewNumNW5FXrjXC4cQ6w0dgVLqDVtDaYPJMb%2BIw0ix2n%2BvcMxwuYU6VbVmimi0NabJxs032kMAZH9zNbZ1Sj96iWU%2Ff1JV8%2FZsndxm5DgfdTSfLBSx0BK9YbWD468RuLBanoukFBfMMGvjM1k60mECR9U9jKDqGo6ItMvccMssXW1GEgl4Ws4MM6%2FpssGOqUBX950CdHIndDfALUMlZaCwat%2B6y%2FW86NPdt8jGmXBNxXdrY5azfZqGZddJvEqwgveC%2B2QkIbl55llsTHBBd1ZS6f2iQwv4FI9dOkWQP3y1JWAfZOG%2FhMLcD49uOyAkI3K1th%2BGMBJ5D%2FaAvqgak9nOdmwY8JuFfmTyH%2FjRKWoz4NDeffbOKOidsa3xVTFoS6ImC0vzun81zCuorE9d5dRqICI%2Bhoo&X-Amz-Signature=2a4ddd7a9c4fb02c507a4358f21ed4962a4d93c6d64ceca3ede21cc3432e695e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

