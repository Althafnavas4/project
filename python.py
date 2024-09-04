shop=[[ 'Adidas Bad Bunny',1,1599,9,'blue'],['new balance', 2, 1599,10,'green']]
while True:
    print('''
1. add product  details
2.view product details          
3.ubdate product details
4.delete product details
5.searche product
6. exit
          ''')
    choice=int(input('enter the choice:'))
    if choice==1:
        name=str(input('enterthe shoes name:'))
        id=int(input('enter  shoes id:'))
        price=int(input('enter shoes price:'))
        stock=int(input('enter shoes stock:'))
        colour=str(input('enter shoes colour'))
        shop.append([name,id,price,stock,colour])




    elif choice==2:
          for i in shop:
           print(i)

    elif choice==3:
        
        id=int(input('enter id:'))
        f=0
        for i in shop:
            if id in i:
                print('''
                    1.ubdate the price
                    2.ubdate the stock
                           ''')
             
                
                choice=int(input("enter your choice:"))
             
                if choice==1:
                   price=int(input("enter price:"))
                   i[3]=price
                elif choice==2:
                    stock=int(input('enter stock:'))
                    i[4]=stock
            f=1
            if f==0:
                print('invalid choice')
    elif choice==4:
        name=str(input('enter the id:'))
        f=0
        for i in shop:
            if id in i:
                shop.remove(i)
            if f==0:
                print('invalid choice')
    elif choice==5:
        id=int(input("enter id :"))
        f=0
        for i in shop:
            if id in i:
                print(i)
            f=1
        if f==0:
               print('invalid id')

    
    elif choice==6:
        break
    else:
        print('invalid choice')            
