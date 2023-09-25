inputstring = str(input("Input string: "))
def solution(inputstring):
    index_brackets_array = []
    brackets_array = []
    cut_turple = []
    not_cut_turple = []
    arr = []
    old_arr = []
    length = len(inputstring)
    for i in range(length):
        if inputstring[i] == '(' or inputstring[i] == ')':
            index_brackets_array.append(i)
            brackets_array.append(inputstring[i])
    index_brackets_array.append('')
    brackets_array.append('')
    cut = ''
    #continue
    for i in range(len(index_brackets_array)-1):
        if brackets_array[i] == '(' and brackets_array[i+1] == '(':
            cut_turple.append((index_brackets_array[i],index_brackets_array[i+1]))
        elif brackets_array[i] == '(' and brackets_array[i+1] == ')' and brackets_array[i+2] != ')':
            cut_turple.append((index_brackets_array[i],index_brackets_array[i+1]))
        elif brackets_array[i] == '(' and brackets_array[i+1] == ')' and brackets_array[i+2] == ')':
            not_cut_turple.append((index_brackets_array[i],index_brackets_array[i+1]))
    cut = ''
    for i in range(len(cut_turple)):
        for j in range(cut_turple[i][0]+1, cut_turple[i][1]):
            cut = cut + inputstring[j]
        arr.append(cut)
        cut = ''
    for i in range(len(arr)):
        old_arr.append(arr[i])
    #reverse cut string
    cut = ''
    for i in range (len(arr)):
        for k in range(len(arr[i])):
            string = arr[i]
            cut = cut +  string[len(arr[i]) - k - 1]
        arr[i] = cut
        cut = ''
    for i in range(len(cut_turple)):
        for j in range(len(not_cut_turple)):
            if (not_cut_turple[j][0] > cut_turple[i][0]):
                if(not_cut_turple[j][1] > cut_turple[i][1]):
                    cut_turple[i] = not_cut_turple[j]
    outputstring = inputstring
    #concatenate string and cut string at the same time
    for i in range(len(old_arr)):
        outputstring = outputstring.replace(old_arr[i],'')
    outputstring_2 = ''
    for i in range(len(inputstring)):
        for j in range(len(arr)):
            if (i == (cut_turple[j][0] + 1)):
                for k in range(len(arr[j])):
                    outputstring_2 = outputstring_2 + arr[j][k]
        try:
            outputstring_2 = outputstring_2 + outputstring[i]
        except:
            pass
    #clear brackkets
    outputstring_3 = ''
    for i in range(len(outputstring_2)):
        if (outputstring_2[i] == '(' or outputstring_2[i] == ')'):
            continue
        else:
            outputstring_3 = outputstring_3 + outputstring_2[i]
    return(outputstring_3)

outputstring = solution(inputstring)
print(outputstring)