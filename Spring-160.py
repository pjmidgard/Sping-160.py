import os
from time import time
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""


namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                           
                           
                            
                           
                              
                            if name=="f":
                                gh="f"
                                ge="f1"
                                os.rename(gh,ge)
                                name="f1"
                    else:
                            print('Path is not exists!')
                            raise SystemExit

                    x=0
                    C1=1
                    x1=0
                    x2=0
                    x3=0
                    
                    X2=0
                    C1=0
                    C2=0
                    C3=0
                    C4=0
                    C5=0
                    
                    
                    n=0
                    x = time()
                    File_information6_times2_1=0
                   
                   
                    
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    File_information6_times3=0
                    
                    with open("f.bin", "wb") as f2:
                                            
                      f2.write(width_bits3)                        
                                            	
                    
              
                    
                
                      
                            
     

                    if i==2:
                        if nameas=="f.bin":
                            print("This file It can't change!")
                            raise SystemExit
                          
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                                
                        
                                            
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    File_information5=""
                    File_information5_2=""

                  
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0
                    

                    
                    
                        

                    
                                       
                    

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        #if i==2:
                            #import paq
                            #data=paq.decompress(data)
                          
                        
                     
                            
                         
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        File_information6_times2=0
                                   
                        File_information5_23=""
 
                        INFO18=""
                        File_information5_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            File_information6_times3=File_information6_times3+1
                            D=1
                            if D==1:
                                if File_information6_times3==1:

                                 
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    lenf=len(INFO)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                            
                                    

                                    if File_information6_times3==1:
                                        File_information5_2=INFO
                            
                                    n = int(File_information5_2, 2)
                                
                                    width_bits=len(File_information5_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(INFO)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1

                                    File_information5_2=INFO
                                   
                                    
                                    
                                    Extact=File_information5_2
                                    A=int(Extact,2)
                                    

                                    lenf3=len(File_information5_2)
                                lenf2=len(File_information5_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**26)-1 and i==1:
                                        print("print file is too big!")
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:
                                    if  int(INFO,2)==0:
                                                    long_of_file=len(INFO)
                                                    
                                                    Nuber_zero_or_else=int(INFO,2)
                                                    long_of_file+=1
                                                    #print(long_of_file)
                                                    if Nuber_zero_or_else==0 and long_of_file<=(2**30)-1:
                                                                                                 long_of_file_N=format(long_of_file,'040b')
                                                                                                 Compress_zeros=long_of_file_N
                                                                                             
                                    
                                    k1=-2
                                    k2=-1
                                    X1=1
                                   
                                    
                                   
                                    
 
                                    
                                    Extract1=0
                                    Times_10=1
                                  
                                    Times_11=-1
                                    Times_12=1
                                    University=-1
                                    Divided_corrdiates=1  
                                    
                                    N_5=-1
                                    Times_7=0

                                    while Extract1!=1:
                                        
                                        

                                           
                                            
                                            
                                            k1+=1
                                            k2+=1
                                            
                                           
                                        
                                           
                                           
                                            
                                            
                                            #N_5+=1
                                            #Times_11+=1
                                    
                                            
                                            
                                            University=int(k2)
                                            X2=X1
                                            C11="0"+str(((8*X2)+40))+"b"
                                            
                                            if University>(2**((8*X1)+40)-1):
                                                    University=0
                                                    k1=-1
                                                    k2=0
                                                    
                                                    X1+=1                                          
                                            	
                                            if X1>44739242:
                                                University=0
                                                X1=1
                                                X2=1
                                            
                                            University_file=format(University,C11)
                                           
                                            

                                                
                                            
                                            Divided_corrdiates=int(University_file[0:(X2*8)],2)
                                            Times_12=int(University_file[(X2*8):(X2*8)+8],2)
                                            Times_10=int(University_file[(X2*8)+8:(X2*8)+16],2)
                                            Times_11=int(University_file[(X2*8)+16:(X2*8)+24],2)
                                            N_5=int(University_file[(X2*8)+24:(X2*8)+32],2)
                                            Times_7=int(University_file[(X2*8)+32:(X2*8)+40],2)
                                            if N_5>=68719476736:
                                                N_5=0
                                            elif Times_12>=2**26 and Times_10>=2**26 and N_5>=2**26 and Times_7>=2**26:
                                                Times_12=1
                                                Times_10=1
                                                N_5=0
                                                Times_7=0
                                                N_5=0

                                           
                                            
                                            
                                            
                                            
                                            
                                             

                                            
                                            if Divided_corrdiates==0:
                                            	Divided_corrdiates=1
                                            if Times_12==0:
                                                Times_12=1 
                                            
                                            if Times_10==0:
                                                Times_10=1 
                                           
                                            
        
                                             
                                            
                                             
                                                                                    
                                            
                                            
                                           
                            
                                           
                                            
                                          
                                          
                                           
                                       
                                            
 
                                            
                                            File_information52=""
                                            File_information53=""
                                            File_information54=""
                                            Add_N=""
    
                                           
                                            File_information52=format(N_5,'024b')
                                            File_information53=format(Times_10,'024b')
                                            
                                            

                                            Add_N=format(Times_11,'024b')
                                            if   File_information6_times2==0:
                                                File_information54=format(Times_7,'040b')
                                                File_information5_2=File_information54
                                                
                 

                                            
                                            File_information54=File_information5_2
 
                                           
                                             
                                            
                                           
                                            
                                            
                                            
                                                
                                            
                                            #print(B)
                                               
                                           
                                            
                                            File_information53=format(Times_10,'024b')                                            
                                            
                                                                                   
                                            
                                                                                         
                                                
                                            File_information5_2=File_information54
    
                                            
                                            File_information5_17=""
                                      
                                            
                                            
                                            lenf6=len(File_information54)
    
    
                                            add_bits=""
    
                                            Times_6=""
    
                                            #Extract
    
                                            INFO10=""
                                            Translate_info_Decimal=""
                                          
                                           
                                            Times_6=""
                                        
                                            Number_of_the_file=0
                                          
    
                                            C=1
                                         
                                            if C==1:
                                                if   File_information6_times2==0:
    
                                                         
    
                                                        
    
                                                        
                                                        
                                                        
                                                        lenf6=len(File_information54)
    
                                                        INFO10=File_information52
                                                        Deep5 = int(INFO10, 2)
                                                       
                                                      
                                                        
                                                        lenf6=len(File_information54)
                                                        File_information54=File_information5_2
                                                        
                                                      
                                                        
                                                        Times_6=File_information53
                                                        Add_N=Add_N
                                                        
                                                        T = int(Times_6, 2)
                                                        Add= int(Add_N, 2)
                                                        lenf6=len(File_information54)
                                                        #print("Deep: ")
                                                        #print(Deep7-25)
                                                        Times_half_Real=0
                                                if   File_information6_times2>0:
                                                        Translate_info_Decimal_2=0
                                                        
                                                
                                                        
            
                                                if C==1 and Times_12!=0:
                                                        File_information54=File_information54
                                                        lenf6=len(File_information54)
                                                       
                                                        
                                                       
                                                        if len (File_information54)!=0:
                        
                                                                                                    
                                                            Number_of_the_file=int(File_information54, 2)
                                                                                                     

                                                        else:
                                                            Number_of_the_file=0
                                          
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                
                                                
                                                                                         
                                                        Number_of_the_file=((((Number_of_the_file*add_ones_together)+Times_11)//3)*Times_10)//Divided_corrdiates

                                                        
                                                        
                                                        
                                                        Times_half_Real+=1
                                                        
                                                        
                                                        
                                                
                                        
                                                
                                                                                  
                                                
                                                
                                                        
                                               

                                              
                                            #####################################################################################################################################################
                                           
                                            
                                            
                                            
                                            File_information5_17=bin(Number_of_the_file)[2:]
                                             
                                            File_information5_2=File_information5_17
                                            #print(File_information5_17)
                                           
    
                                            if i==1:
                                                Make_togher=""
                                                Make_togher=Times_6
                                                
                                                add_bits=""
                                                if C==1 and Times_12!=0:
                                                        File_information6_times2=File_information6_times2+1
    
                                                lenf9=len(File_information5_17)
                                                #print(File_information6_times2)
                                                
                                                
                                                if  File_information6_times2==Times_12:
                                                        File_information6_times2_1=File_information6_times2
                                                        File_information6_times2=0
                                                        
                                                        
                                                        if int(INFO,2)==Number_of_the_file:  


                                                               if C==1:

                                                                       File_information5_17=bin(Number_of_the_file)[2:]
                                                                       lenf14=len(File_information5_17)



                                                                       lenf=len(File_information5_17)
                                                                       add_bits=""
                                                                       count_bits=8-lenf%8
                                                                       z=0
                                                                       if count_bits!=0:
                                                                               if count_bits!=8:
                                                                                   while z<count_bits:
                                                                                       add_bits="0"+add_bits
                                                                                       z=z+1


                                                                       File_information5_17=add_bits+File_information5_17
                                                                #print(File_information5_17)
                                                if int(INFO,2)==Number_of_the_file and File_information6_times2_1==Times_12:
                                                       lenf=len(File_information5_17)
                                                       add_bits=""
                                                       count_bits=8-lenf%8
                                                       z=0
                                                       if count_bits!=0:
                                                               if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1
                                                       File_information5_17=add_bits+File_information5_17        










                                                 
                                                    
                                                       

                                                       Time_Real3=bin(lenf2)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real4=format(T1,'06b')
                                                       long3=Time_Real4+Time_Real3
                                                       





                                                       
                                                       
                                                       C1=bin(Times_11)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                       
                                                       
                                                       Time_Real3=format(Times_11,C)
                                                       T1=len(Time_Real3)
                                                    
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       

                                                       Add_N=Time_Real4+Time_Real1+Time_Real3
                                                       C1=bin(Times_12)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"

                                                      
                                                       Time_Real3=format(Times_12,C)
                                                       T1=len(Time_Real3)
                                                   
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       Time_Real2=Time_Real4+Time_Real1+Time_Real3
                                                       
                                                       C5=len(C1)
                                                       C1=bin(N_5)[2:]
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                       


                                                       Time_Real3=format(N_5,C)
                                                       T1=len(Time_Real3)
                                                   
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       File_information52=Time_Real4+Time_Real1+Time_Real3
                                                       #print(File_information52)
                                                       C1=bin(Times_10)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                       
                                                      
                                                       Time_Real3=format(Times_10,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       File_information53=Time_Real4+Time_Real1+Time_Real3
                                                       C1=bin(Divided_corrdiates)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                    

                                                       
                                                       Time_Real3=format(Divided_corrdiates,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                    
                                                       
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       Divided_corrdiates1=Time_Real4+Time_Real1+Time_Real3
                                                       C1=bin(Times_7)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                    

                                                       
                                                       Time_Real3=format(Times_7,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       N10=Time_Real4+Time_Real1+Time_Real3





                                                       if int(INFO,2)==Number_of_the_file and File_information6_times2_1==Times_12:


                                                               File_information5_17="1"+File_information52+File_information53+Add_N+long3+Time_Real2+Divided_corrdiates1+N10
                                                               lenf=len(File_information5_17)
                                                               add_bits=""
                                                               count_bits=8-lenf%8
                                                               z=0
                                                               if count_bits!=0:
                                                                   if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1

                                                               File_information5_17=add_bits+File_information5_17
                                                               
                                                               Extract1=1
                                                      

                                                       if int(INFO,2)==0:
                                                               File_information5_17=Compress_zeros
                                                               lenf=len(File_information5_17)
                                                               add_bits=""
                                                               count_bits=8-lenf%8
                                                               z=0
                                                               if count_bits!=0:
                                                                   if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1

                                                               File_information5_17=add_bits+File_information5_17
                                                               Extract1=1
                                                    
                                                 
                                    if Extract1==1:                
                                            L=len(File_information5_17)
                                            n = int(File_information5_17, 2)
                                            width_bits=len(File_information5_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            add_bitszzza=""
                                            add_bitszs=""
                                            File_information5_2=Times_6
                                            
                                  
                                                            
                                            with open(nameas, "wb") as f2:
                                                #import paq
                                                #width_bits3=paq.compress(width_bits3)
                                                
                                                f2.write(width_bits3)
                                                    
                                            
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            
                                            return xs;
                                    		
                                if i==2:
                                   
                                    File_information5_17=""
                                    lenf9=len(File_information5_17)
                                    if  len(INFO)<=(5*8):
                                                 
                                                    File_information5_17=File_information5_17
                                                    #print(Number_zeroes)
                                                    Number_zeroes=int(INFO,2)
                                                    Number_zeroes-=1
                                                    File_information5_18=""
                                                   
                                                    Number_zeroes1=0
                                                    while Number_zeroes!=Number_zeroes1:
                                                            File_information5_18=File_information5_18+"0"
                                                            Number_zeroes1+=1
                                                    File_information5_17=File_information5_18

                                                    lenf=len(File_information5_17)
                                                    add_bits=""
                                                    count_bits=8-lenf%8
                                                    z=0
                                                    if count_bits!=0:
                                                            if count_bits!=8:
                                                                    while z<count_bits:
                                                                            add_bits="0"+add_bits
                                                                            z=z+1

                                                    File_information5_17=add_bits+File_information5_17

                                                    L=len(File_information5_17)

                                                    n = int(File_information5_17, 2)

                                                    width_bits=len(File_information5_17)

                                                    width_bits=(width_bits//8)*2

                                                    width_bits=str(width_bits)
                                                    width_bits="%0"+width_bits+"x"
                                                    width_bits3=binascii.unhexlify(width_bits % n)
                                                    width_bits2=len(width_bits3)
                                                    add_bitszzza=""
                                                    add_bitszs=""
                                                    File_information5_2=Times_6
                                                    with open(nameas, "wb") as f2:
                                                            f2.write(width_bits3)
                                                    x2 = time()
                                                    x3=x2-x
                                                    xs=float(x3)
                                                    xs=str(xs)
                                                    
                                                    return xs;
                                   

                                    
                                   
                   
                               
                                            
                                            
                                              

                                            
                                           
                                            
                           
                       
                                                            
                                              
                              
                                    File_information5=File_information5_2
                                   
                                    
                                   
                                    
                                    
                                    
                                    lenf6=len(File_information5)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    INFO10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                  
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    
                                 

                                    
                                 
                                    if C==1:
                                        
                                        if   File_information6_times2==0:
                                            File_information5=INFO
                                           
                                        if   File_information6_times2==0:
                                
                                                lenf6=len(File_information5)
                                                while File_information5[:1]!="1":
                                                    if File_information5[:1]=="0":
                                                        File_information5=File_information5[1:]
                                                        
                                                File_information5=File_information5[1:]
                                               

                                                #08122#17#18
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                                                                
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                Deep5=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                            


                                                #08014 #15
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                T_Real=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                           
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                Add=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                                   

                                                #18020d47 #11
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                long=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit          
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                T14=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                                                                             
                                                


                                                #0010ffff #6
                                                
                                                
                                                Reality=T14
                                                #000801 #3
                                                
                                                
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                Divided_corrdiates=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                                   
                                                
                                                if len(File_information5)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                N10=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]                                                   
                                                #print(N10)
                                                

                                            
                                                
                                                lenf6=len(File_information5)
                                                Reality2=0
                                                
                    
                                                if T14==0:
                                                    T14=1
                                                
                                                if Divided_corrdiates==0:
                                                    Divided_corrdiates=1
                                                
                                                
                                                
                                            

                                                #print(T14)
                                        
                                                #print(Reality)
                                              


                                                #print(Reality)
                                        
                                                
                                        if   File_information6_times2>0:
                                        	Translate_info_Decimal_2=0
                                       
                                      
                                        	
                                        	
                                        
                                        	
    
                                        if C==1 and T14!=0:
                                                File_information5=File_information5
                                                lenf6=len(File_information5)
                                                


                                        if len (File_information5)!=0:
                        
                                                                                                    
                                                    Number_of_the_file=int(File_information5,2)
                                                    #print(Number_of_the_file)

                                        else:
                                                     Number_of_the_file=N10
                                                 
                                                     
                                        if Reality2<Reality:
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                        Reality2+=1
                                                        if T_Real==0:
                                                            T_Real=1                                                        
                                                        Number_of_the_file=((((Number_of_the_file*add_ones_together)+Add)//3)*T_Real)//Divided_corrdiates

                                                 
                                                        #print(Number_of_the_file)
                                             
                                    #####################################################################################################################################################
                                   
                                    
                                    
                                    
                                    File_information5_17=bin(Number_of_the_file)[2:]
                                     
                                    File_information5_2=File_information5_17
                                   

                                    if i==2:

                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T14!=0:
                                                File_information6_times2=File_information6_times2+1

                                        lenf9=len(File_information5_17)
                                        #print(File_information6_times2)
                                        
                                        
                                          
                                        
                                                
                                        if  File_information6_times2==T14:
                                        	   
                                            if C==1 and T14==0:
                                            	File_information5_17=File_information5
                                            	lenf=len(File_information5_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	File_information5_17=add_bits+File_information5_17


                                            	
                                            	lenf=len(File_information5_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	File_information5_17=add_bits+File_information5_17
                                            	
                                            
                                     
                                            if C==1 and T14!=0:
 
                                            	File_information5_17=bin(Number_of_the_file)[2:]
                                            	lenf14=len(File_information5_17)
                                            	lenf=len(File_information5_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	File_information5_17=add_bits+File_information5_17

                                            	
                                            	lenf=len(File_information5_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	File_information5_17=add_bits+File_information5_17
                                            	        
                                            	#print(lenf14)

                                            		
                                            	
                                            	
                                            L=len(File_information5_17)
                                         
                                            n = int(File_information5_17, 2)
                                            #############binary to data
                                            width_bits=len(File_information5_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            ####
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            File_information5_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)

                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            
                                            return xs;
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
