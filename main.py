import cv2
import requests
import io
import json

img = cv2.imread('chinese.jpg')



#cutting image

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode('.jpg', img, [1,90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api, files= {'first-one.jpg': file_bytes},
                                data = {"apikey": "bc318c984b88957",
                                        "language":"chs"})
                                 

results= result.content.decode()
results = json.loads(results)
text_detected = results.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
