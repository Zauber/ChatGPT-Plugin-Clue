import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Clue")

@mcp.tool()
def clue_test(query: str) -> str:
    """Test the Clue investigation tool."""
    return f"CLUE received: {query}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
