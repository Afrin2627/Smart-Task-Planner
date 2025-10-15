import google.generativeai as genai

# Replace with your Gemini API key from https://aistudio.google.com/app/apikey
genai.configure(api_key="AIzaSyDb3RoQW3S6bA8L3fVukDpOCBvyu5UyI_Q")

print("📋 Listing available models...\n")
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)
