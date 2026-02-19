import json

words = set()
with open('/usr/share/dict/words') as f:
    for line in f:
        w = line.strip()
        if len(w) == 5 and w.isalpha() and w == w.lower():
            words.add(w.upper())

sorted_words = sorted(words)
print(f"Total: {len(sorted_words)}")

with open('/Users/wangxinyi/Projects/wordle-game/wordlist.json', 'w') as f:
    json.dump(sorted_words, f)
