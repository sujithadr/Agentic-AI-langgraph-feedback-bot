from project.graph_builder import graph
import json
from datetime import datetime

if __name__ == "__main__":
    # Prompt user for input
    user_input = input("💬 Enter a customer remark: ").strip()

    # Compose input payload using current timestamp
    input_payload = {
        "payload": [
            {
                "time_of_comment": datetime.now().isoformat(),
                "customer_remark": user_input,
                "social_media_channel": "manual",
                "number_of_likes": 0
            }
        ]
    }

    # Invoke the graph with the input
    result = graph.invoke(input_payload)

    # Display the result in a readable format
    print("=== Final Output ===")
    print(json.dumps(result, indent=2))
