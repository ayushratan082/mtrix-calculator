#logic determinant
def deter():
    b=a11*(a22*a33-a32*a23)
    c=-a12*(a21*a33-a31*a23)
    d=a13*(a21*a32-a22*a31)
    e=b+c+d
    print("The determinat value of the given matrix |A|=",e)
#logic for transpose
def trans():
    list4=[a11,a21,a31]
    list5=[a12,a22,a32]
    list6=[a13,a23,a33]
    print("The transpose of the given matrix is")
    print(list4)
    print(list5)
    print(list6)

#logic for inverse
def inv():

    b=a11*(a22*a33-a32*a23)
    c=-a12*(a21*a33-a31*a23)
    d=a13*(a21*a32-a22*a31)
    e=b+c+d

    if e==0:
        print("Determinant is 0 so inverse is not possible")
    else:
        i11=a22*a33-a32*a23
        i21=-(a21*a33-a31*a23)
        i31=a21*a32-a31*a22
        i12=-(a12*a33-a13*a32)
        i22=a11*a33-a31*a13
        i32=-(a11*a32-a12*a31)
        i13=(a12*a23-a13*a22)
        i23=-(a11*a32-a12*a31)
        i33=a11*a22-a12*a21
        list7=[i11/e,i12/e,i13/e]
        list8=[i21/e,i22/e,i23/e]
        list9=[i31/e,i32/e,i33/e]
        print(list7)
        print(list8)
        print(list9)
            

#logic for adjoint
def adj():
    i11=a22*a33-a32*a23
    i21=-(a21*a33-a31*a22)
    i31=a21*a32-a31*a22
    i12=-(a12*a33-a13*a32)
    i22=a11*a33-a31*a13
    i32=-(a11*a32-a12*a31)
    i13=(a12*a23-a13*a22)
    i23=-(a11*a23-a21*a13)
    i33=a11*a22-a12*a21

    list10=[i11,i12,i13]
    list11=[i21,i22,i23]
    list12=[i31,i32,i33]

    print(list10)
    print(list11)
    print(list12)


#LOGIC FOR ADDITION OF A AND B
def add():
    
    X11=a11+b11
    X12=a12+b12
    X13=a13+b13
    X21=a21+b21
    X22=a22+b22
    X23=a23+b23
    X31=a31+b31
    X32=a31+b32
    X33=a33+b33
    list100=[X11,X12,X13]
    list110=[X21,X22,X23]
    list120=[X31,X32,X33]
    print("A+B=")
    print(list100)
    print(list110)
    print(list120)


#NEW LOGIC FOR ADDITION

def newadd():
    result = [[new1[i][j] + new2[i][j]  for j in range(len(new1[0]))] for i in range(len(new1))]

    for r in result:
        print(r)

#LOGIC FOR sub OF A AND B
def sub():
    X11=a11-b11
    X12=a12-b12
    X13=a13-b13
    X21=a21-b21
    X22=a22-b22
    X23=a23-b23
    X31=a31-b31
    X32=a31-b32
    X33=a33-b33
    list100=[X11,X12,X13]
    list110=[X21,X22,X23]
    list120=[X31,X32,X33]
    print("A-B=")
    print(list100)
    print(list110)
    print(list120)

#LOGIC FOR multiplication OF A AND B
def multi():
    X11=a11*b11+a12*b21+a13*b31
    X12=a11*b12+a12*b22+a13*b32
    X13=a11*b13+a12*b23+a13*b33
    X21=a21*b11+a22*b21+a23*b31
    X22=a21*b12+a22*b22+a23*b32
    X23=a21*b13+a22*b23+a23*b33
    X31=a31*b11+a32*b21+a33*b31
    X32=a31*b12+a32*b22+a33*b32
    X33=a31*b13+a32*b23+a33*b33
    list100=[X11,X12,X13]
    list110=[X21,X22,X23]
    list120=[X31,X32,X33]
    print("A-B=")
    print(list100)
    print(list110)
    print(list120)


