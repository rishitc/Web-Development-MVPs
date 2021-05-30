from appwrite.client import Client
from appwrite.services.storage import Storage
import io
import PIL.Image as Image

from secret_key import SECRET_KEY
from project_data import PROJECT_ID, ENDPOINT_URL, FILE_ID


client = Client()

(client
 .set_endpoint(ENDPOINT_URL)  # Your API Endpoint
 .set_project(PROJECT_ID)  # Your project ID
 .set_key(SECRET_KEY)  # Your secret API key
 )

storage = Storage(client)

result = storage.get_file(FILE_ID)
result = storage.get_file_download(FILE_ID)

print(type(result))

if (isinstance(result, bytes)):
    image = Image.open(io.BytesIO(result))
    image.save("./image.png")
