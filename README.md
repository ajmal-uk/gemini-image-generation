# 🎨 Image Generation using Python + Google Gemini (Image Studio)

A powerful Python-based tool that combines the capabilities of **Gemini 1.5 Flash** (for AI-powered prompt enhancement) and **Gemini 2.0 Flash** (for fast, high-quality image generation). Enter a simple prompt, and let the AI enhance and convert it into a stunning image — outputted directly as base64.

---

## 🧠 Features

- 📝 Enhances user prompts using **Gemini 1.5 Flash** for rich image detail
- 🖼️ Generates high-quality AI images using **Gemini 2.0 Flash**
- 🧵 Automatically encodes the output image to **Base64**
- 🗂️ Saves image locally in a `static/` folder
- ⚡ Fast, efficient, and designed for developers & creators

---

## 📂 Project Preview

| Prompted Image Output | Folder Path | Terminal Run |
|-----------------------|-------------|--------------|
| ![cat](https://ik.imagekit.io/uthakkan/Github/cat-image-gen.png?updatedAt=1752562934001) | ![folder](https://ik.imagekit.io/uthakkan/Github/folder-location.png?updatedAt=1752562933711) | ![run](https://ik.imagekit.io/uthakkan/Github/run-view.png?updatedAt=1752562933713) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ajmal-uk/image-generation-using-python-google-gemini-image-studio.git
cd image-generation-using-python-google-gemini-image-studio
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up .env File
Create a .env file in the root directory:
```bash
GEMINI_TEXT_API_KEY=your_text_api_key_here
GEMINI_IMAGE_API_KEY=your_image_api_key_here
```

### 4. Run the Script
```bash
python main.py
```
Enter your image prompt when asked, and the enhanced result will be saved to the /static folder and encoded in Base64.


###  📦 requirements.txt
```bash
google-generativeai
python-dotenv
```

###  🧠 How It Works
- The GeminiChatBot class uses Gemini 1.5 Flash to enrich your prompt text.
- The enhanced prompt is sent to Gemini 2.0 Flash to generate image content.
- The image is saved locally and encoded in Base64 for flexible use in web or API integrations.


###  🛠 Tech Stack
- Python 3
- Google Generative AI (google-generativeai)
- dotenv for API key management
- Base64 encoding for image output


## 👨‍💻 Built with ❤️ by Ajmal UK
