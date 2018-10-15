import sys
with open(sys.argv[1], 'r') as f:
    contents = f.read()

ans = ['\x00'] * 100000
pointer = 0

length = len(contents)
i = 0
while(i < length):
    # print(ans)
    if(contents[i] == '>'):
        pointer += 1
    if(contents[i] == '<'):
        pointer -= 1
    if(contents[i] == '+'):
        ans[pointer] = chr(ord(ans[pointer]) + 1)
    if(contents[i] == '-'):
        ans[pointer] = chr(ord(ans[pointer]) - 1)
    if(contents[i] == '.'):
        print(ans[pointer], end='')
    if(contents[i] == ','):
        ans[pointer] = ord(input())
    if(contents[i] == '['):
        if(ans[pointer] == '\x00'):
            track = 1
            while(True):
                i += 1
                if(contents[i] == '['):
                    track += 1
                elif(contents[i] == ']'):
                    track -= 1
                    if(track == 0):
                        break
    if(contents[i] == ']'):
        if(ans[pointer] != '\x00'):
            track = 1
            while(True):
                i -= 1
                if(contents[i] == ']'):
                    track += 1
                elif(contents[i] == '['):
                    track -= 1
                    if(track == 0):
                        break
    i += 1
