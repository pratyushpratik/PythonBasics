'''
file write
'''
fw = open('simple.txt','w')
fw.write("hey this is pratyush pratik\n")
fw.write("live is hard")
fw.close()

'''
file read
'''
fr = open('simple.txt','r')
text = fr.read()
print(text)