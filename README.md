
# YouTube Playlist Sorting Script

This Python script allows you to interact with a YouTube playlist using the YouTube Data API v3. It fetches the items from the playlist, extracts relevant video details such as titles and artists, and sorts the videos alphabetically by the artist name. The sorted list is then saved to a CSV file for further use or analysis.

## Features

- Fetches video items from a YouTube playlist using the YouTube Data API v3.
- Extracts video information, including video title, ID, and artist (from the title).
- Sorts the videos alphabetically by artist name.
- Saves the sorted video list to a CSV file with a timestamped filename.
- Handles pagination if the playlist contains more than 50 videos.

## Requirements

Before running the script, make sure you have the following Python libraries installed:

- `requests`: For making HTTP requests to the YouTube Data API.
- `pandas`: For handling and manipulating the video data, as well as saving the sorted list into a CSV file.
- `colorama`: For colored output in the terminal.
- `datetime`: To timestamp the saved CSV file.
- `random`: For adding randomness, if needed.

You can install the necessary libraries by running the following command:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Get Your YouTube API Key

To interact with the YouTube Data API, you need a valid API key. Follow the instructions below to get your API key:

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project or select an existing one.
3. Navigate to the "APIs & Services" section, then "Library."
4. Search for "YouTube Data API v3" and enable it.
5. Go to "Credentials" in the left menu and click "Create Credentials" to generate an API key.

### 2. Get Your Playlist ID

The playlist ID is part of the URL of the YouTube playlist. For example, in the following URL:

```
https://www.youtube.com/playlist?list=PL12345ABCDEF
```

The playlist ID is `PL12345ABCDEF`.

### 3. Update API Key and Playlist ID in the Script

Open the script and replace the placeholders for `API_KEY` and `PLAYLIST_ID` with your actual values:

```python
API_KEY = 'YOUR-API-KEY-HERE'
PLAYLIST_ID = 'YOUR-PLAYLIST-ID-HERE'
```

## Usage

Once you've set up the API key and playlist ID, you can run the script to fetch the playlist items, process them, and save the sorted data.

1. Clone or download the repository containing the script.
2. Open a terminal or command prompt in the directory where the script is located.
3. Run the Python script:

```bash
python your_script_name.py
```

The script will fetch the videos from the playlist, sort them by artist name, and save them as a CSV file in the same directory. The file will be named with a timestamp, such as `sorted_playlist_dd_mm_yyyy_hh-mm-ss.csv`.

### Example Output

After running the script, you will see a success message similar to this:

```bash
sorted_playlist_25_12_2024_12-30-45.csv file saved successfully to /path/to/your/directory
```

The CSV file will contain the following columns:

- `title`: The title of the video.
- `video_id`: The unique video ID for the YouTube video.
- `artist`: The artist name extracted from the video title.

## Notes

- The script handles Unicode characters and path-related issues using the `safe_chdir` function.
- If the playlist contains more than 50 videos, the script will handle pagination and continue fetching the remaining videos.
- Ensure that the artist information can be correctly extracted from the video title. The script assumes that the artist's name is present in the title in one of these formats: `Artist - Song Title` or `Artist | Song Title`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
