import sys
import re
from pathlib import Path

def shift_timestamp(timestamp, offset_secs):
    hours, minutes, seconds_and_millis = timestamp.split(':')
    secs, millis = seconds_and_millis.split(',')
    total_millis = (int(hours) * 3600 + int(minutes) * 60 + int(secs)) * 1000 + int(millis)
    total_millis += offset_secs * 1000
    total_millis = max(0, total_millis)  # Prevent negative times

    new_hours = total_millis // 3600000
    total_millis %= 3600000
    new_minutes = total_millis // 60000
    total_millis %= 60000
    new_seconds = total_millis // 1000
    new_millis = total_millis % 1000
    return f"{new_hours:02}:{new_minutes:02}:{new_seconds:02},{new_millis:03}"

def shift_srt(input_file, offset_secs):
    pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    def shift_match(match):
        start, end = match.groups()
        return f"{shift_timestamp(start, offset_secs)} --> {shift_timestamp(end, offset_secs)}"

    shifted_content = pattern.sub(shift_match, content)
    
    # Output file name
    input_path = Path(input_file)
    offset_tag = f"-offset-{offset_secs:+d}s".replace("+", "")  # remove + for positive offsets
    output_path = input_path.with_name(f"{input_path.stem}{offset_tag}{input_path.suffix}")

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(shifted_content)

    print(f"✅ Offset SRT saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python offset_srt.py <path-to-srt-file> <offset-in-seconds>")
        print("Example: python offset_srt.py example.srt 4")
        sys.exit(1)

    input_srt = sys.argv[1]
    try:
        offset_seconds = int(sys.argv[2])
    except ValueError:
        print("❌ Error: Offset must be an integer (can be negative).")
        sys.exit(1)

    shift_srt(input_srt, offset_seconds)