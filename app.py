import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Helper function for querying OpenAI's model using the new client method
def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Specify the model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,  # Adjust token limit as needed
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

# Function for legal document assistant
def legal_assistant():
    st.title("AI-Powered Legal Document Assistant")
    st.write("Choose an option:")
    
    choice = st.radio("Options:", ["Ask a legal question", "Request a document template", "Generate legal contract draft"])

    if choice == "Ask a legal question":
        question = st.text_input("Enter your legal question:")
        if st.button("Submit"):
            prompt = f"As a legal assistant, please answer this question: {question}"
            answer = get_openai_response(prompt)
            st.write("Legal Advice:", answer)

    elif choice == "Request a document template":
        doc_type = st.text_input("Enter the document type (e.g., Contract, Agreement):")
        if st.button("Get Template"):
            prompt = f"Provide a {doc_type} template with standard legal clauses and sections."
            template = get_openai_response(prompt)
            st.write("Document Template:", template)

    elif choice == "Generate legal contract draft":
        contract_details = st.text_area("Enter details for the contract (e.g., parties involved, key terms):")
        if st.button("Generate Draft"):
            prompt = f"Draft a legal contract with the following details: {contract_details}"
            contract_draft = get_openai_response(prompt)
            st.write("Contract Draft:", contract_draft)

# Run the legal assistant function
if __name__ == "__main__":
    legal_assistant()
