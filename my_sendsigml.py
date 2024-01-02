''' Sends SiGML files to the avatar via socket 8052 (standard socket for SiGML Player '''
#IMPORTANT: Please note that this script only works if the SiGML Player is running

import socket
import sys
import main
#Accepts a list of .sigml files as input and sends it to the SiGML Player using a socket
def sendsigml(filenames):
	#Initialises a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Connects to the SiGML Player which listens on port 8052
	s.connect(("localhost", 8052))

	print("Connection established")

	#Determines how many bites are sent per time step
	BUFFER_SIZE = 4096

	try:
		#Opens the specified file, reads from it and sends the content to the SiGML Player via the socket
		f = open(filenames,'rb')
		l = f.read(BUFFER_SIZE)
		print("sending file:", filenames)
		while (l):
			print('l......:',l)
			s.sendall(l)
			#print('Sent ', repr(l)) #if uncommented prints the contents of the file
			l = f.read(BUFFER_SIZE)
		f.close()
	except IOError:
		print("file: " + filenames + " not found")

	#Lets the user know the files have successfully been sent
	print("file(s) sent")

	#Closes the connection
	s.close()
	print("connection closed")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please specify at least one sign to be sent to the avatar")
    else:
        sendsigml(sys.argv[1]) #main(sys.argv[1]) 'E:/NghienCuu/HamNoSys/SignLanguageSynthesis-master/test.sigml'
