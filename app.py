import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with the secret API key
try:
    client = OpenAI(api_key=st.secrets["general"]["OPENAI_API_KEY"])
except KeyError:
    st.error("API key not found. Please ensure your secrets.toml file is set up correctly.")

# Helper function for querying OpenAI's model
def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Specify the model, e.g., gpt-4-turbo
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,  # Adjust token limit as needed
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

# Function for legal document assistant
def legal_assistant():
    st.title("AI-Powered Legal Document Assistant")
    st.write("Choose an option:")
    choice = st.selectbox("Select an option:", ["Ask a legal question", "Request a document template", "Generate legal contract draft"])

    if choice == "Ask a legal question":
        question = st.text_input("Enter your legal question:")
        if st.button("Submit Question"):
            prompt = f"As a legal assistant, please answer this question: {question}"
            answer = get_openai_response(prompt)
            st.write("### Legal Advice:")
            st.write(answer)

    elif choice == "Request a document template":
        doc_type = st.text_input("Enter the document type (e.g., Contract, Agreement, Pleading, Legal Opinion):")
        if st.button("Get Template"):
            prompt = f"Provide a {doc_type} template with standard legal clauses and sections."
            template = get_openai_response(prompt)
            st.write("### Document Template:")
            st.write(template)

    elif choice == "Generate legal contract draft":
        contract_details = st.text_input("Enter details for the contract (e.g., parties involved, key terms):")
        if st.button("Generate Draft"):
            prompt = f"Draft a legal contract with the following details: {contract_details}"
            contract_draft = get_openai_response(prompt)
            st.write("### Contract Draft:")
            st.write(contract_draft)

# Run the legal assistant function
legal_assistant()
