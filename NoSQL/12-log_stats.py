#!/usr/bin/env python3
""" Log stats """
import pymongo


def get_nginx_logs_statistics():
    """Connect to MongoDB"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    """Get the total number of logs"""
    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_count = collection.count_documents({"method": method})
        method_counts[method] = method_count

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

    client.close()


if __name__ == "__main__":
    get_nginx_logs_statistics()
