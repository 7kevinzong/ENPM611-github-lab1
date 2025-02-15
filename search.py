import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    for item in json_data:
        user = item.get("User", "Unknown user")
        rating = item.get(search_string, "N/A")
        results.append(f"{user}: {rating}")

    return results