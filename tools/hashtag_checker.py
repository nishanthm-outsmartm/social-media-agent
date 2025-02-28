from langchain.tools import BaseTool

class HashtagCheckerTool(BaseTool):
    name = "hashtag_checker"
    description = "Toggle hashtag usage"
    
    def _run(self, use_hashtags: bool):
        return {"use_hashtags": use_hashtags}