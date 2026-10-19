from database import db

service = db["service"]
step = db["step"]
rating = db["rating"]

'''
Organização das coleções:

service: 

_id: ObjectID
code: str
name: str
description: str
initial_step: str

step:

_id: ObjectID
code: str
service_name: str
message: str
next step: str
video_path:
website_path: 
options: list (text: str, next step: str)

rating:

_id: ObjectID
type: enum
score: int
comment: str
chatbot_flow: list


'''