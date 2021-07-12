def swapFileData():
  file = input("enter the file name")
  if bool(file) != 0:
      swapFile = input("enter the name of the file to swapped with")
      fileReader = open(file, 'r')
      swapFileReader = open(swapFile, 'r')
      data_a = fileReader.read()
      data_b = swapFileReader.read()
      fileReader = open(file, 'w')
      swapFileReader = open(swapFile, 'w')
      fileReader.write(data_b)
      swapFileReader.write(data_a)
      fileReader.close()
      swapFileReader.close()

swapFileData()