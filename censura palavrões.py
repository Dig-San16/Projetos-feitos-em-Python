palavrões = ["cu","pica","porra","foder"]

while True:
    a = input("|").lower().strip()
    for l in a.split():
        if l in palavrões:
            a = a.replace(l, len(l) * "#")
    if a:
        print(a,"\n")
    else:
        print(a,"\n")