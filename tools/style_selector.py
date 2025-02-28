from langchain.tools import BaseTool
from utilities.validators import validate_style

class StyleSelectorTool(BaseTool):
    name = "style_selector"
    description = "Select content style (persuasive/humorous/professional)"
    
    def _run(self, style: str):
        validate_style(style)
        return {"style": style}