import os
from openai import OpenAI
from RealtimeSTT import AudioToTextRecorder
from ui import UI
import threading

if __name__ == "__main__":
    # Setup OpenAI API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Speech-to-Text Recorder Setup
    recorder = AudioToTextRecorder(
        device="cpu",
        model="tiny.en",
        language="en",
        input_device_index=54,
    )

    def generate_response_translation(messages):
        """Generate translation using OpenAI."""
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=messages,
            stream=True
        )
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content
    
    def clear_console():
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def main():
        """Main function to run the translation loop."""
        clear_console()

        system_prompt_message = {
            'role': 'system',
            'content': f'Translate the given text to portuguese. Output only the translated text.'
        }

        ui = UI()
        t = threading.Thread(
            target=main_loop,
            args=(ui, system_prompt_message),
            daemon=True
        )

        t.start()
        ui.run()
    
    def main_loop(ui, system_prompt_message):
        """Main loop to capture speech and generate translations."""
        while True:
            # Capture user input from microphone
            user_text = recorder.text()
            ui.update_transcription("- " + user_text + "\n\n")

            user_message = {'role': 'user', 'content': user_text}

            ui.update_translation("- ")
            # Generate translation by OpenAI
            for chunk in generate_response_translation([system_prompt_message, user_message]):
                ui.update_translation(chunk)
            ui.update_translation("\n\n")

    main()
