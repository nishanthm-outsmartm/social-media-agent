from tools.style_selector import StyleSelectorTool
from tools.platform_selector import PlatformSelectorTool
from tools.hashtag_checker import HashtagCheckerTool
from tools.url_processor import URLProcessorTool  # If you have this tool
from langchain.llms import OpenAI
from agents.social_media_agent import SocialMediaAgent
from dotenv import load_dotenv  # Add this line
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