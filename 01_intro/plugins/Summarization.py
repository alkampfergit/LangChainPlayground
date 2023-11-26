from langchain.chat_models import AzureChatOpenAI
import os
from langchain import PromptTemplate, LLMChain

class Summarization:

    def summarize_timeline(self, text):

        llm = AzureChatOpenAI(
            openai_api_version="2023-03-15-preview",
            deployment_name="Gpt42", 
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            model_name="gpt-4"
        )
    

        summarize_template_string = """I will give you a transcript of a video. The transcript contains phrases prefixed by the timestamp where the phrase starts. I want you to identify between three and ten main sections of the video. For each section you will create a brief title prefixed with the start timestamp of the section, obtained by the first phrase of the section. 

EXAMPLE ANSWER
00:00 - Title 1
00:33 - Title 2
01:23 - Title 3

[DATA]
{text}
        """
        prompt = PromptTemplate(
            template=summarize_template_string, 
            input_variables=["text"])

        chain = LLMChain(
            prompt=prompt,
            llm=llm
        )

        return chain.run(text=text)