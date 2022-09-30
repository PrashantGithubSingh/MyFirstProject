r=int(input("Enter the rows "))
for i in range(0,r+1,1):
    for j in range(2,r+1-i+1):
        print(" ", end="")
    for z in range(i+1):
        print(" *", end="")

    print()

# range(start, end, jump) => start is included, end is exclude, jump maane kitna shor shor ke chalo
# range(8)=0,1,2,3,4,5,6,7
# range(-4)=0
# range(2,9)=2,3,4,5,6,7,8
# range(11,6)=11
# range(18,30,3)=18,21,24,27 right
# range(15,-30,-4)=15,11,7,3,0,-4,-8,-12,16,-20,-24,-28
# range(21,7,4)=21
# range(15,17,-4)=15 right
