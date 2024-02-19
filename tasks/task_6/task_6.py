import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator

f"""
Task: Build a Quiz Builder with Streamlit and LangChain

In this task, you will combine your knowledge from previous tasks to create a "Quiz Builder" application using Streamlit. 
This application will allow users to upload documents, specify a topic for their quiz, choose the number of questions, 
and generate a quiz based on the content of the uploaded documents.

Components to Use:
- DocumentProcessor: Class from Task 3 for processing uploaded PDF documents.
- EmbeddingClient: Class from Task 4 for embedding queries.
- ChromaCollectionCreator: Class for creating a Chroma collection from processed documents.

Steps:
    1. Initialize the `DocumentProcessor` instance and call `ingest_documents()` to process uploaded PDF documents.

    2. Configure the `EmbeddingClient` with the necessary model, project, and location information.

    3. Create an instance of `ChromaCollectionCreator` using the `DocumentProcessor` and `EmbeddingClient` instances.

    4. Use Streamlit to create a form where users can input the topic for the quiz and select the number of questions with a slider.

    5. Upon form submission, use the `ChromaCollectionCreator` to create a Chroma collection from the processed documents.

    6. Allow the user to enter a query related to the topic for generative quiz questions. Use the Chroma collection to find relevant information based on the query.

Instructions:
    - Use Streamlit's `st.header`, `st.subheader`, `st.text_input`, and `st.slider` to create an interactive form. Capture the user's input for the quiz topic and the desired number of questions.

    - After form submission, ensure that the uploaded documents are processed, and a Chroma collection is created. Provide feedback to the user about the success or failure of these operations.

    - Finally, prompt the user to enter a query for generating quiz questions. Use the created Chroma collection to respond to the query, demonstrating how the collection can be used to retrieve information relevant to the quiz topic.

Example Code Snippets:
```python
# Initializing components
processor = DocumentProcessor()
embed_client = EmbeddingClient(**embed_config)
chroma_creator = ChromaCollectionCreator(processor, embed_client)

# Streamlit form for quiz builder
with st.form("Load Data to Chroma"):
    topic = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document")
    questions = st.slider("Number of Questions", min_value=1, max_value=10, value=5)
    submitted = st.form_submit_button("Generate a Quiz!")
    if submitted:
        # Process documents, create Chroma collection, and generate quiz

"""

st.header("Quizzify")

embed_config = {
    "model_name": "textembedding-gecko@003",
    "project": "YOUR PROJECT ID HERE",
    "location": "us-central1"
}

with st.form("Load Data to Chroma"):
    st.subheader("Quiz Builder")
    st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
    
    ####### YOUR CODE HERE #######
    
    submitted = st.form_submit_button("Generate a Quiz!")
    if submitted:
        # chroma_creator.create_chroma_collection()
            
        # Query the collection after creation
        # query = st.text_input("Enter your query")
        # if query:
            # chroma_creator.query_chroma_collection(query)
        pass