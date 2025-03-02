import logging
from pocketsphinx import LiveSpeech
from openai import OpenAI
from gtts import gTTS
import io
import pygame
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize pygame mixer
if not pygame.mixer.get_init():
    pygame.mixer.init()

class SpeakToAI:
    def __init__(self):
        # Set your OpenAI API key and system prompt here
        self.api_key = "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"
        self.system_prompt = "You are Sarah, a friendly and experienced career coach. Your role is to provide advice on improving skills for various job roles. You are approachable, empathetic, and always ready to help. Your advice should be professional, actionable, and tailored to the individual's needs. Be concise and to the point, but also make the conversation feel natural and engaging. Ask questions to understand their situation better and offer practical tips that they can start implementing right away. Let's work together to help them reach their career goals!"
        self.model = "openchat/openchat-7b:free"
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key
        )
        self.conversation_history = []

    def recognize_speech(self):
        try:
            speech = LiveSpeech()
            for phrase in speech:
                logger.info(f"Recognized: {phrase}")
                return str(phrase)
        except Exception as e:
            logger.error(f"Error in speech recognition: {e}")
            raise

    def send_message(self, user_input):
        try:
            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history,
                {"role": "user", "content": user_input},
            ]

            completion = self.client.chat.completions.create(
              model=self.model,
              messages=messages,
              extra_headers={
                "HTTP-Referer": "https://your-website.com", # Replace with your website URL
                "X-Title": "Your website name",           # Replace with your website name
              }
            )

            response_text = completion.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": response_text})

            return response_text

        except Exception as e:
            logger.error(f"Error in processing text: {e}")
            return "Failed to retrieve response."

    def speak(self, text, language="en"):
        try:
            tts = gTTS(text=text, lang=language)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)

            pygame.mixer.music.load(audio_fp)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            audio_fp.close()

        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
            raise

    def run(self):
        while True:
            # Recognize speech
            user_input = self.recognize_speech()
            if user_input.lower() == 'exit':
                break

            # Send message to OpenAI
            response = self.send_message(user_input)
            logger.info(f"AI Response: {response}")

            # Convert response to speech
            self.speak(response)

# Initialize SpeakToAI and start the conversation loop when the module is run directly
if __name__ == '__main__':
    speak_to_ai = SpeakToAI()
    speak_to_ai.run()
