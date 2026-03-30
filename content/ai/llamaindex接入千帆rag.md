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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBBYR5E%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T040942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCuqetNeUmyIDCJrENhvwwcPtKflahnKxD0uMLQ738lVwIhAKVcPvJhUiWpkkjHBD3B0wh9E3OVo%2FtUoWIsq8RQEpGsKv8DCBwQABoMNjM3NDIzMTgzODA1Igx0GWjS5ZkPZDEVeCkq3AO7tjCFdaCkoCmUxsuDT3HFmvRcVbUXG2UaSXjDYpPbt%2BzigqDMZGqb0i6DX7zGn4ZWN4TV5A9hjXbq6R0QkNmz7%2F6JiDgAdXppmKTsGjsRQHcBTrBiIOKMX3C0sSi0LoN9nLLwWgMkk%2BsnYvsmje26BEjz7BiY1Do7%2Bkl7Z9KgwNxk8V7qfC%2F9D7p6YI5OaTpRFwTs2Hq7uB3i6qQnfGiraB6UKQpeYRKHOIMePGYWBsPiwQOBY1vlWnTflSPN2%2F9z%2FGsfGbdjY8ThTfoY29O3vInosfDTIe9y860xddQFe8DNwqzKyVGaP7YBUfVlLB6ZRU%2FFEHiZ1E6IdgVxv6a%2BnNCST0aB80euy8wolRc%2BSGa8X9%2Bxg7CmhG6OrvUzGZ1GcPWpD%2Fni%2Fl64n%2FTk3OfJJOMDMIzxAZAsAfXwzXQlLPiZ%2BB8nMtYp8LINtTzRLT9uQVb8LrZCuUrTAJe4piehmiEepGB1c3wz2R43rTYlCvuizJ2nqCUKImpBePuKa0bhnJT52FdcP8t0lBv%2FnAqTZFexpIpr8QPyJdmfpjsswiAHBnvfZf%2BPaUfIJ1F9wtXyggOJtOAecbgp5xNPGm9Nw2sQVx2OvcWdodhjIYKr8F%2BxRbXefi8UgoVZFTCDyafOBjqkASoySK%2B3b8cAbcjE8Qaz6b1Pc%2BpotrA5MdSRYAACeaz3YJhn9CdLB%2B1pndn5Q%2FqygZLBAk%2BiDM%2FT60ktOryHSK4%2BMWkrDJPNoam7agIL%2BmdDNHO0d37xnKiDkVKW%2F28E8O2TxqqBYOUU7mxzKpoUlISYkmDG3rKFxsIkc2LJ5nqxAhe6C%2FZYevOoI7W4JKUwB1oDKm1FIv4xR%2FbwXKOJmjnEKH1u&X-Amz-Signature=48fe2b1538e6e1c38d883828b77855ff34405a057b591d5fa0fff11c9b5679a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBBYR5E%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T040942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCuqetNeUmyIDCJrENhvwwcPtKflahnKxD0uMLQ738lVwIhAKVcPvJhUiWpkkjHBD3B0wh9E3OVo%2FtUoWIsq8RQEpGsKv8DCBwQABoMNjM3NDIzMTgzODA1Igx0GWjS5ZkPZDEVeCkq3AO7tjCFdaCkoCmUxsuDT3HFmvRcVbUXG2UaSXjDYpPbt%2BzigqDMZGqb0i6DX7zGn4ZWN4TV5A9hjXbq6R0QkNmz7%2F6JiDgAdXppmKTsGjsRQHcBTrBiIOKMX3C0sSi0LoN9nLLwWgMkk%2BsnYvsmje26BEjz7BiY1Do7%2Bkl7Z9KgwNxk8V7qfC%2F9D7p6YI5OaTpRFwTs2Hq7uB3i6qQnfGiraB6UKQpeYRKHOIMePGYWBsPiwQOBY1vlWnTflSPN2%2F9z%2FGsfGbdjY8ThTfoY29O3vInosfDTIe9y860xddQFe8DNwqzKyVGaP7YBUfVlLB6ZRU%2FFEHiZ1E6IdgVxv6a%2BnNCST0aB80euy8wolRc%2BSGa8X9%2Bxg7CmhG6OrvUzGZ1GcPWpD%2Fni%2Fl64n%2FTk3OfJJOMDMIzxAZAsAfXwzXQlLPiZ%2BB8nMtYp8LINtTzRLT9uQVb8LrZCuUrTAJe4piehmiEepGB1c3wz2R43rTYlCvuizJ2nqCUKImpBePuKa0bhnJT52FdcP8t0lBv%2FnAqTZFexpIpr8QPyJdmfpjsswiAHBnvfZf%2BPaUfIJ1F9wtXyggOJtOAecbgp5xNPGm9Nw2sQVx2OvcWdodhjIYKr8F%2BxRbXefi8UgoVZFTCDyafOBjqkASoySK%2B3b8cAbcjE8Qaz6b1Pc%2BpotrA5MdSRYAACeaz3YJhn9CdLB%2B1pndn5Q%2FqygZLBAk%2BiDM%2FT60ktOryHSK4%2BMWkrDJPNoam7agIL%2BmdDNHO0d37xnKiDkVKW%2F28E8O2TxqqBYOUU7mxzKpoUlISYkmDG3rKFxsIkc2LJ5nqxAhe6C%2FZYevOoI7W4JKUwB1oDKm1FIv4xR%2FbwXKOJmjnEKH1u&X-Amz-Signature=4f6ab8e75f9ab8fcb3feda9513d169256084925ae61eadcb700875a1f69e0ff1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

