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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFDSIF43%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD1VzyO1No%2Bapl6p9ug70xQEnnsIhfi01exf%2BKWSNwxvgIhAODzIhBWEaKMrvz5hNB5%2FQnFyljkCSCFwCyCsmR%2FziDoKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfGjZ4dU1bau7YlEYq3ANW3ltzrmFVPUUcgWOPHS7TMfbKKCoV0d0hRWTIVSZvz3QYnY1XDxfYSm0Tuxdqs3UeLsZRYGRAuUqniU7qoO5wmMQk3x9Ip%2BVsfDsNK3ol%2FM9R7GKbs%2B0XDbNe%2BbgbQBfzYnKJsxDpkfQtLfPqb1BuMVvbq%2BKE6RWNtGXcUU%2BBbRvlKosuy5z7cmwS7LdPqgAr7ABWCpl06exx98k2ZZ%2FwlG%2B%2Bzaziowg%2BZ0JJ9zuS2qPhOjL1vQPDeDYXSyaZ6lFIZ3WxDyUMHe94UJOWu2Sx%2F7BQaGQl%2BSjoyE%2BVAko7Kta8%2BfZ9Vke7lIhg1RPMLphgZLoJJCKMmUwFgyCZxYRXQpeoE5EMkeWNxwh2ldodca%2B3frOrT1vV8KVskufAasrKyPT9PIcYTqFZpr%2BS3pzy5RU4HO4TwCVWj9%2BdAyGmjH%2B5CK%2BQ%2F2efZmS2DlVEIB%2BpCUZI8D7nQYWEgo%2BLsKWocc5kDN21PAGKG7ttJglaBQ4kyL%2BKrHOnRBttXO52XSm%2F5Rk5aEXjALRZlef%2B%2FEN%2BK0TWJu3ZmF5yabtG9X8DwenurDEc9w1t4HFiSCTA3J%2Fp5KVYbcvXaMdK95kHd8lTAk8m7I5HnaUmQxfsc0GdcBWm%2BRSs0TctaTEniTD9t7%2FIBjqkAb9JyRWLrd8ApwgjnTUegssfufF8kCXhtWOwl%2FJ8Dd0%2B1b3zNr%2FXZzqOc%2B%2FoqTiIJQqqWO%2B7HSFDwyy73QQfgUqL3GXu%2BW3zpnJMIcAdjA3svoy0fH8DsB6iZFLjAml3x6oM4zyUoPetncqcH65cQpM6%2BylXCIVgAS819%2Fmku0l4L5l7zAEJYPkQJog4ee%2By8pWDYB7CXyu9nqwjSDlvq5Vo20ek&X-Amz-Signature=b0deb482a0f6096c26dd7cbb180703682240faef97d42ed99e88629d883ec551&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFDSIF43%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD1VzyO1No%2Bapl6p9ug70xQEnnsIhfi01exf%2BKWSNwxvgIhAODzIhBWEaKMrvz5hNB5%2FQnFyljkCSCFwCyCsmR%2FziDoKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfGjZ4dU1bau7YlEYq3ANW3ltzrmFVPUUcgWOPHS7TMfbKKCoV0d0hRWTIVSZvz3QYnY1XDxfYSm0Tuxdqs3UeLsZRYGRAuUqniU7qoO5wmMQk3x9Ip%2BVsfDsNK3ol%2FM9R7GKbs%2B0XDbNe%2BbgbQBfzYnKJsxDpkfQtLfPqb1BuMVvbq%2BKE6RWNtGXcUU%2BBbRvlKosuy5z7cmwS7LdPqgAr7ABWCpl06exx98k2ZZ%2FwlG%2B%2Bzaziowg%2BZ0JJ9zuS2qPhOjL1vQPDeDYXSyaZ6lFIZ3WxDyUMHe94UJOWu2Sx%2F7BQaGQl%2BSjoyE%2BVAko7Kta8%2BfZ9Vke7lIhg1RPMLphgZLoJJCKMmUwFgyCZxYRXQpeoE5EMkeWNxwh2ldodca%2B3frOrT1vV8KVskufAasrKyPT9PIcYTqFZpr%2BS3pzy5RU4HO4TwCVWj9%2BdAyGmjH%2B5CK%2BQ%2F2efZmS2DlVEIB%2BpCUZI8D7nQYWEgo%2BLsKWocc5kDN21PAGKG7ttJglaBQ4kyL%2BKrHOnRBttXO52XSm%2F5Rk5aEXjALRZlef%2B%2FEN%2BK0TWJu3ZmF5yabtG9X8DwenurDEc9w1t4HFiSCTA3J%2Fp5KVYbcvXaMdK95kHd8lTAk8m7I5HnaUmQxfsc0GdcBWm%2BRSs0TctaTEniTD9t7%2FIBjqkAb9JyRWLrd8ApwgjnTUegssfufF8kCXhtWOwl%2FJ8Dd0%2B1b3zNr%2FXZzqOc%2B%2FoqTiIJQqqWO%2B7HSFDwyy73QQfgUqL3GXu%2BW3zpnJMIcAdjA3svoy0fH8DsB6iZFLjAml3x6oM4zyUoPetncqcH65cQpM6%2BylXCIVgAS819%2Fmku0l4L5l7zAEJYPkQJog4ee%2By8pWDYB7CXyu9nqwjSDlvq5Vo20ek&X-Amz-Signature=5d9dd7ad3534410411175965dd2bd39091a247484e8818411b565e3adf75a607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

