import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


# def extract_session_id(session_str: str):
#     match = re.search(r"/sessions/(.*?)/contexts/", session_str)
#     if match:
#         extracted_string = match.group(1)
#         return extracted_string
#
#     return food_dict({"samosa": 2, "chole": 4})



def extract_session_id(session_str: str):

    match = re.search(r"/sessions/([^/]+)/", session_str)
    if match:
        return match.group(1)  # ✅ Only the session ID
    return ""
