#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
]
for row in picture:
    for item in row:
        if item == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    print("My 2024 Christmas Tree")
