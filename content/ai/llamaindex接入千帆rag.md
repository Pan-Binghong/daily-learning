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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466652SIVCU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwcjY%2FKCSw7C9n2p4toTgkeoG5mWqfZHmL6a4LC0LK%2BAiAT0bcgfVWWx5lG0IAb0YiJ0vDwNWRKwK%2BiIsw3aIg84Sr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMOMATIpqwqxgdFizAKtwD1bzWFeRmnEnG1iQwb0HB%2FVsBoJkQnk4K2DIcO%2F5ozIIRdZezw89Ti0c%2B%2FhNxxpQ26CcFSRiRC0EZ%2BJ0CIGtv2rWsSjxVjRAncrUnBsUv0GVzZ832jbIcCYyqbsiZpFt9nKGYr6RoP9n5e1HqJb58qfryX9g1CuqpzG8kCMfE1WBtGKt%2FnnJpf2cjeQTAThk08mYQnwsVk91rvmMt9SPVJFc%2FeNewpcOoHUwczb4xWp7SvNaGw4npDmxBNpYUYEkouyun3puyQd7o0w1ZLVirYjt8OSB7i1R5yH9SXmPw3kIwHOdLfurJj%2FqxKf%2Ft3fmhZG4HVIaSpeSdhVnO2aQcQGKQUPUmf66hPoZtpKUV6NVYoVXVJ9rEshaL9t%2Bui9css0D68cZP0viC3xFYcGEJI5qsdNnywdd6x3lgWKgXU1yFqgnXEKDCYMerjVH63IvFp7ZGrEUoo8V9EA1h7YaZ7XZNFsyShvZku8vaBdwFobQLq0XU9X0gX2%2BQ6adsvdaumsvEMhD6mH8024%2BhuhE6%2BD6rSOJxT73Tj6E5qBeAx1CCo0P41KWHg%2BcsREJkbyxICq0BmHxMFqSled6AKN75cy1%2B3cot%2FO12AY6hco4tWKmE6VZ2Ka4ieZTsWfcw%2FeOCzgY6pgELon4xEDF2AAZVEUcRqZ7BKGryI3Fjc0KVdqcFqfWTp8EwicltZ%2Bv35lXf3Q3Jp8K%2FK5up1hKNMOsRbjiTEiRAZcBZ52GVW9HpLkhLUCuinN%2BDYMcrJhzTyCumS5i99CirCRXukuLI1JV989Wn7N9aKAypp1M%2BK7UJmmVOu8ZvnBisWpc6LvsC39e5Ld6ubWYECTtZSXmpeLFleWjVw%2FFxOQKe3g3p&X-Amz-Signature=63b136048584450556faa81bb0e87d44205be5395ef4d73ae2881106d79436f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466652SIVCU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwcjY%2FKCSw7C9n2p4toTgkeoG5mWqfZHmL6a4LC0LK%2BAiAT0bcgfVWWx5lG0IAb0YiJ0vDwNWRKwK%2BiIsw3aIg84Sr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMOMATIpqwqxgdFizAKtwD1bzWFeRmnEnG1iQwb0HB%2FVsBoJkQnk4K2DIcO%2F5ozIIRdZezw89Ti0c%2B%2FhNxxpQ26CcFSRiRC0EZ%2BJ0CIGtv2rWsSjxVjRAncrUnBsUv0GVzZ832jbIcCYyqbsiZpFt9nKGYr6RoP9n5e1HqJb58qfryX9g1CuqpzG8kCMfE1WBtGKt%2FnnJpf2cjeQTAThk08mYQnwsVk91rvmMt9SPVJFc%2FeNewpcOoHUwczb4xWp7SvNaGw4npDmxBNpYUYEkouyun3puyQd7o0w1ZLVirYjt8OSB7i1R5yH9SXmPw3kIwHOdLfurJj%2FqxKf%2Ft3fmhZG4HVIaSpeSdhVnO2aQcQGKQUPUmf66hPoZtpKUV6NVYoVXVJ9rEshaL9t%2Bui9css0D68cZP0viC3xFYcGEJI5qsdNnywdd6x3lgWKgXU1yFqgnXEKDCYMerjVH63IvFp7ZGrEUoo8V9EA1h7YaZ7XZNFsyShvZku8vaBdwFobQLq0XU9X0gX2%2BQ6adsvdaumsvEMhD6mH8024%2BhuhE6%2BD6rSOJxT73Tj6E5qBeAx1CCo0P41KWHg%2BcsREJkbyxICq0BmHxMFqSled6AKN75cy1%2B3cot%2FO12AY6hco4tWKmE6VZ2Ka4ieZTsWfcw%2FeOCzgY6pgELon4xEDF2AAZVEUcRqZ7BKGryI3Fjc0KVdqcFqfWTp8EwicltZ%2Bv35lXf3Q3Jp8K%2FK5up1hKNMOsRbjiTEiRAZcBZ52GVW9HpLkhLUCuinN%2BDYMcrJhzTyCumS5i99CirCRXukuLI1JV989Wn7N9aKAypp1M%2BK7UJmmVOu8ZvnBisWpc6LvsC39e5Ld6ubWYECTtZSXmpeLFleWjVw%2FFxOQKe3g3p&X-Amz-Signature=1700fa753e0830e8848a692ba007f129dcfd19573cabc96a3c9a79cd1e7baa6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

