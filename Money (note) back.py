#Money Note back 

input=503


if input>=100:
  note100taka=int(input/100)
  print(f"{note100taka} =  100 taka note")
  inputRemain=input%100

if inputRemain>=50:
  note50taka=int(inputRemain/50)
  print(f"{note50taka} =  50 taka note")
  inputRemain=inputRemain%50

if inputRemain>=20:
  note20taka=int(inputRemain/20)
  print(f"{note20taka} =  20 taka note")
  inputRemain=inputRemain%20

if inputRemain>=10:
  note10taka=int(inputRemain/10)
  print(f"{note10taka} =  10 taka note")
  inputRemain=inputRemain%10

if inputRemain>=2:
  note2taka=int(inputRemain/2)
  print(f"{note2taka} =  2 taka note")
  inputRemain=inputRemain%2

if inputRemain>=1:
  note1taka=inputRemain
  print(f"{note1taka} =  1 taka note" )
  
