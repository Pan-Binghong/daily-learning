---
title: 基于Openai接口拓展模型
date: '2024-11-18T07:55:00.000Z'
lastmod: '2024-11-20T03:24:00.000Z'
draft: false
tags:
- Python
- API
categories:
- 后端
---

> 💡 记录一下，基于Openai API进行接口移植的过程，从引用api、测试、最后转接口部署。

---

### GPT-4o接口

```python
client = OpenAI(
    api_key=#这里就放入刚刚购买到的key就可以啦)
from opneai import OpenAI
def gpt_generate_text(prompt, messages_list):
    messages = ''    if messages_list:
        messages = '以下是你和用户的当前会话消息：\n\n' + '\n'.join(messages_list)
    stream = client.chat.completions.create(
        # model="gpt-4-turbo-preview",        model="gpt-4o",
        messages=[
            {"role": "system", "content": messages},
            {"role": "user", "content": prompt},
        ],
        stream=True    )
    text = ''    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            text += chunk.choices[0].delta.content
    return text
```

- 路由函数
---

## Whisper-1接口

- whisper-1模型(进行音频转文本)
```python
def transcribe_audio(audio_file):
    audio=open(audio_file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1",file=audio)
    text = transcription.text
    return text
```

- 路由函数
```python
@app.route("/transcribe", methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400    if audio_file:
        # 保存文件到临时位置        temp_file_path = os.path.join("temp", audio_file.filename)
        audio_file.save(temp_file_path)
        # 调用转录函数        transcription_text = transcribe_audio(temp_file_path)
        # 删除临时文件        os.remove(temp_file_path)
        return jsonify({"text": transcription_text})
```

> 首先我们要确定返回的请求中是否包含文件和文件名，如果没有，则返回错误信息和400，其次，我们需要保存文件到临时位置，然后调用我们写好的转录函数进行转录，最后删除临时文件。最后返回转录后的文本给客户端 供使用。

---

## TTS-1接口

- TTS-1(文本转换为语音)
```python
def text_to_speech(text, vocie, model, path):

    response = client.audio.speech.create(
        model=model,
        voice=vocie,
        input=text
    )
    speech_file_path = Path(path)
    with open(speech_file_path, 'wb') as file:
        file.write(response.content)

    print(f'文件已保存到: {speech_file_path}')
    return speech_file_path
```

