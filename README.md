
# Text Completion Bot

Text Completion Bot is a simple web application that allows users to generate text completions using models hosted on Hugging Face's platform. 
Users can dynamically select from the latest text-generation models, input prompts, and customize generation parameters to get creative responses.

---

## Features

- Dynamically fetches the latest **text-generation** models from Hugging Face.
- Allows users to select models via a dropdown menu.
- Adjustable parameters for text generation:
  - **Maximum Length**: Set the maximum number of tokens to generate (min: 10, max: 500).
  - **Temperature**: Control creativity (higher = more creative).
- Displays total response time for each model's output.
- Provides error handling for:
  - Gateway timeouts (504 errors).
  - Forbidden access (403 errors) for models exceeding free-tier limits.

---

## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shreyasm007/text_completion_bot_hugging_face_API.git
   cd text_completion_bot_hugging_face_API
   ```

2. **Set Up the Environment**
   - Create a `.env` file in the root directory and add your Hugging Face API key:
     ```env
     HUGGINGFACE_API_KEY=your_api_key_here
     ```

3. **Install Dependencies**
   Ensure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the Streamlit app using the command:
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**
   - The application will open in your default web browser.
   - If not, navigate to `http://localhost:8501`.

---

## Dependencies

- `streamlit`: For creating the web interface.
- `requests`: To fetch models from Hugging Face's API.
- `huggingface_hub`: To interact with Hugging Face's inference API.
- `python-dotenv`: To securely manage API keys.

Install all dependencies via `requirements.txt`.

---

## Project Files

- **app.py**: The main application file.
- **.env**: Stores the Hugging Face API key.
- **requirements.txt**: List of required Python libraries.
- **README.md**: Project documentation.

---

## Features in Action

- **Model Selection**: Choose from the latest Hugging Face models tagged for text generation.
- **Customizable Parameters**: Adjust max length (10–500) and temperature (0.0–1.0).
- **Dynamic Output**: Get responses with the total time taken displayed.

---

## Error Handling

This application gracefully handles:
1. **Gateway Timeout (504)**: For models exceeding free-tier limits.
2. **Forbidden Access (403)**: For large models like `EleutherAI/gpt-j-6B`.

---

## Future Enhancements

- Add support for additional text-generation pipelines.
- Enable user authentication to save and manage prompts and outputs.
- Explore integrating fine-tuned models for domain-specific tasks.


---

## Acknowledgements

- [Hugging Face](https://huggingface.co) for their incredible models and API.
- [Streamlit](https://streamlit.io) for the intuitive app framework.

---

## Contribution

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

