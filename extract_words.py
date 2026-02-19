#!/usr/bin/env python3
import json

words = set()
with open('/usr/share/dict/words') as f:
    for line in f:
        w = line.strip()
        if len(w) == 5 and w.isalpha() and w == w.lower():
            words.add(w.upper())

sorted_words = sorted(words)
print(f"Total: {len(sorted_words)}")

rows = []
for i in range(0, len(sorted_words), 10):
    chunk = sorted_words[i:i+10]
    rows.append("'" + "','".join(chunk) + "'")

js_content = ",\n".join(rows)
with open('/Users/wangxinyi/Projects/wordle-game/words_out.txt', 'w') as f:
    f.write(js_content)
print("Done writing words_out.txt")
