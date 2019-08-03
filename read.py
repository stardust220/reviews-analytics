data = []
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print("the average of review lens is", sum_len/len(d))