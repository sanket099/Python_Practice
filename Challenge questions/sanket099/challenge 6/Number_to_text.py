#converting numbers to their text values 
#works for not more than three digit numbers

def num_to_words(num):
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy', ' eighty','ninety']
    teen = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    hundred = ['hundred']
    thousand = ['thousand']

    if len(num)==1 and int(num)<10:
        for i in range(11):
            k = int(num[0])
            if k==i:
                print(ones[i])
                break
            
    if len(num)==2:
        
        if int(num)<20:
            
        
            for i in range(1,11):
                k=int(num[1])
                if k==i:
                    
                    p = teen[i]
                    print(p)
                    break

        else:
            for i in range(1,11):
                j = int(num[0])
                
                if j == i:
                    y = tens[i]
                    print (y,end = "-")
                    break
                
            for t in range(1,11):
                k = int(num[1])
                if k==t:
                    o = ones[t]
                    print (o)
                    break
    if len(num) == 3:
        for i in range(1,11):
                j = int(num[0])
                if j == i:
                    y = ones[i]
                    print (y,"hundred and ",end = "")
                    break
        if (int(num[1]*10 + num[2])<10):
            for i in range(1,11):
                k=int(num[2])
                if k == i:
                    
                    p = teen[i]
                    print(p)
                    break
        else:
            for i in range(1,11):
                j = int(num[1])
                
                if j == i:
                    y = tens[i]
                    print (y,end = "-")
                    break
                
            for t in range(1,11):
                k = int(num[2])
                if k==t:
                    o = ones[t]
                    print (o)
                    break

#drivercode
num = input("enter")
num_to_words(num)
            
        
                        
            
            

        
            

                
        
        
        
          
            

            





        

                    
                
                    
                

     
    
    
