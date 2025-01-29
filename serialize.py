from bson import ObjectId

def serialize_doc(doc):
    """Converts ObjectId to string to avoid serialization errors"""
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc
