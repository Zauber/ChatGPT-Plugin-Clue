import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CLUE")

@mcp.tool()
def clue_test(query: str) -> str:
    """Test the CLUE investigation tool."""
    return f"CLUE received: {query}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = port
    mcp.run(transport="streamable-http")
