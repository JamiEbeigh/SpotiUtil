import os


# opens the supplied file and reads through it to find the client ID and client secret
# returns: success:bool, clientId:str, clientSecret:str
def getSpotifyCredentials(txtFile: str):
  clientId = ""
  clientSecret = ""
  
  if not os.path.isfile(txtFile):
    return False, "", ""
  
  with open(txtFile) as f:
    for l in f.readlines():
      if l.startswith("ClientId:"):
        clientId = l.lstrip("ClientId:").strip(' ')
      if l.startswith("ClientSecret:"):
        clientSecret = l.lstrip("ClientSecret:").strip(' ')
  
  if clientId != "" and clientSecret != "":
    return True, clientId, clientSecret
  return False, "", ""
