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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5W3SYY4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRxT92%2FMYbNo8X3i5w2ui%2FOUcL4VNfwmVsOT%2Fx%2FJ8fRgIhANSkTCkSn80gL2KAdbJuFgDV2Ac9Xc4H1BbcXGUBaPpVKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAkuihfiLO1GBB8j0q3AMdznIgLvuRcJNrI4SLdRGFjFlKob9mrJf3znu3sT3suXBKLxXmE%2FbZ%2B0DHxzvAfPMpNUDvpKnDoJ3Hm6yxcwa3eFNWQLyHmHJRC90SWSfyqZMHFjvn5195XggKu6z2goND%2BK%2FhG2dmTVxAMtw%2BNo%2Ffjg6ftwG2RwM%2FyfOkK91%2FU338gWZoATmWKiYv860k0FkOc1DrrdqfztC6bSTHErUFbb5p8jweQz3ceqBShqKg3fHEWO4f78hdmr7nyYwxVrWNXAxPPKU48kCRSh52BpUpWjnCxA2wIQm%2Bq8Za5kQDoVYwNv2vgkwotY%2FVSaHjn2cHQhRKf4ZbnCY1y93ILKu%2FjR1YJxbL5%2BVzqZhTBYtNMz%2FAtF5Q9ZWhGCGPC9X1oVOWy%2BZOEBbTNkVwKb%2Bi3uvIHb6KGE2%2F3pntvg8NsFN9QhxXEmHLJ8bImjUyzmoyz6qTJ5JnZOIUCF65FwfRxHrYZiaDDwD4HYMTd5jmrcID8jlIMO6DDkdnxwcDPa9Nfdr4E5vos%2BU7lw4IGCdeFy%2Fjf0Nb8NjGypNQXS8yihi8OrX0j660c5V2kc%2FYde7P45yl99OsYTkMER690nsTd3O4uZzYM4ydPUBQF5%2BIgXZY95BjPMhvweTdj8Ha9jCqzJ7JBjqkAVP%2FadRymjPf9R7Zu6EfkZHZZyVBVBreohwxRU0xREBAzbyWBNs8XK49k8zr7W9tQ0XcZpm9taVUT8VHcRqbWX4LXFsRVZis5qkuzLyDv4M5SFt0u69d67%2BwBTqbtFRtQg6ObvU6N3C1hkMy8wjK6zLNzzi6fkcm7OIdwciQxjb5tw0aDg0EipMyCq1qvUSDq%2BiS4DPuvBYEl4i6Vobfo405MSQQ&X-Amz-Signature=446bb1606db9625c29514ee808713501bac22951109c679e5a36c16f6141d482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5W3SYY4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRxT92%2FMYbNo8X3i5w2ui%2FOUcL4VNfwmVsOT%2Fx%2FJ8fRgIhANSkTCkSn80gL2KAdbJuFgDV2Ac9Xc4H1BbcXGUBaPpVKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAkuihfiLO1GBB8j0q3AMdznIgLvuRcJNrI4SLdRGFjFlKob9mrJf3znu3sT3suXBKLxXmE%2FbZ%2B0DHxzvAfPMpNUDvpKnDoJ3Hm6yxcwa3eFNWQLyHmHJRC90SWSfyqZMHFjvn5195XggKu6z2goND%2BK%2FhG2dmTVxAMtw%2BNo%2Ffjg6ftwG2RwM%2FyfOkK91%2FU338gWZoATmWKiYv860k0FkOc1DrrdqfztC6bSTHErUFbb5p8jweQz3ceqBShqKg3fHEWO4f78hdmr7nyYwxVrWNXAxPPKU48kCRSh52BpUpWjnCxA2wIQm%2Bq8Za5kQDoVYwNv2vgkwotY%2FVSaHjn2cHQhRKf4ZbnCY1y93ILKu%2FjR1YJxbL5%2BVzqZhTBYtNMz%2FAtF5Q9ZWhGCGPC9X1oVOWy%2BZOEBbTNkVwKb%2Bi3uvIHb6KGE2%2F3pntvg8NsFN9QhxXEmHLJ8bImjUyzmoyz6qTJ5JnZOIUCF65FwfRxHrYZiaDDwD4HYMTd5jmrcID8jlIMO6DDkdnxwcDPa9Nfdr4E5vos%2BU7lw4IGCdeFy%2Fjf0Nb8NjGypNQXS8yihi8OrX0j660c5V2kc%2FYde7P45yl99OsYTkMER690nsTd3O4uZzYM4ydPUBQF5%2BIgXZY95BjPMhvweTdj8Ha9jCqzJ7JBjqkAVP%2FadRymjPf9R7Zu6EfkZHZZyVBVBreohwxRU0xREBAzbyWBNs8XK49k8zr7W9tQ0XcZpm9taVUT8VHcRqbWX4LXFsRVZis5qkuzLyDv4M5SFt0u69d67%2BwBTqbtFRtQg6ObvU6N3C1hkMy8wjK6zLNzzi6fkcm7OIdwciQxjb5tw0aDg0EipMyCq1qvUSDq%2BiS4DPuvBYEl4i6Vobfo405MSQQ&X-Amz-Signature=edd7a0b1caf30d5ef73f401a9161357a187f9e02963bb62878785246dcf0ae07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

