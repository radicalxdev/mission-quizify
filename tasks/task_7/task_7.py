import streamlit as st
from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
import os
import sys
sys.path.append(os.path.abspath('../../'))

class QuizGenerator:
    def __init__(self, topic=None, num_questions=1, vectorstore=None):
        """
        Initializes the QuizGenerator with a required topic, the number of questions for the quiz,
        and an optional vectorstore for querying related information.

        :param topic: A string representing the required topic of the quiz.
        :param num_questions: An integer representing the number of questions to generate for the quiz, up to a maximum of 10.
        :param vectorstore: An optional vectorstore instance (e.g., ChromaDB) to be used for querying information related to the quiz topic.
        """
        if not topic:
            self.topic = "General Knowledge"
        else:
            self.topic = topic

        if num_questions > 10:
            raise ValueError("Number of questions cannot exceed 10.")
        self.num_questions = num_questions

        self.vectorstore = vectorstore
        self.llm = None
        self.system_template = """
            You are a subject matter expert on the topic: {topic}
            
            Follow the instructions to create a quiz question:
            1. Generate a question based on the topic provided and context as key "question"
            2. Provide 4 multiple choice answers to the question as a list of key-value pairs "choices"
            3. Provide the correct answer for the question from the list of answers as key "answer"
            4. Provide an explanation as to why the answer is correct as key "explanation"
            
            You must respond as a JSON object with the following structure:
            {{
                "question": "<question>",
                "choices": [
                    {{"key": "A", "value": "<choice>"}},
                    {{"key": "B", "value": "<choice>"}},
                    {{"key": "C", "value": "<choice>"}},
                    {{"key": "D", "value": "<choice>"}}
                ],
                "answer": "<answer key from choices list>",
                "explanation": "<explanation as to why the answer is correct>"
            }}
            
            Context: {context}
            """
    
    def init_llm(self):
        """
        Task: Initialize the Large Language Model (LLM) for quiz question generation.

        Overview:
        This method prepares the LLM for generating quiz questions by configuring essential parameters such as the model name, temperature, and maximum output tokens. The LLM will be used later to generate quiz questions based on the provided topic and context retrieved from the vectorstore.

        Steps:
        1. Set the LLM's model name to "gemini-pro" 
        2. Configure the 'temperature' parameter to control the randomness of the output. A lower temperature results in more deterministic outputs.
        3. Specify 'max_output_tokens' to limit the length of the generated text.
        4. Initialize the LLM with the specified parameters to be ready for generating quiz questions.

        Implementation:
        - Use the VertexAI class to create an instance of the LLM with the specified configurations.
        - Assign the created LLM instance to the 'self.llm' attribute for later use in question generation.

        Note: Ensure you have appropriate access or API keys if required by the model or platform.
        """
        self.llm = VertexAI(
            ############# YOUR CODE HERE ############
        )
        
    def generate_question_with_vectorstore(self):
        """
        Task: Generate a quiz question using the topic provided and context from the vectorstore.

        Overview:
        This method leverages the vectorstore to retrieve relevant context for the quiz topic, then utilizes the LLM to generate a structured quiz question in JSON format. The process involves retrieving documents, creating a prompt, and invoking the LLM to generate a question.

        Prerequisites:
        - Ensure the LLM has been initialized using 'init_llm'.
        - A vectorstore must be provided and accessible via 'self.vectorstore'.

        Steps:
        1. Verify the LLM and vectorstore are initialized and available.
        2. Retrieve relevant documents or context for the quiz topic from the vectorstore.
        3. Format the retrieved context and the quiz topic into a structured prompt using the system template.
        4. Invoke the LLM with the formatted prompt to generate a quiz question.
        5. Return the generated question in the specified JSON structure.

        Implementation:
        - Utilize 'RunnableParallel' and 'RunnablePassthrough' to create a chain that integrates document retrieval and topic processing.
        - Format the system template with the topic and retrieved context to create a comprehensive prompt for the LLM.
        - Use the LLM to generate a quiz question based on the prompt and return the structured response.

        Note: Handle cases where the vectorstore is not provided by raising a ValueError.
        """
        ############# YOUR CODE HERE ############
        # Initialize the LLM from the 'init_llm' method if not already initialized
        # Raise an error if the vectorstore is not initialized on the class
        ############# YOUR CODE HERE ############
        
        from langchain_core.runnables import RunnablePassthrough, RunnableParallel

        ############# YOUR CODE HERE ############
        # Enable a Retriever using the as_retriever() method on the VectorStore object
        # HINT: Use the vectorstore as the retriever initialized on the class
        ############# YOUR CODE HERE ############
        
        ############# YOUR CODE HERE ############
        # Use the system template to create a PromptTemplate
        # HINT: Use the .from_template method on the PromptTemplate class and pass in the system template
        ############# YOUR CODE HERE ############
        
        # RunnableParallel allows Retriever to get relevant documents
        # RunnablePassthrough allows chain.invoke to send self.topic to LLM
        setup_and_retrieval = RunnableParallel(
            {"context": retriever, "topic": RunnablePassthrough()}
        )
        
        ############# YOUR CODE HERE ############
        # Create a chain with the Retriever, PromptTemplate, and LLM
        # HINT: chain = RETRIEVER | PROMPT | LLM 
        ############# YOUR CODE HERE ############

        # Invoke the chain with the topic as input
        response = chain.invoke(self.topic)
        return response
    
# Test the Object
if __name__ == "__main__":
    
    from tasks.task_3.task_3 import DocumentProcessor
    from tasks.task_4.task_4 import EmbeddingClient
    from tasks.task_5.task_5 import ChromaCollectionCreator
    
    
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "YOUR-PROJECT-ID-HERE",
        "location": "us-central1"
    }
    
    screen = st.empty()
    with screen.container():
        st.header("Quiz Builder")
        processor = DocumentProcessor()
        processor.ingest_documents()
    
        embed_client = EmbeddingClient(**embed_config) # Initialize from Task 4
    
        chroma_creator = ChromaCollectionCreator(processor, embed_client)

        question = None
    
        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
            topic_input = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document")
            questions = st.slider("Number of Questions", min_value=1, max_value=10, value=1)
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                chroma_creator.create_chroma_collection()
                
                st.write(topic_input)
                
                # Test the Quiz Generator
                generator = QuizGenerator(topic_input, questions, chroma_creator)
                question = generator.generate_question_with_vectorstore()

    if question:
        screen.empty()
        with st.container():
            st.header("Generated Quiz Question: ")
            st.write(question)