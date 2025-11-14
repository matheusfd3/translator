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
        model="tiny.en",
        device="cpu",
        input_device_index=54,
    )

    def generate_response(messages):
        """Generate assistant's response using OpenAI."""
        response = client.chat.completions.create(
            model="gpt-5-nano",
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
        """Main translation loop."""
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
        while True:
            print("\nSay something!")

            # Capture user input from microphone
            user_text = recorder.text()
            ui.update_transcription("- " + user_text + "\n\n")
            print(f"Input text: {user_text}")

            user_message = {'role': 'user', 'content': user_text}

            # Stream translation
            ui.update_translation("- ")
            print("Translation: ", end="", flush=True)
            for chunk in generate_response([system_prompt_message, user_message]):
                ui.update_translation(chunk)
                print(chunk, end="", flush=True)
            ui.update_translation("\n\n")
            print()
    main()