- 路由函数
```python
app = Flask(__name__)
server_ip = ""  # 替换为你的服务器IP@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_endpoint():
    data = request.json
    text = data.get('text')
    voice = data.get('voice')
    model = data.get('model')
    output_path = './output.mp3'    if not text or not voice or not model:
        return {'error': 'Missing required parameters'}, 400    try:
        # Define the directory where you want to save the files        output_dir = Path('./audio_files')
        output_dir.mkdir(exist_ok=True)
        # Generate a unique filename using UUID        unique_filename = f"{uuid.uuid4()}.mp3"        output_path = output_dir / unique_filename
        # Generate the speech and save the file        speech_file_path = text_to_speech(text, voice, model, output_path)
        # Create the file URL        file_url = f"http://{server_ip}/root/xxx/{speech_file_path}"        # Return the file URL as a response        return jsonify({'file_url': file_url}), 200    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

> 首先我们要在后端代码中写入 我们的服务器ip地址我们要确保我们的json数据存在 四个键 text ， voice ， model ， output_path ，其次我们调用text_to_speech函数，传入text，voice，model，output_path，然后我们生成一个唯一的filename，保存到output_dir目录下最后我们生成一个file_url，然后返回给客户端。

---

## 测试截图

### gpt4o

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBDVRYTG%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGfP8Ry4ROBZ6KwsBVDMvZgTXhY8YPsI4QcSb2XzcFVoAiAHKThtqsPHq9WlXBkSNzQzgYNJI9yHPviRXCQWFvcvYSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMimus5By0ubRJTaRmKtwDhDsM1rj86ko6EkkeKYICdnvYidpsYL9RNskhQSkPKYwouTpEsksLEsUuZIQAo85YaKYSP%2BnHghLn%2BLbNxtyQZJ8EDxkE%2FkhYreVGZYnyBTKu%2B6cvWiFSsGDUcVp1qYM%2F2%2BDFfO15wvHgK%2FUCbq93sk0ZsHpn6a%2FNlRVNfs1YQiuDiiHW2S0sBWj6BZesDlzbP%2FCCg4iwX7IWzHglaftCPpN%2F%2B9DbKjHCcm%2BMDv9NL3TBuWKxZSQ%2FIoV9jDXVqQ0i762%2BlJDDtrIMJ2V9%2BvBc36uAkYo5iX7g4snwzQAX7wJLNcYFINKURQ7OZVypCZgKnxm7Yy7VEZMkg7mRbrczZ%2FAiKMPAV8vpoye%2FEuokNrRce28kJDIn3bGHTRHPYZ4U6kOyZCJjLKVB93aHAlDjp0l6RkkVWWm6kTmqOfarwx%2B2GZitn7DNCOZ1BnJc8mm7HPwT%2F1DXWP2c7NOLA7gZJBcs5mkuABw3GSaoxoHHVEYp8YSEJUjxIf5CEFjTcp4fM27NikHG%2BdQzsNzNxCOyZhxqdAJj3LdPVqSncaq1i%2B%2B%2FfPkYAJ5yNKas7x%2BHPYrz8n4awJ%2BuPIYmL4XebE7ydgwmYR5qy%2BCNMNu17LrZRGs5BHFy4NdlbY8Ni0kwgOvmzgY6pgF5406PzD1E0%2FlNEJxz%2FQzuBd%2B%2F8jRY0l%2Fql2t%2B4ySXytsQA67A0O6jPSy%2FBUrx1izCNxVB8fWepFIl9la1lLXqgzLkqvnzgUsM%2Fpkj9EUa85PGCxywHeIza%2B50B2Qqsrn86GjHgQOlcA7AZlVmKQSeA62qzD0MsPTZJecdRXId2%2BxnwrsRLozEsBFsKtdc%2Ff5A4dP7sWziIRNG7eaVJYSlGvX4J8q4&X-Amz-Signature=59be4a7283ddb5d18b0e8da939fcbfb080e0df19abe10b2c07ed75689c2077ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBDVRYTG%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGfP8Ry4ROBZ6KwsBVDMvZgTXhY8YPsI4QcSb2XzcFVoAiAHKThtqsPHq9WlXBkSNzQzgYNJI9yHPviRXCQWFvcvYSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMimus5By0ubRJTaRmKtwDhDsM1rj86ko6EkkeKYICdnvYidpsYL9RNskhQSkPKYwouTpEsksLEsUuZIQAo85YaKYSP%2BnHghLn%2BLbNxtyQZJ8EDxkE%2FkhYreVGZYnyBTKu%2B6cvWiFSsGDUcVp1qYM%2F2%2BDFfO15wvHgK%2FUCbq93sk0ZsHpn6a%2FNlRVNfs1YQiuDiiHW2S0sBWj6BZesDlzbP%2FCCg4iwX7IWzHglaftCPpN%2F%2B9DbKjHCcm%2BMDv9NL3TBuWKxZSQ%2FIoV9jDXVqQ0i762%2BlJDDtrIMJ2V9%2BvBc36uAkYo5iX7g4snwzQAX7wJLNcYFINKURQ7OZVypCZgKnxm7Yy7VEZMkg7mRbrczZ%2FAiKMPAV8vpoye%2FEuokNrRce28kJDIn3bGHTRHPYZ4U6kOyZCJjLKVB93aHAlDjp0l6RkkVWWm6kTmqOfarwx%2B2GZitn7DNCOZ1BnJc8mm7HPwT%2F1DXWP2c7NOLA7gZJBcs5mkuABw3GSaoxoHHVEYp8YSEJUjxIf5CEFjTcp4fM27NikHG%2BdQzsNzNxCOyZhxqdAJj3LdPVqSncaq1i%2B%2B%2FfPkYAJ5yNKas7x%2BHPYrz8n4awJ%2BuPIYmL4XebE7ydgwmYR5qy%2BCNMNu17LrZRGs5BHFy4NdlbY8Ni0kwgOvmzgY6pgF5406PzD1E0%2FlNEJxz%2FQzuBd%2B%2F8jRY0l%2Fql2t%2B4ySXytsQA67A0O6jPSy%2FBUrx1izCNxVB8fWepFIl9la1lLXqgzLkqvnzgUsM%2Fpkj9EUa85PGCxywHeIza%2B50B2Qqsrn86GjHgQOlcA7AZlVmKQSeA62qzD0MsPTZJecdRXId2%2BxnwrsRLozEsBFsKtdc%2Ff5A4dP7sWziIRNG7eaVJYSlGvX4J8q4&X-Amz-Signature=c56545e3a2df986b9eb8d3e0d9addd27a72eac7c3a876e1e70ea44c5cbff4f17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBDVRYTG%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGfP8Ry4ROBZ6KwsBVDMvZgTXhY8YPsI4QcSb2XzcFVoAiAHKThtqsPHq9WlXBkSNzQzgYNJI9yHPviRXCQWFvcvYSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMimus5By0ubRJTaRmKtwDhDsM1rj86ko6EkkeKYICdnvYidpsYL9RNskhQSkPKYwouTpEsksLEsUuZIQAo85YaKYSP%2BnHghLn%2BLbNxtyQZJ8EDxkE%2FkhYreVGZYnyBTKu%2B6cvWiFSsGDUcVp1qYM%2F2%2BDFfO15wvHgK%2FUCbq93sk0ZsHpn6a%2FNlRVNfs1YQiuDiiHW2S0sBWj6BZesDlzbP%2FCCg4iwX7IWzHglaftCPpN%2F%2B9DbKjHCcm%2BMDv9NL3TBuWKxZSQ%2FIoV9jDXVqQ0i762%2BlJDDtrIMJ2V9%2BvBc36uAkYo5iX7g4snwzQAX7wJLNcYFINKURQ7OZVypCZgKnxm7Yy7VEZMkg7mRbrczZ%2FAiKMPAV8vpoye%2FEuokNrRce28kJDIn3bGHTRHPYZ4U6kOyZCJjLKVB93aHAlDjp0l6RkkVWWm6kTmqOfarwx%2B2GZitn7DNCOZ1BnJc8mm7HPwT%2F1DXWP2c7NOLA7gZJBcs5mkuABw3GSaoxoHHVEYp8YSEJUjxIf5CEFjTcp4fM27NikHG%2BdQzsNzNxCOyZhxqdAJj3LdPVqSncaq1i%2B%2B%2FfPkYAJ5yNKas7x%2BHPYrz8n4awJ%2BuPIYmL4XebE7ydgwmYR5qy%2BCNMNu17LrZRGs5BHFy4NdlbY8Ni0kwgOvmzgY6pgF5406PzD1E0%2FlNEJxz%2FQzuBd%2B%2F8jRY0l%2Fql2t%2B4ySXytsQA67A0O6jPSy%2FBUrx1izCNxVB8fWepFIl9la1lLXqgzLkqvnzgUsM%2Fpkj9EUa85PGCxywHeIza%2B50B2Qqsrn86GjHgQOlcA7AZlVmKQSeA62qzD0MsPTZJecdRXId2%2BxnwrsRLozEsBFsKtdc%2Ff5A4dP7sWziIRNG7eaVJYSlGvX4J8q4&X-Amz-Signature=fea05b6f2261a3d63da2698ad992619480ab388b83fe488d41b7dd4513ad6dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

