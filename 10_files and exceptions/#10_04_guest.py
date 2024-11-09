#write_txt 
from pathlib import Path

contents = "programming.txt"


path = Path('programming.txt')
path.write_text("contents")

