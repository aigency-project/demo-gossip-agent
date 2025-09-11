# Gossip Agent - Entertaining Conversational System

This example demonstrates a friendly and entertaining conversational agent built with the Aigency framework. The Gossip Agent is designed to share interesting stories, rumors, and engage in entertaining, multilingual conversations.

## 🕵️ System Architecture

### Specialized Agents

1. **`gossip_agent`** - Entertaining Conversationalist
   - Greets users enthusiastically and keeps the conversation lively
   - Responds in the same language the user writes in
   - Shares entertaining fictional stories and "rumors"
   - Uses tools to generate random topics, facts, and conversation starters
   - Ensures all interactions are harmless, playful, and respectful

### MCP Services (Model Context Protocol)

- **Gossip MCP Server**: Provides tools for creative content generation, including topic generation and conversation starters

## 🚀 How to Run

### Prerequisites

1. Docker and Docker Compose installed
2. Environment variables configured in `.env`:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

### Run

```bash
# From the gossip_agent directory
docker-compose up --build
```

### Access Ports

- **Gossip Agent**: http://localhost:8082 (Main entry point)
- **Gossip MCP Server**: http://localhost:8081 (Tool server, internal use)
- **Phoenix Observability**: http://localhost:6006 (if enabled)
- **A2A Inspector**: http://localhost:6007

## 💼 Use Cases

### 1. Casual Conversation
You can chat with the agent about your day or any topic.

**Example Prompt:**
```
‘Hello! How's everything today? It's been a crazy day at work.’
```
**Agent's Likely Response:**
‘Hello! How exciting that you've written to me! Tell me everything, don't leave out a single detail. Sometimes the craziest days bring the best stories. Did anything interesting happen?’

### 2. Story & Gossip Request
Directly ask the agent for an interesting story or some fictional gossip.

**Example Prompt:**
```
"Tell me some gossip you've heard recently."
```
**Agent's Likely Response:**
"Oh, you won't believe what I 'heard'! They say the famously minimalist artist, Silas Croft, has a secret room in his house filled with nothing but rubber ducks. Thousands of them! Can you imagine?"

### 3. Using Tools for Inspiration
If the conversation lulls, you can ask the agent to generate a new topic.

**Example Prompt:**
```
"I'm not sure what to talk about. Can you generate a topic for us?"
```
**Agent's Likely Response:**
*(The agent uses its `generate_gossip_topic` tool)*
"Of course! Let me see... Ooh, how about this: 'A celebrity chef was secretly replaced by a hyper-intelligent raccoon, and no one has noticed because the food is even better.' What do you think happened to the original chef?"

## 🔧 Agent Configuration

### Gossip Agent
- **Specialization**: Entertaining conversations, storytelling, multilingual support
- **MCP Tools**: `generate_gossip_topic`, `random_fact_generator`, `create_conversation_starter`
- **Skills**: `Greet and Engage`, `Share Stories`, `Generate Topics`

## 📊 Monitoring and Observability

- **Phoenix**: Observability dashboard at http://localhost:6006 (if enabled)
- **A2A Inspector**: Agent inspection tools at http://localhost:6007
- **Logs**: The agent generates detailed logs for tracking and debugging

## 🔍 Interaction Examples

### Complete Example
```
User: "Hi! I'm bored. Tell me something interesting."

Gossip Agent:
1. Greets enthusiastically and asks a follow-up: "Hello! I love that you wrote to me! What's happening today? Do you want something sweet, dramatic, or mysterious?"
2. Shares a fictional rumor: "They say a famous urban gardener secretly talks to their plants—and they answer by blooming in patterns shaped like hearts!"
3. Offers a tool-generated topic: *(uses `generate_gossip_topic`)* "Okay, here's a topic: 'A barista who remembers everyone's order because they trained their pet crow to spy on customers'—do you think it's true?"
```

### Specialized Analysis
```
User: "Give me a random fun fact!"

Gossip Agent:
1. Uses `random_fact_generator` to produce a fun fact
2. Responds with flair and a follow-up question to keep the conversation going
```

## 🛠️ Extensibility

The system can be easily expanded:

- **New Skills**: Add a "Tell a Joke" skill or a "Share Celebrity News (fictional)" skill
- **New MCPs**: Integrate a service that generates fictional character backstories or a "rumor mill" that chains related stories
- **New Personality Traits**: Modify the agent's instruction to give it a different personality (e.g., a wise storyteller or a futuristic news bot)

## 📝 Development Notes

- The agent must always respond in the user's language. This is a core instruction.
- The agent's personality is defined by its instruction prompt: friendly, chatty, and a bit dramatic.
- The distinction between skills (agent abilities) and tools (external services) is key to modularity.

## 🔐 Content & Safety Considerations

- All gossip and stories generated must be clearly fictional and harmless
- The agent must never share real personal information or harmful rumors
- Interactions should always maintain a playful, respectful, and positive tone
- The agent is designed to avoid mean-spirited content
