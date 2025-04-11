from langgraph.graph import StateGraph, START
from project.state import State
from project.handlers import (
    extract_content,
    run_compliment_code,
    run_question_code,
    tag_query,
    beautify
)
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI Chat model using env vars
llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1
)

# Prompt template for classification
prompt = ChatPromptTemplate.from_messages([
    ("user", "I have a customer message: \"{text}\". Is this a 'question' or a 'compliment'? Reply with only one word.")
])

# Build LLM pipeline
chain = prompt | llm | StrOutputParser()

def route_question_or_compliment(state: State):
    """
    Uses an LLM to classify the customer remark.
    Expected output: 'question' or 'compliment'
    """
    response = chain.invoke({"text": state["text"]})
    return response.strip().lower()

# Build LangGraph
graph_builder = StateGraph(State)

# Add processing nodes
graph_builder.add_node("extract_content", extract_content)
graph_builder.add_node("run_question_code", run_question_code)
graph_builder.add_node("run_compliment_code", run_compliment_code)
graph_builder.add_node("tag_query", tag_query)
graph_builder.add_node("beautify", beautify)

# Add execution flow edges
graph_builder.add_edge(START, "extract_content")
graph_builder.add_edge("extract_content", "tag_query")
graph_builder.add_edge("run_question_code", "beautify")
graph_builder.add_edge("run_compliment_code", "beautify")
graph_builder.add_edge("tag_query", "beautify")

# Add conditional routing using OpenAI
graph_builder.add_conditional_edges(
    "extract_content",
    route_question_or_compliment,
    {
        "question": "run_question_code",
        "compliment": "run_compliment_code"
    }
)

# Compile the LangGraph
graph = graph_builder.compile()
