# from dotenv import load_dotenv
import streamlit as st
import os
from openai import OpenAI
from PIL import Image

# Uncomment if using environment variables from .env file
# load_dotenv()

# Initialize OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["general"]["OPENAI_API_KEY"])

# Load the logo image
logo = Image.open("logo.png")  # Replace with the path to your logo

# Streamlit App UI
def main():
    # Center-align the logo
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.image(logo, use_column_width="auto")  # Adjusts size automatically
    with col3:
        st.write(" ")

    # Title and description
    st.title("AI-Powered Legal Document Assistant")
    st.write("Welcome! This assistant can help you with legal questions, document templates, and contract drafting.")

    # Sidebar with options
    st.sidebar.title("Choose an Option")
    option = st.sidebar.selectbox("What would you like to do?", (
        "Ask a Legal Question",
        "Request a Document Template",
        "Generate Legal Contract Draft"
    ))

    # Helper function for querying OpenAI's model
    def get_openai_response(prompt):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5
        )
        return response.choices[0].message.content

    # Input fields based on option selected
    if option == "Ask a Legal Question":
        question = st.text_input("Enter your legal question here:")
        if st.button("Get Answer"):
            if question:
                prompt = f"As a legal assistant, please answer this question: {question}"
                answer = get_openai_response(prompt)
                st.subheader("Legal Advice:")
                st.write(answer)
            else:
                st.warning("Please enter a question.")

    elif option == "Request a Document Template":
        doc_type = st.text_input("Enter the document type (e.g., Contract, Agreement, Pleading, Legal Opinion):")
        if st.button("Get Template"):
            if doc_type:
                prompt = f"Provide a {doc_type} template with standard legal clauses and sections."
                template = get_openai_response(prompt)
                st.subheader("Document Template:")
                st.write(template)
            else:
                st.warning("Please enter a document type.")

    elif option == "Generate Legal Contract Draft":
        contract_details = st.text_area("Enter details for the contract (e.g., parties involved, key terms):")
        if st.button("Generate Contract"):
            if contract_details:
                prompt = f"Draft a legal contract with the following details: {contract_details}"
                contract_draft = get_openai_response(prompt)
                st.subheader("Contract Draft:")
                st.write(contract_draft)
            else:
                st.warning("Please enter contract details.")

if __name__ == "__main__":
    main()
