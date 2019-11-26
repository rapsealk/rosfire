#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time

import firebase_admin
from firebase_admin import credentials, db


def GOOGLE_APPLICATION_CREDENTIALS():
    return "lottegroundcontrol-firebase-adminsdk-1p0vi-c3913fc8fc.json"


# Fetch the service account key JSON file contents
cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS())

# Initialize the app with a service account, granting admin privileges
default_app = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://lottegroundcontrol.firebaseio.com"
})
print(default_app.name)

# Database EventListener
db.reference('root/child/value').listen(lambda event: print(event.event_type, event.path, event.data))

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference("root/child/value")
ref.set({
    "key": "value"
})
print(ref.get())


if __name__ == "__main__":
    ttime = time.time()
    for i in range(10):
        ref = db.reference("root/child")
        print(time.time() - ttime, ref.get())
        ttime = time.time()
