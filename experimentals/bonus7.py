from experimentals.bonus6_zipFunction import filename

filenames = ['doc.txt','report.txt','presentation.txt']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
print(filenames)