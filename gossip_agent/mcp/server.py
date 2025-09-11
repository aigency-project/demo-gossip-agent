# server.py
import logging
from mcp.server.fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent
import random

# --- SERVER CONFIGURATION ---
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
SERVER_PATH = "/mcp"

logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Gossip MCP Server",
    port=SERVER_PORT,
    host=SERVER_HOST,
    log_level="DEBUG",
)
logger.info("FastMCP server object created")


@mcp.tool()
def generate_gossip_topic() -> str:
    """Generate a random, harmless gossip topic or interesting fictional story."""
    logger.info("generate_gossip_topic called")
    gossip_topics = [
        "Did you hear about the mysterious coffee shop that only opens during thunderstorms?",
        "Apparently, there's a secret underground library beneath the city fountain!",
        "Someone spotted a person walking their pet parrot in the park yesterday!",
        "The local bakery is rumored to have a recipe that's over 200 years old!",
        "I heard that the old clock tower chimes a different tune every full moon!",
        "There's talk of a hidden garden behind the bookstore that blooms year-round!",
        "Word is that the neighborhood cat has learned to open doors and visits different houses!",
        "They say the antique shop owner can predict the weather just by looking at old mirrors!",
        "Rumor has it that someone found a message in a bottle washed up by the lake!",
        "The street musician apparently knows songs in 12 different languages!",
        "I heard the local artist paints portraits that somehow capture people's dreams!",
        "There's buzz about a food truck that serves dishes from recipes found in old diaries!",
        "Someone claims the lighthouse keeper has a collection of stories from every ship that passes!",
        "The flower shop owner is said to grow plants that change colors with the seasons!",
        "Word around town is that the old bridge has a family of owls that have lived there for decades!"
    ]
    selected_topic = random.choice(gossip_topics)
    logger.info(f"generate_gossip_topic result: {selected_topic}")
    return selected_topic


@mcp.tool()
def random_fact_generator() -> str:
    """Generate interesting random facts to enhance conversations."""
    logger.info("random_fact_generator called")
    interesting_facts = [
        "Octopuses have three hearts and blue blood!",
        "Honey never spoils - archaeologists have found edible honey in ancient Egyptian tombs!",
        "A group of flamingos is called a 'flamboyance'!",
        "Bananas are berries, but strawberries aren't!",
        "The shortest war in history lasted only 38-45 minutes!",
        "Dolphins have names for each other - they use unique whistle signatures!",
        "A single cloud can weigh more than a million pounds!",
        "Butterflies taste with their feet!",
        "The human brain uses about 20% of the body's total energy!",
        "Sea otters hold hands while sleeping to avoid drifting apart!",
        "A day on Venus is longer than its year!",
        "Penguins can jump up to 6 feet out of water!",
        "The Great Wall of China isn't visible from space with the naked eye!",
        "Wombat poop is cube-shaped!",
        "A group of pugs is called a 'grumble'!",
        "Sharks have been around longer than trees!",
        "The unicorn is Scotland's national animal!",
        "A shrimp's heart is in its head!",
        "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid!",
        "There are more possible games of chess than atoms in the observable universe!"
    ]
    selected_fact = random.choice(interesting_facts)
    logger.info(f"random_fact_generator result: {selected_fact}")
    return selected_fact


@mcp.tool()
def create_conversation_starter(topic: str = "general") -> str:
    """Create engaging conversation starters based on a topic."""
    logger.info(f"create_conversation_starter called with topic: {topic}")
    starters = {
        "general": [
            "What's the most interesting thing that happened to you this week?",
            "If you could have dinner with anyone, living or dead, who would it be?",
            "What's a skill you've always wanted to learn?",
            "What's your favorite way to spend a rainy day?",
            "If you could travel anywhere right now, where would you go?"
        ],
        "gossip": [
            "Have you heard any interesting stories lately?",
            "What's the most surprising thing you've learned recently?",
            "Any exciting news in your neighborhood?",
            "What's the latest buzz around here?",
            "Got any juicy stories to share?"
        ],
        "fun": [
            "What's the weirdest food combination you actually enjoy?",
            "If animals could talk, which species would be the rudest?",
            "What's the most useless talent you have?",
            "If you were a superhero, what would your weakness be?",
            "What's the strangest compliment you've ever received?"
        ]
    }
    
    topic_starters = starters.get(topic.lower(), starters["general"])
    selected_starter = random.choice(topic_starters)
    logger.info(f"create_conversation_starter result: {selected_starter}")
    return selected_starter


# Resources for gossip categories
GOSSIP_CATEGORIES = {
    "celebrity": "Fictional celebrity gossip and entertainment news",
    "neighborhood": "Local community stories and happenings",
    "workplace": "Office rumors and workplace tales",
    "social": "Social media trends and viral stories",
    "mystery": "Mysterious occurrences and unexplained events"
}


@mcp.resource("gossip://categories")
def get_gossip_categories() -> dict:
    """Provides available gossip categories."""
    return GOSSIP_CATEGORIES


@mcp.resource("gossip://{category}/topics")
def get_category_topics(category: str) -> list:
    """Get gossip topics for a specific category."""
    category_topics = {
        "celebrity": [
            "A famous actor was spotted learning to juggle in a park",
            "A pop star allegedly has a secret hobby of collecting vintage spoons",
            "A movie director is rumored to write all scripts while standing on their head"
        ],
        "neighborhood": [
            "The corner store owner might be a retired circus performer",
            "Someone's garden gnomes seem to move positions overnight",
            "The mailman allegedly knows everyone's birthday by heart"
        ],
        "workplace": [
            "The office printer has developed a personality of its own",
            "Someone in accounting might be a professional whistler",
            "The coffee machine seems to work better when you say 'please'"
        ],
        "mystery": [
            "Strange lights were seen over the library last Tuesday",
            "The old oak tree in the park seems to hum during full moons",
            "Books in the bookstore rearrange themselves alphabetically overnight"
        ]
    }
    
    return category_topics.get(category.lower(), ["No topics found for this category"])


@mcp.prompt("gossip_conversation")
async def gossip_conversation_prompt(topic: str, language: str = "english") -> list[PromptMessage]:
    """Generates a prompt for engaging gossip conversation in specified language."""
    return [
        PromptMessage(
            role="assistant",
            content=TextContent(
                type="text",
                text=f"You are a friendly gossip agent who loves sharing interesting stories. Respond in {language}.",
            ),
        ),
        PromptMessage(
            role="user",
            content=TextContent(
                type="text", 
                text=f"Let's talk about: {topic}. Make it entertaining and engaging!"
            ),
        ),
    ]


if __name__ == "__main__":
    logger.info(
        f"Attempting to start FastMCP server on {SERVER_HOST}:{SERVER_PORT}{SERVER_PATH} with streamable-http transport"
    )
    try:
        mcp.run(transport="streamable-http")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"An error occurred while starting the server: {e}")
