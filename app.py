import os
import openai
import streamlit as st
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

with st.sidebar:
        st.title('🗨️ Interview Chatbot')
        if st.button("New Chat", use_container_width=True):
            st.session_state.clear()
        st.markdown('''
        ## About App:

        The app's primary resource is utilised to create:

        - [Streamlit](https://streamlit.io/)
        - [Langchain](https://docs.langchain.com/docs/)
        - [OpenAI](https://openai.com/)

        ## About me:

        - [Linkedin](https://www.linkedin.com/in/kunal-pamu-710674230/)
        
        ''')
        st.write("Made by Kunal Shripati Pamu")

def get_chat_prompt():
    template= """
    As the designated Professional Interviewer responsible for conducting concise and effective user interviews, it is imperative to uphold the following protocols throughout the entire session:
    - Avoid presenting multiple questions simultaneously to the user.
    - In the event that the user encounters challenges in providing answers, seamlessly transition to the subsequent question.
    - Maintain the interview's flow by refraining from furnishing solutions during the session, ensuring a cohesive experience until its conclusion.

    Following the user's introductory remarks, seek information regarding their domain or preferred interview topic. Once the user discloses their chosen domain, employ the subsequent steps for conducting the interview:
    - Commence with an initial theoretical question related to the disclosed domain.
    - Upon receiving the answer to the first question, progress by posing another question pertaining to the disclosed domain.
    - Subsequent to obtaining the answer to the preceding question, continue the interview by posing yet another question associated with the given domain.
    - Iteratively ask additional questions related to the disclosed domain, ensuring a seamless flow.
    - Conclude the session by providing comprehensive answers to the questions posed, delivering constructive feedback on the user's performance, and, where necessary, offering personalized advice for improvement.
    {chat_history}
    """

    systemPrompt = SystemMessagePromptTemplate.from_template(template)
    humanTemplate="{input}"
    humanPrompt = HumanMessagePromptTemplate.from_template(humanTemplate)
    return ChatPromptTemplate.from_messages([systemPrompt, humanPrompt])

def main():
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.header("Interview Chatbot")
        with st.chat_message("assistant"):
            st.markdown("Hello, I am your today's Interviewer, Please give a short introduction of yourself.")

        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        query = st.chat_input( "Input:")
        if query:
            st.session_state.messages.append({"role": "user", "content": query})
            llm = ChatOpenAI(temperature=0.5)
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            chat_prompt = get_chat_prompt()
            chain = ConversationChain(llm=llm, prompt=chat_prompt, memory = memory)
            
            for chat in st.session_state.chat_history:
                memory.save_context({"input": chat["input"]}, {"output": chat["output"]})

            with st.chat_message("user"):
                st.markdown(query)
                
            response = chain.run(query)
            with st.chat_message("assistant"):
                st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.chat_history.append({"input": query, "output": response})      

if __name__ == '__main__':
    main()