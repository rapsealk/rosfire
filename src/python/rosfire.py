#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import rospy

import firebase_admin
from firebase_admin import credentials, db

import json


"""
Load configuration
"""
config_file = open("config.json", "r")
config = config_file.readlines()
config = json.loads(''.join(config))
config_file.close()


def GOOGLE_APPLICATION_CREDENTIALS():
    return config["credentials"]


def init_node(cert_path=None):
    cert_path = cert_path if cert_path is not None \
        else GOOGLE_APPLICATION_CREDENTIALS()
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(cert_path)
    # Initialize the app with a service account, granting admin privileges
    default_app = firebase_admin.initialize_app(cred, {
        "databaseURL": config["databaseURL"]
    })
    print(default_app.name)


# FIXME
init_node()


class Publisher:

    def __init__(self, name: str, data_class, queue_size=None):
        self._publisher = rospy.Publisher(name, data_class, queue_size=queue_size)
        self._reference = db.reference(name)

    def publish(self, message_instance):
        self._publisher.publish(message_instance)
        self._reference.set(message_instance)


class Subscriber:

    def __init__(self, name: str, data_class, callback=None):
        def _callback(data):
            callback(data)
        self._subscriber = rospy.Subscriber(name, data_class, _callback)
        self._reference = db.reference(name)
        # self._reference.listen(lambda event: print(event))

    def once(self):
        return self._reference.get()


class FirebaseSubscriber:

    def __init__(self, name: str, callback=None):
        self._reference = db.reference(name)
        self._reference.listen(callback)

    def once(self):
        return self._reference.get()


if __name__ == "__main__":
    raise RuntimeError("import rosfire")
