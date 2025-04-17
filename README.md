# Subtitle Offset Tool

A simple Python script to shift the timestamps in `.srt` subtitle files by a user-defined number of seconds — perfect for syncing subtitles with video content that has an intro, delay, or offset.

---

## Features

- Offsets subtitles by any number of seconds (positive or negative).
- Supports both forward and backward shifts.
- Automatically creates a new subtitle file with the offset in the filename (e.g., `video-offset-4s.srt`).
- No external libraries required — pure Python!

---

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/chad-butler-git/offset_srt.git
   cd subtitle-offset-tool
   ```

2. (Optional but recommended) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. No extra dependencies needed — just make sure you have Python 3.6+ installed.

---

## Usage

Run the script with the path to your `.srt` file and the desired offset in seconds:

```bash
python offset_srt.py <path-to-srt-file> <offset-in-seconds>
```

### Examples

```bash
# Add a 4-second delay to all subtitles
python offset_srt.py welcome.srt 4

# Move subtitles 2 seconds earlier
python offset_srt.py interview.srt -2
```

### Output

The output file will be saved in the same directory with a modified filename, such as:

- `welcome-offset-4s.srt`
- `interview-offset-2s.srt`

---

## Why Use This?

If your video contains an intro animation, splash screen, or delay that isn’t accounted for in your subtitle file, this script lets you easily adjust the timing without manual editing. Great for online course creators, editors, and video producers.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing

Feel free to fork the project and submit a pull request if you’d like to add features.

---

## Questions or Feedback?

Open an issue or reach out!
