with open("output.tsv", "w") as text_file:
    with open('C:\Python34\\access.log', 'r') as f:
        for line in f:
            arr=line.split(' ')
        #print(line)
        #print(arr)
        #if len(arr)> 18 :  print(arr[0]+' '+arr[3]+' '+arr[5]+' '+arr[6]+' '+arr[7]+' '+arr[8]+' '+arr[9]+' '+arr[10]+' '+arr[17])
            if len(arr)> 10 : text_file.writelines(arr[0]+'\t'+arr[3]+'\t'+arr[5]+'\t'+arr[6]+'\t'+arr[7]+'\t'+arr[8]+'\t'+arr[9]+'\t'+arr[10]+'\n')  ##print(arr[0]+'\t'+arr[3]+'\t'+arr[5]+'\t'+arr[6]+'\t'+arr[7]+'\t'+arr[8]+'\t'+arr[9]+'\t'+arr[10])
            if len(arr)< 10 : text_file.writelines(arr[0]+'\t'+arr[3]+'\t'+arr[5]+'\t'+arr[6]+'\t'+arr[7]+'\t'+arr[8]+'\t'+arr[9]+'\t'+arr[10]+'\n')  # print(arr[0]+'\t'+arr[3]+'\t'+arr[5]+'\t'+arr[6]+'\t'+arr[7]+'\t'+arr[8]+'\t'+arr[9])
