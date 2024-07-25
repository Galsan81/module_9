

def all_variants(text):
    for i in range(len(text)+1):
        for l in range(len(text) - i +1):

            yield text[l:l+i]


a = all_variants("abcdfsad")
for i in a:
    print(i)