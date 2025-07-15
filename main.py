import uuid
import os
import base64
from dotenv import load_dotenv
import google.generativeai as genai_text
from google import genai as genai_image
from google.genai import types

load_dotenv()
TEXT_API_KEY = os.getenv("GEMINI_TEXT_API_KEY")
IMAGE_API_KEY = os.getenv("GEMINI_IMAGE_API_KEY")

genai_text.configure(api_key=TEXT_API_KEY)

class GeminiChatBot:
    def __init__(self, system_prompt=None):
        self.system_prompt = system_prompt or (
            "You are a professional prompt optimizer for image generation. "
            "Transform user requests into rich, vivid, detailed, efficient prompts."
        )
        self.model = genai_text.GenerativeModel(
            model_name="gemini-1.5-flash-8b",
            system_instruction=self.system_prompt.strip(),
            generation_config={
                "temperature": 0.85,
                "top_p": 1,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }
        )
        self.chat = self.model.start_chat(history=[])

    def enhance_prompt(self, user_prompt: str) -> str:
        try:
            response = self.chat.send_message(user_prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Prompt enhancement failed: {e}")
            return user_prompt 


def generate_image_base64(user_prompt):
    try:
        enhancer = GeminiChatBot()
        enhanced_prompt = enhancer.enhance_prompt(user_prompt)
        print(f"\n[Enhanced Prompt]\n{enhanced_prompt}\n")

        client = genai_image.Client(api_key=IMAGE_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=enhanced_prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                image_filename = f"generated_image_{uuid.uuid4()}.png"
                image_path = os.path.join("static", image_filename)

                with open(image_path, "wb") as f:
                    f.write(image_data)

                with open(image_path, "rb") as f:
                    image_base64 = base64.b64encode(f.read()).decode("utf-8")

                with open('a.txt', 'w') as f:
                    f.write(image_base64)

                return f"data:image/png;base64,{image_base64}"

        raise ValueError("No image data found in the response.")

    except Exception as e:
        print(f"Image generation failed: {e}")
        raise RuntimeError("Image generation failed.")


if __name__ == "__main__":
    user_input = input("🎨 Enter your image prompt: ")
    result = generate_image_base64(user_input)
    print("\n[Image Base64 Output Snippet]\n" + result[:300] + "...")
