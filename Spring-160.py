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
                    
                  
                                            
                     
                                            	
                    
              
                    
                
                      
                            
     

                    if i==2:
                        if  nameas="spring.spring"
                    
                            print("This not spring file!")
                            raise SystemExit 
                        C=1


         
                           
                                
                        
                                            
                    if i==1:
                        
                        nameas="spring.spring"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    File_information5=""
                    File_information5_2=""

                  
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0
                    

                    
                    
                        

                    
                                       
                    

 
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()

                        
                     
                            
                         
      
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
                                  

                                                                                             
                                    
                                    k1=-2
                                    k2=-1
                                    X1=1
                                    
                                    
                                   
                                    
 
                                    
                                    Extract1=0
                                    Times_10=1
                                    counts=-1
                                  
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
                                                    counts=-1
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
                                            counts+=1
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
                                                       Time_Real3=bin(lenf2)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real4=format(T1,'06b')
                                                       long_file=Time_Real4+Time_Real3






                                                 
                                                    
                                                       

                                                                          





                                                       
                                                       
                                                       C1=bin(X1)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"
                                                       
                                                       
                                                       Time_Real3=format(X1,C)
                                                       T1=len(Time_Real3)
                                                    
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       

                                                       XN=Time_Real4+Time_Real1+Time_Real3
                                                       C1=bin(counts)[2:]
                                                       C5=len(C1)
                                                       C2=C5//8
                                                       C4=C5%8
                                                       if C4!=0:
                                                           C3=(C2+1)*8
                                                       else:
                                                           C3=C2*8
                                                       C="0"+str(C3)+"b"

                                                      
                                                       Time_Real3=format(counts,C)
                                                       T1=len(Time_Real3)
                                                   
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'06b')
                                                       Counts=Time_Real4+Time_Real1+Time_Real3
                                                       






                                                       if int(INFO,2)==Number_of_the_file and File_information6_times2_1==Times_12:


                                                               File_information5_17="1"+XN+Counts+long_file
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

                                                
                                                f2.write(width_bits3)
                                                    
                                            
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            
                                            return xs;
                                    		
                                if i==2:
                                   


                                   

                                    
                                   
                   
                               
                                            
                                            
                                              

                                            
                                           
                                            
                           
                       
                                                            
                                              
                              

                                 

                                    
                                 
                                    if C==1:
                                        
                                        if   File_information6_times2==0:
                                            File_information5=INFO
                                            #print(INFO)
                                           
                                        if   File_information6_times2==0:
                                
                                                lenf6=len(File_information5)
                                                while File_information5[:1]!="1":
                                                    if File_information5[:1]=="0":
                                                        File_information5=File_information5[1:]
                                                        
                                                File_information5=File_information5[1:]
                                                #print(File_information5)
                                              
                                                #print(Extract_info)
                                                
                                               
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                XR=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                Real_C1=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]
                                                Extract_info=int(File_information5[:Real_C1],2)
                                                File_information5=File_information5[Real_C1:]
                                                Real_C=int(File_information5[0:6],2)
                                                File_information5=File_information5[6:]
                                                long=int(File_information5[:Real_C],2)
                                                File_information5=File_information5[Real_C:]                                                      
                                                #08122#17#18
                                    
                                    k1=-2
                                    k2=-1
                                    X1=1
                                   
                                    
                                   
                                    
 
                                    
                                    Extract1=0
                                    Times_10=1
                                  
                                    Times_11=-1
                                    Times_12=1
                                    University=-1
                                    
                                    Divided_corrdiates=1  
                                    counts=-1
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
                                                    counts=-1
                                                    
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
                                            counts+=1
                                            #print(counts)
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
                                           
    
                                            if i==2:
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
                                                if Extract_info==counts and File_information6_times2_1==Times_12 and X1==XR:
                                                       lenf=len(File_information5_17)










                                                 
                                                    
                                                       





                                                       if Extract_info==counts and File_information6_times2_1==Times_12 and X1==XR:
             


                                                               
                                                               CN="0"+str(long)+"b"
                                                               File_information5_17=format(Number_of_the_file,CN)

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

                                                
                                                f2.write(width_bits3)
                                                    
                                            
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            
                                            return xs;
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)#