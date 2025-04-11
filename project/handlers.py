def extract_content(state):
    """
    Extracts the customer remark from the payload.
    """
    return {"text": state["payload"][0]["customer_remark"]} 
    # Extracting customer remark from the payload
    # and returning it as a new state dictionary
    # with the key "text". 



def run_compliment_code(state):
    """
    Returns a friendly response for compliments.
    """
    return {"answer": {"temp_answer": "Thanks for the compliment."}} 
    # Returns a dictionary with a friendly response
    # for compliments. The response is stored under
    # the key "temp_answer" within the "answer" dictionary.


def run_question_code(state):
    """
    Returns a positive acknowledgment for questions.
    """
    return {"answer": {"temp_answer": "Wow nice question."}}
    # Returns a dictionary with a positive acknowledgment
    # for questions. The response is stored under
    # the key "temp_answer" within the "answer" dictionary.

def tag_query(state):
    """
    Classifies the text into tags based on simple keyword detection.
    """
    if "package" in state["text"].lower():
        return {"tag": "Packaging"}
    elif "price" in state["text"].lower():
        return {"tag": "Pricing"}
    else:
        return {"tag": "General"}
    # Classifies the text into tags based on simple keyword detection
    # and returns a dictionary with the tag.

def beautify(state):
    """
    Creates the final output by beautifying the intermediate response.
    """
    return {
        "answer": {
            "final_beautified_answer": [
                f"{state['answer']['temp_answer']} I will pass it to the {state['tag']} Department"
            ]
        }
    }
    # Creates the final output by beautifying the intermediate response