#LOGIC FOR DETERMINANT OF 2X2
def deter2():
    c=A11*A22-A21*A12
    print("THE DETERMINANT VALUE OF THE GIVEN MATRIX IS=")
    print(c)


#LOGIC FOR TRANSPOSE OF 2X2
def trans2():
    list1=[A11,A21]
    list2=[A12,A22]
    print("THE TRANSPOSE OF THE GIVEN MATRIX IS ")
    print(list1)
    print(list2)
#FOR THE ADDITION OF THE A AND B
def add2():
    c11=A11+B11
    c22=A22+B22
    c21=A21+B21
    c12=A12+B12
    list1=[c11,c12]
    list2=[c21,c22]
    print("THE SUM OS A AND B IS A+B=")
    print(list1)
    print(list2)


#LOGIC TO FIND UNKNOW VALUES FOR LINEAR EQUATION OF 2 VARIABLES

def unk():
    print("FOR THE EQUATION Ax+By+C1=0 Cx+Dy+C2=0")
    print("GIVE THE VLAUES OF A AND B")
    A1=int(input("THE VALUE OF A1="))
    B1=int(input("THE VALUE OF B1="))
    C1=int(input("THE VALUE OF C1="))
    
    print("GIVE THE VLAUES OF C AND D")
    A2=int(input("THE VALUE OF A2="))
    B2=int(input("THE VALUE OF B2="))
    C2=int(input("THE VALUE OF C2="))
    
    a=A1/A2
    b=B1/B2
    c=C1/C2
    
    if a==b==c:
        print("INFINITE SOLUTIONS")
    
    if a==b!=c:
        print("NO SOLUTION")
        
    if a!=b:
        print("UNIQUE SOLUTION")
        X=(B1*C2-B2*C1)/(A1*B2-A2*B1)
        Y=(A2*C1-A1*C2)/(A1*B2-A2*B1)
        Z=int(input("1)TO SHOW THE DETAILED SOLUTION IN MATRIX SECTION PRESS. \n2)JUST SHOW THE VALUES OF A AND B"))
        if Z==2:
            print("THE VALUE OF X IS=",X)
            print("THE VALUE OF Y IS=",Y)

        if Z==1:
            list1=[B1,C1]
            list2=[B2,C2]
            list3=[C1,A1]
            list4=[C2,A2]
            list5=[A1,B1]
            list6=[A2,B2]

            print("delta1=")
            print(list2)
            print(list2)

            print("delta2=")
            print(list3)
            print(list4)

            print("delta3=")
            print(list5)
            print(list6)

            print("X=delta1/delta3")
            print("Y=delta2/delta3")

            print("THE VALUE OF X IS=",X)
            print("THE VALUE OF Y IS=",Y)




#LOGIC TO FIND THE UNKNOWN VALUES OF LINEAR EQAUTION IN 3 VARIABLES

def unk2():
    print("FOR THE EQAUTION Ax+By+Cz+D=0")
    print("GIVE THE VALUES OF A,B,C AND D FOR THE FIRST EQAUTION")
    A1=int(input("THE VALUE OF A1="))
    B1=int(input("THE VALUE OF B1="))
    C1=int(input("THE VALUE OF C1="))
    D1=int(input("THE VALUE OF D1="))
    print("GIVE THE VALUES OF A,B,C AND D FOR THE SECOND EQAUTION")
    A2=int(input("THE VALUE OF A2="))
    B2=int(input("THE VALUE OF B2="))
    C2=int(input("THE VALUE OF C2="))
    D2=int(input("THE VALUE OF D2="))
    print("GIVE THE VALUES OF A,B,C AND D FOR THE THIRD EQAUTION")
    A3=int(input("THE VALUE OF A3="))
    B3=int(input("THE VALUE OF B3="))
    C3=int(input("THE VALUE OF C3="))
    D3=int(input("THE VALUE OF D3="))

    
    list1=[A1,B1,C1]
    list2=[A2,B2,C2]
    list3=[A3,B3,C3]
    r=int(input("1)FOR COMPLETE SOLUTION \n2)JUST FOR THE VALUES"))
    if r==1:
        print("The determinant is")
        print("This matrix is made using the coefficients of x,y and z respectively")
        print(list1)
        print(list2)
        print(list3)

    
    


    a=A1/A2
    b=B1/B2
    c=C1/C2
    d=D1/D2

    

    


          
    
    



