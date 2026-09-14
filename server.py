from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Clue")

@mcp.tool()
def clue_test(query: str) -> str:
    """Test the Clue investigation tool."""
    return f"Clue received: {query}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
