def printFrequency(strr):
    M = {}

    word = ""

    for i in range(len(strr)):

        if (strr[i] == ' '):

            if (word not in M):

                M[word] = 1

                word = ""

            else:

                M[word] += 1

                word = ""

        else:

            word += strr[i]

    if (word not in M):

        M[word] = 1

    else:

        M[word] += 1

    for it in M:
        print(it, "-", M[it])

strr = "Apple Apple boy boy boy boy token token frequency"
printFrequency(strr)