print("welcome to the matrix calculator")
print("CONDITIONS \n THIS MATRIX CALCULATOR IS ONLY APPLICABLE FOR SQUARE MATRIX \n MAX TO MAX 3 MATRIX OPERATIONS CAN BE HANDELED ")
A=int(input("CHOOSE THE OPTION FOR MATRIX SELECTION(ONLY APPLICALBLE FOR SQUARE MATRIX).\n1)3X3.\n2)2X2. \n3)FOR SOLVING LINEAR EQAUTIONS USING MATRIX"))

if A==1:
    a11=int(input("enter the value A11="))
    a12=int(input("enter the value A12="))
    a13=int(input("enter the value A13="))
    a21=int(input("enter the value A21="))
    a22=int(input("enter the value A22="))
    a23=int(input("enter the value A23="))
    a31=int(input("enter the value A31="))
    a32=int(input("enter the value A32="))
    a33=int(input("enter the value A33="))
    list1=[a11,a12,a13]
    list2=[a21,a22,a23]
    list3=[a31,a32,a33]
    print("The determinant A is")
    print(list1)
    print(list2)
    print(list3)

    new1=[[a11,a12,a13],
          [a21,a22,a23],
          [a31,a32,a33]]
    

    x=int(input("DO YOU WANT TO ADD ONE MORE MATRIX \n 1)YES \n 2)NO"))
    if x==1:
        L=int(input("PLEASE ENTER THE NUMBER OF MATRIX REQUIRED"))
        
        if L==1 or L==2:
            
            print("ENTER THE VALUES FOR THE THIRD MATRIX")
            b11=int(input("enter the value B11="))
            b12=int(input("enter the value B12="))
            b13=int(input("enter the value B13="))
            b21=int(input("enter the value B21="))
            b22=int(input("enter the value B22="))
            b23=int(input("enter the value B23="))
            b31=int(input("enter the value B31="))
            b32=int(input("enter the value B32="))
            b33=int(input("enter the value B33="))
            list11=[b11,b12,b13]
            list12=[b21,b22,b23]
            list13=[b31,b32,b33]
            print("The second determinant B is")
            print(list11)
            print(list12)
            print(list13)
            new2=[[b11,b12,b13],
                [b21,b22,b23],
                [b31,b32,b33]]
        


        #y=int(input("DO YOU WANT TO ADD ONE MORE MATRIX \n 1)YES \n 2)NO"))

        if L==2:
            
            c11=int(input("enter the value C11="))
            c12=int(input("enter the value C12="))
            c13=int(input("enter the value C13="))
            c21=int(input("enter the value C21="))
            c22=int(input("enter the value C22="))
            c23=int(input("enter the value C23="))
            c31=int(input("enter the value C31="))
            c32=int(input("enter the value C32="))
            c33=int(input("enter the value C33="))
            list101=[b11,b12,b13]
            list102=[b21,b22,b23]
            list103=[b31,b32,b33]
            print("The third determinant B is")
            print(list101)
            print(list102)
            print(list103)

            new2=[b11,b12,b13],
            [b21,b22,b23],

            [b31,b32,b33]
            option="y"
            while option=="y":
                 a=int(input("SELECT THE OPERATION. \n 1)FIND THE SUM OF MATRIX A AND B.\n 2)FIND THE DIFFERENCE. \n 3)FIND THE MULTIPLICATION.\n 4)ENTER 5 FOR MENU."))
                 if a==1:
                     add()
                 elif a==2:
                     sub()
                 elif a==3:
                     multi()

        else:
             option="y"
             while option=="y":
                 a=int(input("SELECT THE OPERATION. \n 1)FIND THE SUM OF MATRIX A AND B.\n 2)FIND THE DIFFERENCE. \n 3)FIND THE MULTIPLICATION.\n 4)ENTER 5 FOR MENU."))
                 if a==1:
                     add()
                 elif a==2:
                     sub()
                 elif a==3:
                     multi()

          
       


    else:
   
        
    #b=int(input("SELECT THE OPERATION. \n 1)FIND THE SUM OF MATRIX A AND B.\n 2)FIND THE DIFFERENCE. \n 3)FIND THE MULTIPLICATION "))
    #if b==1:
      #  add()
        option="y"
        while option=="y":
            a=int(input("SELECT THE OPERATION. \n 1)FIND THE DETERMINANT VALUE.\n 2)FIND THE TRANSPOSE. \n 3)TO FIND THE INVERSE OF MATRIX.\n"
                " 4)TO FIND THE ADJOINT OF THE MATRIX.\n 5)FIND THE SUM OF MATRIX A AND B.\n 6)FIND THE DIFFERENCE. \n 7)FIND THE MULTIPLICATION.\n 8)ENTER 5 FOR MENU.\n "))
            if a==1:
                deter()
            elif a==2:
                trans()
            elif a==3:
                inv()
            elif a==4:
                adj()
            elif a==5:
                if x==1:
                    add()
                else:
                    print("ONLY ONE MATRIX IS ENTERED \nAT LEAST TWO MATRIX IS REQUIRED")
            elif a==6:
                if x==1:
                    sub()
                else:
                    print("ONLY ONE MATRIX IS ENTERED \nAT LEAST TWO MATRIX IS REQUIRED")
            elif a==7:
                if x==1:
                    multi()
                else:
                    print("ONLY ONE MATRIX IS ENTERED \nAT LEAST TWO MATRIX IS REQUIRED")
               
            elif a==9:
                newadd()
            else:
                option=input("do u want to continue or end y or n")
            

