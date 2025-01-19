# FG AI App

FG AI App is a simple app written in Python leveraging Ollama LLMs and Streamlit UI.
The intention of this app is to teach working with AI powered by locally installed LLMs (Large Language Models)
and quickly build a web based UI using the Streamlit library.

The app provides:

- Settings page to choose locally pulled Ollama models
- Chatbot
- Translator
- … more to come

## Installation

### Prerequisites
- Python 3.12 and later
- [Ollama](https://ollama.com) and downloaded [models](https://ollama.com/search) 
- Required libraries listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

### Download Ollama models
```bash
ollama pull <name-of-model>
```

### Show list of Ollama models
```bash
ollama list
```

Example output:
```
NAME                   ID              SIZE      MODIFIED    
phi4:latest            ac896e5b8b34    9.1 GB    6 days ago     
llama3.3:latest        a6eb4748fd29    42 GB     5 weeks ago    
qwen2.5-coder:14b      3028237cc8c5    9.0 GB    7 weeks ago    
mistral-nemo:latest    994f3b8b7801    7.1 GB    8 weeks ago    
llama3.2:3b            a80c4f17acd5    2.0 GB    8 weeks ago    
```

These are the models which are available in the app’s settings page. 

## How to run the app

```bash
streamlit run app.py
python -m streamlit run app.py    # Run configuration to start Streamlit from an IDE such as PyCharm
```

See screenshot of PyCharm run configuration below.

![PyCharm run configuration](assets/pycharm_run_config.png)

## Examples screenshot

![Settings](assets/screenshot.png)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Credits

Thanks to Sven Bosau for providing this [YouTube tutorial](https://youtu.be/9n4Ch2Dgex0?si=YJf8ME0B-nr4gQpo) and the [source code](https://github.com/Sven-Bo/python-multipage-webapp) for a multi page Streamlist app.
