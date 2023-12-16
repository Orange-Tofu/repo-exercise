import socket
REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    # See if we can resolve the host name - tells us if there is
    # A DNS listening
    host = socket.gethostbyname(hostname)
    # Connect to the host - tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    # print("Connected to Internet")
    return True
    
  except Exception as e:
     print("Error in check_internet function, Caught Exception")
     print("Error:", e)
     return None
   
  # print("Not Connected to Internet") 
  return False

# is_connected(REMOTE_SERVER)