str1 = "Hello"
str2 = "World"
text="  Python Is Awesome          "
result = str1 + " " + str2
print(result)
print("Uppercase:", result.lower())
print("Length Of The String:", len(result))
print("Modify Text:", result.replace("Hello", "Welcome my"))
print("Words:", text.split())
print("Stripped Text:", text.strip())
substring = "Is"
if substring in text:
    print(substring, "foud in the text")