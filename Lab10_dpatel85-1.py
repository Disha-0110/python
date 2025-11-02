"""
Program: Lab10_dpatel85-1.py (Word Frequency Counter)
Author: Disha Patel
Purpose: Count how often each word appears in a user-selected text file.
         Words are case-insensitive and punctuation is removed.
         Uses exception handling and the Path library.
Date: 2025-11-01
"""

from pathlib import Path

def printWds(data):
    for word in sorted(data.keys()):
        print(f"{word} : {data[word]}")
    return

def wordFreq(fptr):
    freq = {}
    punctChars = (".", ",", "!", "?", ":", ";", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_")
    line = fptr.readline()
    while line:
        for c in punctChars:
            line = line.replace(c, "")
        words = line.split()
        for word in words:
            tmp = word.lower()
            freq[tmp] = freq.get(tmp, 0) + 1
        line = fptr.readline()
    return freq

def main():
    try:
        filename = input("Enter the filename to read: ").strip()
        file_path = Path(filename)
        with file_path.open("r", encoding="utf-8") as fptr:
            data = wordFreq(fptr)
            printWds(data)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
