#!/usr/bin/env python3
"""Python script that list all documents in a collection"""
import pymongo


def list_all(mongo_collection) -> list:
    """Listing all documents"""

    all_doc: list = []

    for documents in mongo_collection.find():
        all_doc.append(documents)

    return all_doc
