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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDV2P2J%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo%2Bjkz%2FgfdA1%2BZ%2FjQwoVMZFL7HUlVo2hzp1OI8f3fxvAIgaKRVvp3hc3EyQiFcRV18cCrkTlyvGKGh6eRzrFuzUYMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDUp%2FbO%2FeoDRNo5ACrcA6OuL9hoVOxzIMoSGeuS1cSLc4l6%2FW8Fa5neQ6yC9hZhkyrSgR%2F0ONXh1iEljH6Gy5USBFgRvNPsdTmeAqMiWOnVL%2BCe%2FTgP4GMazIiSVkxUAEyXQpQ3EiLYh0J0mlX9PJFMtFyRJ%2FQV3kosgvEvSRRMS6smD07IhHnAtf7PuOj2mcFp9x62U3kYuJSjSxe89ugpnSLwG6ITyioTSa7xN0epdWbRbGpVkI9EyOHLug2nyBQnPY3c8mOYSDAp4tryKNv7kW8Iui3o5nVyIEcIpPCyb2X2azsJ2nGC4BLcoEC0ig82UB28C4yLkwI0%2BXltndYdlbMBharRIJIjCSTqrWQUf3L0znZ6Ug9bTtE0qfnp1MNgeK5d9AWVI9Yc%2F74vRcM3PfjTp1V%2BJeX09GtPWaiTNjGi5HnPxG3%2FMvOCndNw2p7vkh1DIM6pQNHqS4AKV36eq1sVR6PDpvMQ2WJaqJAtTWJRHQzEaJJvBAAT8bq43c5jxnDEZRezt1VRRTb%2BVzptXnVjknCSwltvScgRVUbYYRJu%2BEmqkpSiSfBsFAaQHH%2BP0PFZpn%2BeaaV%2F5ZC7UsRjJuWbW1nmXKlE8U9oepVHBARqfPsEJz4qbjdT0okmMecElTZoPosFokY5MMDeo80GOqUB9IhTT6XHJbOQhzk4m2665XnUlNqjkL%2FqIVAIUhmgNQ7qpNnkbM47X55PDah2%2BrPj%2FmIZVxYxIg9AlxG2Tdmz4RO3SP49SFokjTN94%2B8i4WEi7xFosjYuqQwHalvS%2B%2FJwE9W22ZOwtfKV1O8BBOSb2x%2FE4NI5uk8J1AmSq3Hk1LlCy9pQdcjyl%2F4gpl%2F1zBT2cbiw%2Fi4%2FjFyO1QuzhJ6qPh6raKCr&X-Amz-Signature=575a566a8cb66897b3e295cce1bd1302405baa0a2632e51b9d1b0b710cb25aaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDV2P2J%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo%2Bjkz%2FgfdA1%2BZ%2FjQwoVMZFL7HUlVo2hzp1OI8f3fxvAIgaKRVvp3hc3EyQiFcRV18cCrkTlyvGKGh6eRzrFuzUYMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDUp%2FbO%2FeoDRNo5ACrcA6OuL9hoVOxzIMoSGeuS1cSLc4l6%2FW8Fa5neQ6yC9hZhkyrSgR%2F0ONXh1iEljH6Gy5USBFgRvNPsdTmeAqMiWOnVL%2BCe%2FTgP4GMazIiSVkxUAEyXQpQ3EiLYh0J0mlX9PJFMtFyRJ%2FQV3kosgvEvSRRMS6smD07IhHnAtf7PuOj2mcFp9x62U3kYuJSjSxe89ugpnSLwG6ITyioTSa7xN0epdWbRbGpVkI9EyOHLug2nyBQnPY3c8mOYSDAp4tryKNv7kW8Iui3o5nVyIEcIpPCyb2X2azsJ2nGC4BLcoEC0ig82UB28C4yLkwI0%2BXltndYdlbMBharRIJIjCSTqrWQUf3L0znZ6Ug9bTtE0qfnp1MNgeK5d9AWVI9Yc%2F74vRcM3PfjTp1V%2BJeX09GtPWaiTNjGi5HnPxG3%2FMvOCndNw2p7vkh1DIM6pQNHqS4AKV36eq1sVR6PDpvMQ2WJaqJAtTWJRHQzEaJJvBAAT8bq43c5jxnDEZRezt1VRRTb%2BVzptXnVjknCSwltvScgRVUbYYRJu%2BEmqkpSiSfBsFAaQHH%2BP0PFZpn%2BeaaV%2F5ZC7UsRjJuWbW1nmXKlE8U9oepVHBARqfPsEJz4qbjdT0okmMecElTZoPosFokY5MMDeo80GOqUB9IhTT6XHJbOQhzk4m2665XnUlNqjkL%2FqIVAIUhmgNQ7qpNnkbM47X55PDah2%2BrPj%2FmIZVxYxIg9AlxG2Tdmz4RO3SP49SFokjTN94%2B8i4WEi7xFosjYuqQwHalvS%2B%2FJwE9W22ZOwtfKV1O8BBOSb2x%2FE4NI5uk8J1AmSq3Hk1LlCy9pQdcjyl%2F4gpl%2F1zBT2cbiw%2Fi4%2FjFyO1QuzhJ6qPh6raKCr&X-Amz-Signature=4b585d1a79de355aaa3b60d76aa4f251751eebd7fa65dcb58295f4732943a1ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDV2P2J%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo%2Bjkz%2FgfdA1%2BZ%2FjQwoVMZFL7HUlVo2hzp1OI8f3fxvAIgaKRVvp3hc3EyQiFcRV18cCrkTlyvGKGh6eRzrFuzUYMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDUp%2FbO%2FeoDRNo5ACrcA6OuL9hoVOxzIMoSGeuS1cSLc4l6%2FW8Fa5neQ6yC9hZhkyrSgR%2F0ONXh1iEljH6Gy5USBFgRvNPsdTmeAqMiWOnVL%2BCe%2FTgP4GMazIiSVkxUAEyXQpQ3EiLYh0J0mlX9PJFMtFyRJ%2FQV3kosgvEvSRRMS6smD07IhHnAtf7PuOj2mcFp9x62U3kYuJSjSxe89ugpnSLwG6ITyioTSa7xN0epdWbRbGpVkI9EyOHLug2nyBQnPY3c8mOYSDAp4tryKNv7kW8Iui3o5nVyIEcIpPCyb2X2azsJ2nGC4BLcoEC0ig82UB28C4yLkwI0%2BXltndYdlbMBharRIJIjCSTqrWQUf3L0znZ6Ug9bTtE0qfnp1MNgeK5d9AWVI9Yc%2F74vRcM3PfjTp1V%2BJeX09GtPWaiTNjGi5HnPxG3%2FMvOCndNw2p7vkh1DIM6pQNHqS4AKV36eq1sVR6PDpvMQ2WJaqJAtTWJRHQzEaJJvBAAT8bq43c5jxnDEZRezt1VRRTb%2BVzptXnVjknCSwltvScgRVUbYYRJu%2BEmqkpSiSfBsFAaQHH%2BP0PFZpn%2BeaaV%2F5ZC7UsRjJuWbW1nmXKlE8U9oepVHBARqfPsEJz4qbjdT0okmMecElTZoPosFokY5MMDeo80GOqUB9IhTT6XHJbOQhzk4m2665XnUlNqjkL%2FqIVAIUhmgNQ7qpNnkbM47X55PDah2%2BrPj%2FmIZVxYxIg9AlxG2Tdmz4RO3SP49SFokjTN94%2B8i4WEi7xFosjYuqQwHalvS%2B%2FJwE9W22ZOwtfKV1O8BBOSb2x%2FE4NI5uk8J1AmSq3Hk1LlCy9pQdcjyl%2F4gpl%2F1zBT2cbiw%2Fi4%2FjFyO1QuzhJ6qPh6raKCr&X-Amz-Signature=3e71e180f297d31984a31c34af6006abb601d30d42598f1cc31e2558e0d87cff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

