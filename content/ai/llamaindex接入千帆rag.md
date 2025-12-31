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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466543DJR33%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Wz7Jcwdeqi26AYYEPkv%2FSmaj%2Bvbs%2FxCNYhZBLeNBRQIgUbZmDa3IviVKQNue0n61ci1qPWIHCbtURfISlGa%2BbGsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdzhSkLtv4fcubEhyrcAx70U5L2e5VV7MxkdX%2F4gYYHfcIL6M3RMiCH%2FHlt%2F5qMJAjWHTsok%2B442nrrDiBVlz2hcngoCHA0hxeKY220tA89bafVBwTOLUqBv6nhs5OJKbmBInh1QRIdppsSMhHbE48FT%2B2r3uji2NDoGXNWo5NtABeBIcbTEITsdzzLTi5oz4%2Fzxnlw2UNH9Qmk71MzViPZC7vgfSJ0D1COsOBn4V7sP453AyMe1pO7Pbl0sIoUEMFp%2FGdhRmeBHAcLRxh2iTtSnuFAr5B9GUjyIoaLLfo3iW8QdMu7qZ9kcgWhURQ6FqVYok2vBPz4oSowFeViOk38YPeAk6SWfxlghx%2F6e5C0dGFHucKC4R9iDXtvjcDTSFr0wrWopO4wAeSa5yCUprSLmf8oPrFeqoCWl9F5Hej9whPXRAOH9%2FrIEkAmhhAX1d5UGHvF2f97QJQC5qR9pXzVb2wU1WJZptaDxw5kEcMyzklBbj8D0gItXYiOugf8XjQ3j4ekJjIcvFsw6nytl3tViBWRnHBpFNgZRvtDV7T3EBKlhefprXf1q2ThHBZ%2FkghnbEmKIHZp92WOiPzD3tlAg3lw4konuoOlq1G9t7HDLCoQAdPFwmKCCtwLQOD0ycDVtrkh583JyuXpMNf20coGOqUBM4MILPYWAXCeHHkBcyKiJcGutlB3FD%2BCN85GYzlX0NG%2BH%2BYYIXAyn2wGA%2B0tGDaLglF6yuCMr%2B63trVrNFr8zi9vUrPKvz%2BFiohX5nw3NqA%2B5WBRAOY%2F1%2Bb9YwIyswD9uaRnPBmjaU1noJGShTR4X0yZG%2Byd4Lk7UhG7jrCvZFAT7m27yDtIQvC6cR5%2B6hL26bgo3l2qB%2FsBmwqq1BvwqkbaFvqB&X-Amz-Signature=e0dfa1709b6554362a73566774f0a64ea238a084f2f344b781f8ad8c8e4840f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466543DJR33%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Wz7Jcwdeqi26AYYEPkv%2FSmaj%2Bvbs%2FxCNYhZBLeNBRQIgUbZmDa3IviVKQNue0n61ci1qPWIHCbtURfISlGa%2BbGsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdzhSkLtv4fcubEhyrcAx70U5L2e5VV7MxkdX%2F4gYYHfcIL6M3RMiCH%2FHlt%2F5qMJAjWHTsok%2B442nrrDiBVlz2hcngoCHA0hxeKY220tA89bafVBwTOLUqBv6nhs5OJKbmBInh1QRIdppsSMhHbE48FT%2B2r3uji2NDoGXNWo5NtABeBIcbTEITsdzzLTi5oz4%2Fzxnlw2UNH9Qmk71MzViPZC7vgfSJ0D1COsOBn4V7sP453AyMe1pO7Pbl0sIoUEMFp%2FGdhRmeBHAcLRxh2iTtSnuFAr5B9GUjyIoaLLfo3iW8QdMu7qZ9kcgWhURQ6FqVYok2vBPz4oSowFeViOk38YPeAk6SWfxlghx%2F6e5C0dGFHucKC4R9iDXtvjcDTSFr0wrWopO4wAeSa5yCUprSLmf8oPrFeqoCWl9F5Hej9whPXRAOH9%2FrIEkAmhhAX1d5UGHvF2f97QJQC5qR9pXzVb2wU1WJZptaDxw5kEcMyzklBbj8D0gItXYiOugf8XjQ3j4ekJjIcvFsw6nytl3tViBWRnHBpFNgZRvtDV7T3EBKlhefprXf1q2ThHBZ%2FkghnbEmKIHZp92WOiPzD3tlAg3lw4konuoOlq1G9t7HDLCoQAdPFwmKCCtwLQOD0ycDVtrkh583JyuXpMNf20coGOqUBM4MILPYWAXCeHHkBcyKiJcGutlB3FD%2BCN85GYzlX0NG%2BH%2BYYIXAyn2wGA%2B0tGDaLglF6yuCMr%2B63trVrNFr8zi9vUrPKvz%2BFiohX5nw3NqA%2B5WBRAOY%2F1%2Bb9YwIyswD9uaRnPBmjaU1noJGShTR4X0yZG%2Byd4Lk7UhG7jrCvZFAT7m27yDtIQvC6cR5%2B6hL26bgo3l2qB%2FsBmwqq1BvwqkbaFvqB&X-Amz-Signature=a7c40a07d382f03c45e35b63c10933e81fe52cbfb3624e01a1a1f70692c530dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