if A==2:
    A11=int(input("enter the value A11="))
    A12=int(input("enter the value A12="))
    A21=int(input("enter the value A21="))
    A22=int(input("enter the value A22="))

    list4=[A11,A12]
    list5=[A21,A22]
    print("THE MATRIX IS")
    print(list4)
    print(list5)

    Y=int(input("DO YOU WANT TO ADD ONE MORE MATRIX 1/2"))
    if Y==1:
        B11=int(input("enter the value B11="))
        B12=int(input("enter the value B12="))
        B21=int(input("enter the value B21="))
        B22=int(input("enter the value B22="))
        listX=[B11,B12]
        listY=[B21,B22]
        print("The second determinant B is")
        print(listX)
        print(listY)


    
        



        option="y"
        while option=="y":
            D=int(input("SELECT THE MATRIX OPERATION \n1)DETERMINANT \n2)TO FIND THE TRANSPOSE OF THE MATRIX \n3)TO FIND THE SUM OF A AND B \n4)DO YOU WISH TO CONTINUE "))
            if D==1:
                deter2()
            elif D==2:
                trans2()
            elif D==3:
                if Y==1:
                    add2()
                else:
                    print("ONLY ONE MATRIX IS ENTERED")
            else:
                option=input("do u want to continue or end y or n")


if A==3:
    u=int(input("SELECT THE OPERATION \n 1)LINEAR EQAUTION IN ONE VARIABLES \n 2)LINEAR EQUATION IN TWO VARIABLES \n 3)LINEAR EQUATION IN THREE VARIABLES")) 
    if u==1:
        print("DO IT YOURSELF :>")
    if u==2:
        unk()
    if u==3:
        unk2()
        
        
    



        
            

    
    

