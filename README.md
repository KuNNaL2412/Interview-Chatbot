# Interview-Chatbot

Problem Statement: Building a Streamlit Chatbot App for Conducting User Interviews.
 
Description: The goal of this project is to develop a Streamlit chatbot application that conducts user interviews. The chatbot will prompt users to introduce themselves and specify the job role they are seeking an interview for (e.g., HR manager, Developer, Project Manager, etc.). Based on the specified job role, the chatbot will ask 3-4 role-specific questions. The follow-up questions will be tailored based on the user's responses. After the interview questions, the chatbot will conclude the interview by providing a brief feedback on the user's performance. Additionally, the application will include an "exit chat" button to clear the conversation, allowing a new user to start a new interview.
 
Key Features:

-User Introduction: The chatbot initiates the conversation by asking the user to introduce themselves.

-Job Role Selection: Prompt the user to select the job role they're being interviewed for.

-Tailored Questions: Based on the job role selected, the chatbot asks 3-4 job-specific questions.

-Contextual Follow-ups: Utilize OpenAI api and LangChain to generate follow-up questions based on the user's responses and the chosen job role.

-Feedback Provision: Conclude the interview by providing concise feedback on the user's performance in the interview.

-Exit Chat Option: Include an exit chat button to clear the conversation, allowing a new user to start a fresh interview.
 
Techniques and Libraries: Utilize Langchain and OpenAi api to generate natural language responses and feedback based on user interactions. Implement prompt templates to structure the interview process and guide the conversation flow. Leverage Streamlit for building the user interface and handling the interview process.
