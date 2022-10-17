
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_str = "142578 45абв44 ооооабв 87654"

target = "абв"

print(' ' .join([word for word in my_str.split() if not target in word]))

