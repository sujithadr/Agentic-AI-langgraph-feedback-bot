def extract_content(state):
    """
    Extracts the customer remark from the payload.
    """
    return {"text": state["payload"][0]["customer_remark"]}


def run_compliment_code(state):
    """
    Returns a friendly response for compliments.
    """
    return {"answer": {"temp_answer": "Thanks for the compliment."}}


def run_question_code(state):
    """
    Returns a positive acknowledgment for questions.
    """
    return {"answer": {"temp_answer": "Wow nice question."}}


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
