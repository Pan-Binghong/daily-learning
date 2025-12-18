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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2D4FY2K%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAwfVXVfPruYtHDOsorohl6SxwAQZmmEGbehOGVEeKb9AiAZ1MEdakH0SJG%2FLEFJGKP%2BWpB2MKGt3mHNKbOZfM2DmCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKSClan215uoJF7WAKtwDzA6t7EltrL17uOe6vVT2j1Wup9q3zHpw8Co98duOrtaq3M4qzB%2BpJaUTJGm3PHQFy2gufziUYDgMEEpV7s%2F0nrJ0IV%2FlGKggpGQV7Vc1XQZ6nXgENgxw%2Bos14DXwprW6fK4Zgdlkr3WnmyaEDMkowIgGPQou5z%2FXyOXf5VgtmUV5Edpu59jaYx%2FwFE1JjeQGPQVVcQcD96fhiNDtiNVHljtIGtg%2FJwYy86Ti9ufbeP3ArmpQB4MD80p%2BgdsJ%2FEKHMDHVN3iXpOzlZQnlS1E2znbpiTZizmWi2lQYLll6AyO6f2p6VZV9%2FOIoiQtXHPswmMFzpSJqa82YM6CgNuIE9t9FRj5Yv9DKHLQPxJLGJAIoqmTxioshNaWEVRJF02QsJJfqO7WE0KvU349E%2FyHEqEIjl289X19fBKUcW4HOkmmzMOYzvP3PWG9BHb5pestRhFe66ZfARRPrHuF7iYNiYr%2BB9xxMtdnrol%2FfVdneAuh%2BL%2F%2F9WSdD86fmUH3BnV8JD2b07yRQodL7gGSS9pnc%2BRV%2F%2Bpit7gbUtgnXZGHXeT1lFj1mNmnBxklmyBFUw0yZiSNs0DCTCp3X2OP%2FynhjpBOw3JXh8W7m0QE6nHtMRomsrlHC%2F7YThsIBNsowicqNygY6pgG9wWZr%2F1CTw3aKOzCD3GGA3pMZiH6QukJKepymBhQod9%2FrOBBwfKPyx4XIj2UDuDYNVZPzHvmGQrNIciXso%2F3OKh9TMRMjZCIKDm9A6xbA0tXoG%2B5Q2oksC4GXqCk8d9Zn2G3g7JK1FIreGCkfXuYWh9NZyQWCqzDC8PzCx4eYt166c0BRoPhCsHNselv9MSg6Wja5%2FNlraLkQtjhkeO9StwYo4Ps7&X-Amz-Signature=5b7d212c323d167cdc60b375e67388967d6a5b62b6e8fffc920257604988e05c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2D4FY2K%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAwfVXVfPruYtHDOsorohl6SxwAQZmmEGbehOGVEeKb9AiAZ1MEdakH0SJG%2FLEFJGKP%2BWpB2MKGt3mHNKbOZfM2DmCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKSClan215uoJF7WAKtwDzA6t7EltrL17uOe6vVT2j1Wup9q3zHpw8Co98duOrtaq3M4qzB%2BpJaUTJGm3PHQFy2gufziUYDgMEEpV7s%2F0nrJ0IV%2FlGKggpGQV7Vc1XQZ6nXgENgxw%2Bos14DXwprW6fK4Zgdlkr3WnmyaEDMkowIgGPQou5z%2FXyOXf5VgtmUV5Edpu59jaYx%2FwFE1JjeQGPQVVcQcD96fhiNDtiNVHljtIGtg%2FJwYy86Ti9ufbeP3ArmpQB4MD80p%2BgdsJ%2FEKHMDHVN3iXpOzlZQnlS1E2znbpiTZizmWi2lQYLll6AyO6f2p6VZV9%2FOIoiQtXHPswmMFzpSJqa82YM6CgNuIE9t9FRj5Yv9DKHLQPxJLGJAIoqmTxioshNaWEVRJF02QsJJfqO7WE0KvU349E%2FyHEqEIjl289X19fBKUcW4HOkmmzMOYzvP3PWG9BHb5pestRhFe66ZfARRPrHuF7iYNiYr%2BB9xxMtdnrol%2FfVdneAuh%2BL%2F%2F9WSdD86fmUH3BnV8JD2b07yRQodL7gGSS9pnc%2BRV%2F%2Bpit7gbUtgnXZGHXeT1lFj1mNmnBxklmyBFUw0yZiSNs0DCTCp3X2OP%2FynhjpBOw3JXh8W7m0QE6nHtMRomsrlHC%2F7YThsIBNsowicqNygY6pgG9wWZr%2F1CTw3aKOzCD3GGA3pMZiH6QukJKepymBhQod9%2FrOBBwfKPyx4XIj2UDuDYNVZPzHvmGQrNIciXso%2F3OKh9TMRMjZCIKDm9A6xbA0tXoG%2B5Q2oksC4GXqCk8d9Zn2G3g7JK1FIreGCkfXuYWh9NZyQWCqzDC8PzCx4eYt166c0BRoPhCsHNselv9MSg6Wja5%2FNlraLkQtjhkeO9StwYo4Ps7&X-Amz-Signature=c8bafe71bb21e47b187e2459382f7637f039ef72e94f05ccdb229760b098f5d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

