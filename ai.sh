#!/bin/bash
# Set your OpenAI API key here
API_KEY="your api key"
# Read the prompt from the command line argument
PROMPT="$*"
# Escape any backticks and double quotes in the prompt argument
PROMPT=${PROMPT//\\/\\\\}
PROMPT=${PROMPT//\"/\\\"}
PROMPT=${PROMPT//\\/\\}
# Get the number of columns in the terminal window
WIDTH=$(tput cols)
# Make the API call and extract the response content using jq, then wrap the output to the terminal window width using fold
RESPONSE=$(curl -s -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $API_KEY" \
-d "{\"model\": \"gpt-3.5-turbo\", \"messages\": [{\"role\": \"user\", \"content\": \"$PROMPT\"}]}" \
https://api.openai.com/v1/chat/completions \
| jq -r '.choices[].message.content | gsub("^[[:space:]]+|[[:space:]]+$";"")' \
| fold -s -w $WIDTH)
# Output the response content
echo "$RESPONSE"
