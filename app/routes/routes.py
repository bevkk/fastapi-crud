# Import necessary modules and classes
from bson import ObjectId
from datetime import datetime
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.config.config import Collection
from app.models.models import Post

# Create an APIRouter instance
router = APIRouter()

# Define a route to create a new item (Post) in the database
@router.post("/create")
async def create_item(item: Post):
    # Convert the incoming item to a dictionary
    item_dict = item.dict()
    # Add creation and update timestamps to the item
    item_dict["created_at"] = datetime.now()
    item_dict["updated_at"] = datetime.now()
    # Insert the item into the MongoDB collection and retrieve its ObjectId
    result = Collection.insert_one(item_dict)
    item_dict["_id"] = str(result.inserted_id)
    return item_dict


# Define a route to read all items from the database
@router.get("/read")
async def read_items():
    data = []
    # Iterate through all documents in the MongoDB collection
    for doc in Collection.find({}):
        doc["_id"] = str(doc["_id"]) # Convert ObjectId to a string
        data.append(doc)
    return data

# # Define a route to delete all items from the database
# @router.delete("/delete/all")
# async def delete_all():
#     # Delete all documents in the MongoDB collection and get the count of deleted items
#     x = Collection.delete_many({})
#     return {"message": "All items deleted", "deleted_count": x.deleted_count}

# Define a route to delete a specific item by its ObjectId
@router.delete("/delete/{id}")
async def delete_item(id: str):
    # Convert the provided id string to a MongoDB ObjectId
    id = ObjectId(id)
    # Delete the document with the specified ObjectId
    res = Collection.delete_one({"_id": id})
    if res.deleted_count == 1:
        return {"message": f"{id} deleted."}
    else:
        return HTTPException(status_code=404, detail=f"{id} does not exist.")


# Define a route to update a specific item by its ObjectId
@router.put("/update/{id}")
async def update_item(id: str, update_class: Post):
    # Convert the provided id string to a MongoDB ObjectId
    id = ObjectId(id)
    # Update the document with the specified ObjectId
    result = Collection.update_one(
        {"_id": id},
        {
            "$set": {
                "title": update_class.title,
                "short_desc": update_class.short_desc,
                "description": update_class.description,
                "tags": update_class.tags,
                "updated_at": datetime.now()
            }
        }
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="{id} not found")

    return {"message": f"{id} updated."}