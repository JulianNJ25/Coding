lines = int(input())
language = ""
t_count = 0
s_count = 0

for line in range(lines):
    text = input( )
    
    for char in text:
        if char == 's' or char == 'S':
            s_count += 1
        if char == 't' or char == 'T':
            t_count += 1
    
if t_count > s_count:
    language = "English"
    print(language)
elif s_count > t_count:
    language = "French"
    print(language)
elif t_count == s_count:
    language = "French"
    print(language)
