# 🎨 AI Image Generator – Python + Gemini

<p align="center">
  <img src="https://ik.imagekit.io/uthakkan/Github/cat-image-gen.png?updatedAt=1752562934001" alt="Sample AI Image" width="400"/>
</p>

A powerful Python tool combining **Gemini 1.5 Flash** (for AI-powered prompt enhancement) and **Gemini 2.0 Flash** (for fast, high-quality image generation). Enter a prompt, let AI enhance it, and generate stunning images instantly — outputted directly as **Base64** and saved locally.

---

## 🧠 Features

* 📝 **Prompt Enhancement**: Gemini 1.5 Flash enriches your text prompts for rich image details
* 🖼️ **AI Image Generation**: Gemini 2.0 Flash creates high-quality images
* 🧵 **Base64 Encoding**: Automatically encodes generated images
* 🗂️ **Local Storage**: Saves output in the `static/` folder
* ⚡ **Fast & Developer-Friendly**: Ideal for AI creators, developers, and hobbyists

---

## 📂 Project Preview

| Prompted Output                                                                             | Folder Path                                                                                   | Terminal Run                                                                             |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ![Output](https://ik.imagekit.io/uthakkan/Github/cat-image-gen.png?updatedAt=1752562934001) | ![Folder](https://ik.imagekit.io/uthakkan/Github/folder-location.png?updatedAt=1752562933711) | ![Terminal](https://ik.imagekit.io/uthakkan/Github/run-view.png?updatedAt=1752562933713) |

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ajmal-uk/image-generation-using-python-google-gemini-image-studio.git
cd image-generation-using-python-google-gemini-image-studio
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Keys

Create a `.env` file in the root directory:

```bash
GEMINI_TEXT_API_KEY=your_text_api_key_here
GEMINI_IMAGE_API_KEY=your_image_api_key_here
```

### 4️⃣ Run the Script

```bash
python main.py
```

Enter your prompt and the AI-enhanced image will be saved in `/static` and encoded in Base64.

---

## 🛠 Tech Stack

* **Python 3** – Core programming language
* **Google Generative AI** – `google-generativeai` SDK for text & image generation
* **dotenv** – API key management
* **Base64** – Encoding images for API/web use

---

## 🧠 How It Works

1. **Prompt Enhancement** – `Gemini 1.5 Flash` enriches the user input text.
2. **Image Generation** – Enhanced prompt is passed to `Gemini 2.0 Flash` for creating images.
3. **Base64 Encoding & Storage** – Images are saved locally and encoded for flexible usage.

---

## 📦 Requirements

```txt
google-generativeai
python-dotenv
```

---

## 👨‍💻 Author

**Ajmal UK** – Passionate about AI, Python, and creative development.

---

## 📞 Contact

<p align="center">
  <a href="https://zymail.pythonanywhere.com">🌐 Website</a> • 
  <a href="mailto:contact.uthakkan@gmail.com">📧 Email</a> • 
  <a href="https://twitter.com/ZyMailApp">🐦 Twitter</a> • 
  <a href="https://github.com/ajmal-uk">🐙 GitHub</a>
</p>

