digit_f=False
input_str=input("ваша строка ")
input_str=list(input_str)
for f in list(input_str):
    if f.isdigit():
        digit_f=True
        break
    else:
        digit_f=False
for f in list(input_str):
    if not f.isdigit():
        input_str.remove(f)
if digit_f==True:
    print(len(input_str))
else:
    print("цифры не обнаружены")

