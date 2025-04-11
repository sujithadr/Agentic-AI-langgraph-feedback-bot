from project.graph_builder import graph
import json

if __name__ == "__main__":
    # Example payload simulating a customer remark
    input_payload = {
        "payload": [
            {
                "time_of_comment": "2025-04-10",
                "customer_remark": "Why is the price so high?",
                "social_media_channel": "twitter",
                "number_of_likes": 56
            }
        ]
    }

    # Invoke the graph with the input
    result = graph.invoke(input_payload)

    # Display the result in a readable format
    print("=== Final Output ===")
    print(json.dumps(result, indent=2))
