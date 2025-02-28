from langchain.tools import BaseTool
from utilities.validators import validate_platform

class PlatformSelectorTool(BaseTool):
    name = "platform_selector"
    description = "Select social media platform"
    
    def _run(self, platform: str):
        validate_platform(platform)
        return {"platform": platform}