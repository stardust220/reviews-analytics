data = []
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print("the average of review lens is", sum_len/len(d))

# filter the data if length is less than 100 words
new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print("the total number of the review which less than 100 words are", len(new))


good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print("the total number of the review which mentioned 'good' are", len(new))
print(good[0])

#list comprehension
good_2 = [d for d in data if 'good' in d]

bad = ['bad' in d for d in data]

