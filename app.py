import os
import streamlit as st
from openai import OpenAI, OpenAIError

# Set your OpenAI API key directly (ensure this is securely managed in production)


# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["general"]["OPENAI_API_KEY"])

# Helper function for querying OpenAI's model
def get_openai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use GPT-4o
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,  # Adjust token limit as needed
            temperature=0.5
        )
        return response.choices[0].message.content  # Access method for the response
    except OpenAIError as e:
        st.error(f"Error calling OpenAI API: {e}")
        return "Sorry, there was an error processing your request."

# Function for legal document assistant
def legal_assistant():
    st.title("AI-Powered Legal Document Assistant")
    st.write("Choose an option:")
    choice = st.selectbox("Select an option:", ["Ask a legal question", "Request a document template", "Generate legal contract draft"])

    if choice == "Ask a legal question":
        question = st.text_input("Enter your legal question:")
        if st.button("Submit Question"):
            if question:
                prompt = f"As a legal assistant, please answer this question: {question}"
                answer = get_openai_response(prompt)
                st.write("### Legal Advice:")
                st.write(answer)
            else:
                st.warning("Please enter a question.")

    elif choice == "Request a document template":
        doc_type = st.text_input("Enter the document type (e.g., Contract, Agreement, Pleading, Legal Opinion):")
        if st.button("Get Template"):
            if doc_type:
                prompt = f"Provide a {doc_type} template with standard legal clauses and sections."
                template = get_openai_response(prompt)
                st.write("### Document Template:")
                st.write(template)
            else:
                st.warning("Please enter a document type.")

    elif choice == "Generate legal contract draft":
        contract_details = st.text_input("Enter details for the contract (e.g., parties involved, key terms):")
        if st.button("Generate Draft"):
            if contract_details:
                prompt = f"Draft a legal contract with the following details: {contract_details}"
                contract_draft = get_openai_response(prompt)
                st.write("### Contract Draft:")
                st.write(contract_draft)
            else:
                st.warning("Please enter contract details.")

# Run the legal assistant function
if __name__ == "__main__":
    legal_assistant()
