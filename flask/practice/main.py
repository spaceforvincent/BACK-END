import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = " "
audioFilePath = r"sound/STT.wav"
languageCode = "korean"
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))

data = json.loads(response.data.decode("utf-8", errors='ignore'))    
rec_text= data['return_object']['recognized']
print(rec_text)
  