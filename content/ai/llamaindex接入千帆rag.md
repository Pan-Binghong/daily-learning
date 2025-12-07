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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BCOGIYI%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMPd3ef3HNbv57vTfO%2FhKGpBBef6Il%2FbmOON4eGvqUJwIhANa%2BqcXPe6ckkeDxZlj1r4x0wEX4Q%2Fr6PGOEnBuLrrziKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSOMqmoWNd8ZtaQcsq3APzLr85YGZbmXU6fmE5UW6fgMHwK4zEFhPstuyBW9RlIXiOkDd5O7FRrkoHnFFh4tlOUlRwsW5IA0esJd6zKzCZx8p477WYv8iRI1kfJirgSM2VHin6nTP6nh0%2FH0TzBqmthJAHbOZjGFiIHAuT%2B6v%2BzDcjy3tGpCY1PNtM9Y099sJq%2FCndQfFQzymFOlAwsCCIsPHreUyMSc84b64OL8bz0DyMKkHkMjLFO2QMyNwjyPNcE4Qaf5uTFBlB2Sputbk2k6D0QPKFrYckbajNOYY9psb0jjIqyM5TqYA5yD8aynjeKXLM9vHWC5OaDiesmsQXT5sfzZJJlNzmygQFc2vnHBPgxVDXwGV1yApBG5jHvDc4lLPNVbZcQLCsFXXpFhEJMqO9%2Bq2tAVyr3GoxVpQKYx4yI%2BbwlNANRxhtAXv5gwExgiwmKE2uiHLykR7IgOD9eQX4xgc1iQRXyV926UJdrMqin4m3nS2uVbfsPbQwvn6S5Auem4%2Fw2pAcTirr4B1qcBWvU9ADoiC5qL1yqZ97M0txS3vdfzC9a8NRg5kGY8urRDWV0Ky3RfxInw4CbzuuIu2HokEaDwJMhkCigs7jixadKD8kHcRgIW%2F4M5DgPV1BICQsB70ODBydGjCL%2FtLJBjqkAR%2FwQjkqzl9j4Q0VvSjmvsSClnLDPmCTtRODg19inxBeJqX%2FoeYIqzyPHuPAw5GCvRNRypp%2BiVN9sGBBdygEm8tbjne8lSHWlUQQddbmjkNJ8pklYYqBJzuDl3ak649nU5D0Agq%2Fg3IW4lQqycW%2FKhYWp8IPWqQkEYtHHu13BoB3OBWNraqANTwXBswq5X9sKaYWJEcZMZa%2BGrORFYaIllIJrZW4&X-Amz-Signature=c2ded0ef7c8b132bdf28bd4cb0c4842693f227de82a046c3cdf5dcb4b22ecb84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BCOGIYI%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMPd3ef3HNbv57vTfO%2FhKGpBBef6Il%2FbmOON4eGvqUJwIhANa%2BqcXPe6ckkeDxZlj1r4x0wEX4Q%2Fr6PGOEnBuLrrziKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSOMqmoWNd8ZtaQcsq3APzLr85YGZbmXU6fmE5UW6fgMHwK4zEFhPstuyBW9RlIXiOkDd5O7FRrkoHnFFh4tlOUlRwsW5IA0esJd6zKzCZx8p477WYv8iRI1kfJirgSM2VHin6nTP6nh0%2FH0TzBqmthJAHbOZjGFiIHAuT%2B6v%2BzDcjy3tGpCY1PNtM9Y099sJq%2FCndQfFQzymFOlAwsCCIsPHreUyMSc84b64OL8bz0DyMKkHkMjLFO2QMyNwjyPNcE4Qaf5uTFBlB2Sputbk2k6D0QPKFrYckbajNOYY9psb0jjIqyM5TqYA5yD8aynjeKXLM9vHWC5OaDiesmsQXT5sfzZJJlNzmygQFc2vnHBPgxVDXwGV1yApBG5jHvDc4lLPNVbZcQLCsFXXpFhEJMqO9%2Bq2tAVyr3GoxVpQKYx4yI%2BbwlNANRxhtAXv5gwExgiwmKE2uiHLykR7IgOD9eQX4xgc1iQRXyV926UJdrMqin4m3nS2uVbfsPbQwvn6S5Auem4%2Fw2pAcTirr4B1qcBWvU9ADoiC5qL1yqZ97M0txS3vdfzC9a8NRg5kGY8urRDWV0Ky3RfxInw4CbzuuIu2HokEaDwJMhkCigs7jixadKD8kHcRgIW%2F4M5DgPV1BICQsB70ODBydGjCL%2FtLJBjqkAR%2FwQjkqzl9j4Q0VvSjmvsSClnLDPmCTtRODg19inxBeJqX%2FoeYIqzyPHuPAw5GCvRNRypp%2BiVN9sGBBdygEm8tbjne8lSHWlUQQddbmjkNJ8pklYYqBJzuDl3ak649nU5D0Agq%2Fg3IW4lQqycW%2FKhYWp8IPWqQkEYtHHu13BoB3OBWNraqANTwXBswq5X9sKaYWJEcZMZa%2BGrORFYaIllIJrZW4&X-Amz-Signature=2b24f0f4658ff2ee69fe59afdfa363bcfea99707ad7614acb9850f7aafdc4df8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

