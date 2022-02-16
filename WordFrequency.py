
def main():
    outfile = "AI.txt"
    data = word_count(outfile)
    display(data)

def word_count(outfile):
    data = []
    file = open(outfile, 'r')
    lines = file.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word in data:
                data[word] += 1 
            else:
                data[word] = 1
    return data 

def display(data):
    for key in data:
        print(key, ' ', data[key])



main()