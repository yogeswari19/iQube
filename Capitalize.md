def solve(s):
    m=[]
    t=s.split(" ")
    for i in range(0,len(t)):
        k=t[i].capitalize()
        m.append(k)
    return " ".join(m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
