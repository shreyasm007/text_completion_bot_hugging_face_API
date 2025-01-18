
# Text Completion Bot

A simple web application that uses Hugging Face's Inference API to generate text completions based on user input. This project is built with **Streamlit** for the frontend and allows dynamic selection of models for text generation.

---

## 🚀 Features

- **Dynamic Model Selection**: Choose from a variety of models hosted on Hugging Face, such as `gpt2`, `EleutherAI/gpt-neo`, and more.
- **Interactive UI**: User-friendly interface built with Streamlit.
- **Customizable Parameters**:
  - `Max Length`: Set the maximum length of the generated text.
  - `Temperature`: Control the creativity of the output.
- **Environment Variable Support**: Securely manage API keys using a `.env` file.

---

## 📦 Installation and Setup

### Prerequisites

- Python 3.7 or later
- A [Hugging Face API Key](https://huggingface.co/settings/tokens)
- Streamlit

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shreyasm007/text_completion_bot_hugging_face_API.git
   cd text_completion_bot_hugging_face_API
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**:
   Create a `.env` file in the root directory and add your Hugging Face API key:
   ```
   HUGGINGFACE_API_KEY=your_api_key_here
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**:
   The app will run locally on [http://localhost:8501](http://localhost:8501).

---

## 🛠️ Usage

1. **Enter a Prompt**:
   Input any text in the prompt field to guide the text generation.

2. **Set Parameters**:
   - Adjust the `Max Length` slider to control the length of the generated text.
   - Modify the `Temperature` slider to tweak the creativity of the output.

3. **Choose a Model**:
   Enter the name of a Hugging Face model (e.g., `gpt2`, `EleutherAI/gpt-neo`) in the "Model Name" input field.

4. **Generate Text**:
   Click the "Generate Text" button to see the output.

---

## 🌟 Example Output

**Prompt**: "The future of AI is"  
**Output**: "The future of AI is bright. With advancements in machine learning, artificial intelligence is set to revolutionize industries, improve lives, and unlock new possibilities."

---

## 🗂️ Project Structure

```
text-completion-bot/
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not shared publicly)
└── README.md            # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository, make your changes, and submit a pull request.

---

## 🙌 Acknowledgements

- [Hugging Face](https://huggingface.co/) for their powerful APIs.
- [Streamlit](https://streamlit.io/) for their easy-to-use app framework.
