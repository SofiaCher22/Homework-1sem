def is_vowel(char):
    return char in 'аеиоуыэюя'
def translate(text):
    result = []
    leng= len(text)
    for i in range(leng):
        char = text[i]
        result.append(char)       
        if is_vowel(char):
            if i > 0 and not is_vowel(text[i - 1]):
                result.append('с' + char)
    return ''.join(result)
with open('input.txt', 'r', encoding='utf-8') as file:
    input_text = file.read().strip()
translated_text = translate(input_text)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(translated_text)
print(translated_text)