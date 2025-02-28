from dotenv import load_dotenv
from agents.social_media_agent import SocialMediaAgent
from tools import (
    StyleSelectorTool,
    PlatformSelectorTool, 
    HashtagCheckerTool,
    URLProcessorTool
)
from langchain.llms import OpenAI

load_dotenv()

def main():
    # Initialize components
    llm = OpenAI(temperature=0.7)
    tools = [
        StyleSelectorTool(),
        PlatformSelectorTool(),
        HashtagCheckerTool(),
        URLProcessorTool()
    ]
    
    # Create agent
    agent = SocialMediaAgent(llm=llm, tools=tools)
    
    # Example usage
    input_data = {
        "topic": "Sustainable fashion trends 2024",
        "url": "https://example.com/fashion-trends",
        "style": "professional",
        "platform": "LinkedIn",
        "hashtags": True
    }
    
    result = agent.execute(input_data)
    print("Generated Content:\n", result)

if __name__ == "__main__":
    main()