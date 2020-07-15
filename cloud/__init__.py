def makeCloudtext(words, counts):
 assert(len(words) == len(counts)), "input arrays must be of equal length"
 max_index = len(words)
 output_array = []
 word = ""
#shouldcreakout sep f for tag

 for i in range(0,max_index):
     word = words[i]
     tag = f"<h2>{word}</h2>"
     if counts[i] > 1:
         output_array.append(tag)
 return output_array    

def makeCloud(text_array):
    try:
        f = open("demo.html", "w")
        f.write(" ".join(text_array))
    except:
        print("failed")
    finally:
        f.close()