from pymongo import MongoClient

# Replace with your MongoDB URI
uri = ""

try:
    # Connect to MongoDB
    client = MongoClient(uri)
    db = client["dummyDB"]  # Replace with your database name
    collection = db["customers"]  # Replace with your collection name

    # Find all users from India
    users_from_india = collection.find({"country": "India"})

    # Print all users from India
    print("Users from India:")
    for user in users_from_india:
        print(user)

    # Find and count users from each country
    pipeline = [
        {"$group": {"_id": "$country", "count": {"$sum": 1}}}
    ]
    users_by_country = list(collection.aggregate(pipeline))

    # Print count of users from each country
    print("\nNumber of users from each country:")
    for country_info in users_by_country:
        country = country_info["_id"]
        count = country_info["count"]
        print(f"{country}: {count} users")

except Exception as e:
    print("Error:", e)
finally:
    # Close the connection to MongoDB
    client.close()
