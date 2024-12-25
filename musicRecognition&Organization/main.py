from shazamio import Shazam
import asyncio
import os

async def process_mp3_files(directory):
    shazam = Shazam()

    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            print(f"Processing: {filename}")

            try:
                with open(file_path, "rb") as mp3_file:
                    mp3_bytes = mp3_file.read()

                result = await shazam.recognize(mp3_bytes)

                if "track" in result:
                    track = result["track"]
                    title = track.get("title", "Unknown Title")
                    artist = track.get("subtitle", "Unknown Artist")

                    new_filename = f"{artist} - {title}.mp3"

                    new_filename = "".join(c for c in new_filename if c.isalnum() or c in " -_.")
                    new_file_path = os.path.join(directory, new_filename)

                    os.rename(file_path, new_file_path)
                    print(f"Renamed to: {new_filename}")
                else:
                    print(f"No song information found for: {filename}. Keeping the original name.")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Specify the directory containing MP3 files
    directory = 'ENTER YOUR DIRECTORY. example: D://Music'
    asyncio.run(process_mp3_files(directory))
