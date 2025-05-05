"""
Lab 3, Task 4
Developer: Logovoy Artem Alekseevich
Date: 2025-07-04
Version: 1.0
Description: Analyze text for word count, 'z' word, exclude 'a' words.
"""

text = """So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."""

def task4():
    print("\n--- Задание 4: Анализ текста ---")
    words = text.replace(',', ' ').split()
    
    print(f"a) Количество слов: {len(words)}")

    for idx, word in enumerate(words, 1):
        if 'z' in word.lower():
            print(f"б) Первое слово с 'z': '{word}' (позиция {idx})")
            break
    else:
        print("б) Слов с 'z' не найдено.")
    
    filtered = [word for word in words if not word.lower().startswith('a')]
    print("в) Текст без слов на 'a':\n" + ' '.join(filtered))