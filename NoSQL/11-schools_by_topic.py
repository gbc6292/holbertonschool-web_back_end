#!/usr/bin/env python3
"""Python script that return a list of school having
a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> list:
    """Return a list of schools"""
    sch: list = []
    query = {"topics": topic}

    for school in mongo_collection.find(query):
        sch.append(school)

    return sch
