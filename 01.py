# 1. Привести строку к единому регистру (например, нижнему), чтобы сравнение было
# регистронезависимым.
# 2. Удалить из строки все пробелы и небуквенные символы (если требуется)
# 3. Создать перевёрнутую (обратную) версию строки
# 4. Сравнить исходную строку с перевёрнутой
#    - Если они совпадают, строка — палиндром
#    - Если не совпадают, строка не палиндром
# 5. Вернуть результат в удобочитаемом формате

def check_palindrome(s: str) -> str:
       s = s.lower()
       cleaned = ''.join(char for char in s if char.isalnum())
       if cleaned == cleaned[::-1]:
           return f"✅ '{s}' — это палиндром!"
       else:
           return f"❌ '{s}' — это НЕ палиндром!"


print(check_palindrome("А роза упала на лапу Азора"))  # ✅
print(check_palindrome("Racecar"))  # ✅
print(check_palindrome("Python"))  # ❌
print(check_palindrome("12321"))  # ✅
print(check_palindrome("Hello, world!"))  # ❌