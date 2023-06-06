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
                    Circle_times2_1=0
                   
                   
                    
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
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

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                  
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
                        if i==2:
                            import paq
                            data=paq.decompress(data)
                          
                        
                     
                            
                         
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        INFO18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    lenf=len(INFO)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=INFO
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
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

                                    Equal_info_between_of_the_cirlce_of_the_file_2=INFO
                                   
                                    
                                    
                                    Extact=Equal_info_between_of_the_cirlce_of_the_file_2
                                    A=int(Extact,2)
                                    

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
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
                                                                                             
                                    from qiskit.circuit import QuantumCircuit
                                    k1=-2
                                    k2=-1
                                    X1=1
                                   
                                    
                                   
                                    circuit = QuantumCircuit(2**805306368)
 
                                    
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
                                            
                                           
                                        
                                            if k1==2**805306368:
                                                k1=-1
                                                k2=0
                                              
                                           
                                           
                                            
                                            
                                            #N_5+=1
                                            #Times_11+=1
                                    
                                            circuit.cp(University, k1, k2)
                                            
                                            University=int(k2)
                                         
                                            C11="0"+str(805306368)+"b"
                                            
                                            if University>(2**805306368)-1:
                                                    University=0
                                                    k1=-1
                                                    k2=0
                                                    
                                                                                         
                                            	
                                            
                                            
                                            University_file=format(University,C11)
                                           
                                            

                                                
                                            
                                            Divided_corrdiates=int(University_file[0:134217728],2)
                                            Times_12=int(University_file[134217728:268435456],2)
                                            Times_10=int(University_file[268435456:402653184],2)
                                            Times_11=int(University_file[402653184:536870912],2)
                                            N_5=int(University_file[536870912:671088640],2)
                                            Times_7=int(University_file[671088640:805306368],2)

                                           
                                            
                                            
                                            
                                            
                                            
                                             

                                            
                                            if Divided_corrdiates==0:
                                            	Divided_corrdiates=1
                                            if Times_12==0:
                                                Times_12=1 
                                            
                                            
                                            
        
                                             
                                            
                                             
                                                                                    
                                            
                                            
                                           
                            
                                           
                                            
                                          
                                          
                                           
                                       
                                            
 
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file2=""
                                            Equal_info_between_of_the_cirlce_of_the_file3=""
                                            Equal_info_between_of_the_cirlce_of_the_file4=""
                                            Add_N=""
    
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file2=format(N_5,'024b')
                                            Equal_info_between_of_the_cirlce_of_the_file3=format(Times_10,'024b')
                                            
                                            

                                            Add_N=format(Times_11,'024b')
                                            if   Circle_times2==0:
                                                Equal_info_between_of_the_cirlce_of_the_file4=format(Times_7,'040b')
                                                Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file4
                                                
                 

                                            
                                            Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file_2
 
                                           
                                             
                                            
                                           
                                            
                                            
                                            
                                                
                                            
                                            #print(B)
                                               
                                           
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file3=format(Times_10,'024b')                                            
                                            
                                                                                   
                                            
                                                                                         
                                                
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file4
    
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=""
                                      
                                            
                                            
                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
    
                                            add_bits=""
    
                                            Times_6=""
    
                                            #Extract
    
                                            INFO10=""
                                            Translate_info_Decimal=""
                                          
                                           
                                            Times_6=""
                                        
                                            Number_of_the_file=0
                                          
    
                                            C=1
                                         
                                            if C==1:
                                                if   Circle_times2==0:
    
                                                         
    
                                                        
    
                                                        
                                                        
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
                                                        INFO10=Equal_info_between_of_the_cirlce_of_the_file2
                                                        Deep5 = int(INFO10, 2)
                                                       
                                                      
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file_2
                                                        
                                                      
                                                        
                                                        Times_6=Equal_info_between_of_the_cirlce_of_the_file3
                                                        Add_N=Add_N
                                                        
                                                        T = int(Times_6, 2)
                                                        Add= int(Add_N, 2)
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        #print("Deep: ")
                                                        #print(Deep7-25)
                                                        Times_half_Real=0
                                                if   Circle_times2>0:
                                                        Translate_info_Decimal_2=0
                                                        
                                                
                                                        
            
                                                if C==1 and Times_12!=0:
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file4
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                       
                                                        
                                                       
                                                        if len (Equal_info_between_of_the_cirlce_of_the_file4)!=0:
                        
                                                                                                    
                                                            Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file4, 2)
                                                                                                     

                                                        else:
                                                            Number_of_the_file=0
                                          
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                
                                                
                                                                                         
                                                        Number_of_the_file=((((Number_of_the_file*add_ones_together)+Times_11)//3)*Times_10)//Divided_corrdiates
                                                        if Number_of_the_file>=(2**536870912)-1:
                                                            Number_of_the_file=(2**536870912)-1
                                                       
                                                        
                                                        
                                                        
                                                        Times_half_Real+=1
                                                        
                                                        
                                                        
                                                
                                        
                                                
                                                                                  
                                                
                                                
                                                        
                                               

                                              
                                            #####################################################################################################################################################
                                           
                                            
                                            
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                             
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                            #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                           
    
                                            if i==1:
                                                Make_togher=""
                                                Make_togher=Times_6
                                                
                                                add_bits=""
                                                if C==1 and Times_12!=0:
                                                        Circle_times2=Circle_times2+1
    
                                                lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(Circle_times2)
                                                
                                                
                                                if  Circle_times2==Times_12:
                                                        Circle_times2_1=Circle_times2
                                                        Circle_times2=0
                                                        
                                                        
                                                        if int(INFO,2)==Number_of_the_file:  


                                                               if C==1:

                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                                                       lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)



                                                                       lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                       add_bits=""
                                                                       count_bits=8-lenf%8
                                                                       z=0
                                                                       if count_bits!=0:
                                                                               if count_bits!=8:
                                                                                   while z<count_bits:
                                                                                       add_bits="0"+add_bits
                                                                                       z=z+1


                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                                #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                if int(INFO,2)==Number_of_the_file and Circle_times2_1==Times_12:
                                                       lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                       add_bits=""
                                                       count_bits=8-lenf%8
                                                       z=0
                                                       if count_bits!=0:
                                                               if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1
                                                       Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17        









                                                       if INFO[:8]!="00000000":
                                                           Size=8
                                                           lenf2=1
                                                       else:
                                                           Size=40
                                                       C="0"+str(Size)+"b"
                                                       

                                                       Time_Real3=format(lenf2,C)
                                                       T1=len(Time_Real3)
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                       long3=Time_Real1+Time_Real3






                                                       
                                                       
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)

                                                       Add_N=Time_Real1+Time_Real3
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                       Time_Real2=Time_Real1+Time_Real3
                                                       
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                                       
                                                       Equal_info_between_of_the_cirlce_of_the_file2=Time_Real1+Time_Real3
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                       Equal_info_between_of_the_cirlce_of_the_file3=Time_Real1+Time_Real3
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                       Divided_corrdiates1=Time_Real1+Time_Real3
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
                                                       C="0"+str(40)+"b"
                                                       Time_Real1=format(T1,C)
                                                       N10=Time_Real1+Time_Real3                                                       





                                                       if int(INFO,2)==Number_of_the_file and Circle_times2_1==Times_12:


                                                               Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file2+Equal_info_between_of_the_cirlce_of_the_file3+Add_N+long3+Time_Real2+Divided_corrdiates1+N10
                                                               Extract1=1
                                                      

                                                       if int(INFO,2)==0:
                                                               Equal_info_between_of_the_cirlce_of_the_file_17=Compress_zeros
                                                               lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                               add_bits=""
                                                               count_bits=8-lenf%8
                                                               z=0
                                                               if count_bits!=0:
                                                                   if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1

                                                               Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                               Extract1=1
                                                    
                                                 
                                    if Extract1==1:                
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                            
                                  
                                                            
                                            with open(nameas, "wb") as f2:
                                                import paq
                                                width_bits3=paq.compress(width_bits3)
                                                f2.write(width_bits3)
                                                    
                                            
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            
                                            return xs;
                                    		
                                if i==2:
                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                    lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if  len(INFO)<=(5*8):
                                                 
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17
                                                    #print(Number_zeroes)
                                                    Number_zeroes=int(INFO,2)
                                                    Number_zeroes-=1
                                                    Equal_info_between_of_the_cirlce_of_the_file_18=""
                                                   
                                                    Number_zeroes1=0
                                                    while Number_zeroes!=Number_zeroes1:
                                                            Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_18+"0"
                                                            Number_zeroes1+=1
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18

                                                    lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                    add_bits=""
                                                    count_bits=8-lenf%8
                                                    z=0
                                                    if count_bits!=0:
                                                            if count_bits!=8:
                                                                    while z<count_bits:
                                                                            add_bits="0"+add_bits
                                                                            z=z+1

                                                    Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                                    L=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)

                                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                                    width_bits=(width_bits//8)*2

                                                    width_bits=str(width_bits)
                                                    width_bits="%0"+width_bits+"x"
                                                    width_bits3=binascii.unhexlify(width_bits % n)
                                                    width_bits2=len(width_bits3)
                                                    add_bitszzza=""
                                                    add_bitszs=""
                                                    Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                                    with open(nameas, "wb") as f2:
                                                            f2.write(width_bits3)
                                                    x2 = time()
                                                    x3=x2-x
                                                    xs=float(x3)
                                                    xs=str(xs)
                                                    
                                                    return xs;
                                   

                                    
                                   
                   
                               
                                            
                                            
                                              

                                            
                                           
                                            
                           
                       
                                                            
                                              
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                   
                                    
                                   
                                    
                                    
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    INFO10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                  
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    
                                 

                                    
                                 
                                    if C==1:
                                        
                                        if   Circle_times2==0:
                                            Equal_info_between_of_the_cirlce_of_the_file=INFO
                                           
                                        if   Circle_times2==0:
                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                               

                                                #08122#17#18
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                                                                
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                Deep5=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                            


                                                #08014 #15
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                             
                                                
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                                                                     
                                                T_Real=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                Add=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]

                                                #18020d47 #11
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                     
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                long=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                
                                                T14=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]


                                                #0010ffff #6
                                                
                                                
                                                Reality=T14
                                                #000801 #3
                                                
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                                                                   
                                                                                                                                                                                                
                                                Divided_corrdiates=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                #print(Divided_corrdiates)
                                                

                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:40],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[40:]
                                                
                                                if len(Equal_info_between_of_the_cirlce_of_the_file)==0:
                                                    print("Wrong file!")
                                                    raise SystemExit                                                    
                                                N10=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                #print(N10)
                                                

                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Reality2=0
                                                if T14==0:
                                                    T14=1
                                                
                                                if Divided_corrdiates==0:
                                                    Divided_corrdiates=1
                                                
                                                
                                                
                                            

                                                #print(T14)
                                        
                                                #print(Reality)
                                              


                                                #print(Reality)
                                        
                                                
                                        if   Circle_times2>0:
                                        	Translate_info_Decimal_2=0
                                       
                                      
                                        	
                                        	
                                        
                                        	
    
                                        if C==1 and T14!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                


                                        if len (Equal_info_between_of_the_cirlce_of_the_file)!=0:
                        
                                                                                                    
                                                    Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file,2)
                                                    #print(Number_of_the_file)

                                        else:
                                                     Number_of_the_file=N10
                                                 
                                                     
                                        if Reality2<Reality:
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                        Reality2+=1
                                                        Number_of_the_file=((((Number_of_the_file*add_ones_together)+Add)//3)*T_Real)//Divided_corrdiates
                                                        if Number_of_the_file>=(2**536870912)-1:
                                                            Number_of_the_file=(2**536870912)-1
                                                 
                                                        #print(Number_of_the_file)
                                             
                                    #####################################################################################################################################################
                                   
                                    
                                    
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:

                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T14!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                          
                                        
                                                
                                        if  Circle_times2==T14:
                                        	   
                                            if C==1 and T14==0:
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17


                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            	
                                            
                                     
                                            if C==1 and T14!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            	        
                                            	#print(lenf14)

                                            		
                                            	
                                            	
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            #############binary to data
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            ####
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
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
