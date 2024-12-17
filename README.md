# Web Search Endpoint

A Flask-based REST API that provides web search functionality using the Tavily API. This service allows you to search for both news and general information with customizable search parameters.

## Features

- News search endpoint
- General information search endpoint
- Customizable search results count
- Domain filtering capabilities
- Docker support
- Comprehensive error handling and logging

## Prerequisites

- Python 3.11+
- Docker (optional)
- Tavily API key

## Installation

### Local Setup

1. Clone the repository: 
```bash
git clone https://github.com/your-username/web-search-endpoint.git
cd web-search-endpoint
```

2. Install dependencies:

```bash
poetry install
```

3. Set up environment variables:

```bash
cp .env.example .env
```

4. Run the application:

```bash
poetry run python app.py
```

5. Access the API at `http://localhost:5000/search` (or the port specified in the Docker Compose file).

### Docker Setup

1. Build the Docker image:

```bash
docker-compose up --build
```

### Usage


The API exposes a single endpoint at `/search` that accepts POST requests.

### API Endpoint

**POST /search**

Request body:

```json
{
    "query": "your search query",
    "model": "news" or "general",
    "max_results": 10,
    "include_domains": ["example.com", "example.org"]
}
```

Exampple response: 

```json
{
    "query": "US presidential election",
    "results": [
        {
            "content": "US non-voters: tell us why you abstained in the 2024 US presidential election | US elections 2024 | The Guardian The Guardian view We’re interested to hear from people who would have been eligible to vote in the 2024 US presidential election but did not. Tell us why you did not vote in the 2024 US presidential election, and how you voted in previous elections. If you were legally able to vote in the 2024 US presidential election but did not, tell us why If you are happy to, share how you voted in the previous two elections in 2020 and 2016, or whether you abstained then also Optional For more information, please see our guidance on contacting us via WhatsApp. For true anonymity please use our SecureDrop service instead.",
            "date": "Mon, 18 Nov 2024 15:43:00 GMT",
            "title": "US non-voters: tell us why you abstained in the 2024 US presidential election - The Guardian US",
            "url": "https://www.theguardian.com/us-news/2024/nov/18/election-trump-harris-non-voters-callout"
        },
        {
            "content": "Przemysław Radomski - Sunshine Profits | November 27, 2024 | 10:04 am Markets USA Gold  Before summarizing, we would like to discuss one specific thing: gold’s performance around Thanksgiving – during the US presidential election years. Gold and Thanksgiving during the presidential election years Four years earlier, in 2012, gold topped right after Thanksgiving and – just like in 2016 – it bottomed in the second half of December. Consequently, Thanksgiving during the US presidential election year had a bearish follow-up for gold in most cases. All in all, while there remain some opportunities to gain something extra on gold investments in the long run, the outlook for the precious metals market remains bearish for the following weeks.",
            "date": "Wed, 27 Nov 2024 18:07:23 GMT",
            "title": "Gold price ahead of the Thanksgiving weekend - MINING.com",
            "url": "https://www.mining.com/web/gold-price-ahead-of-the-thanksgiving-weekend/"
        }
    ]
}
```

## Project Structure

- `app.py`: Main Flask application and API endpoints
- `tavily_tool.py`: Tavily API wrapper and search functionality
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration
- `docker-compose.yml`: Docker Compose configuration

## Error Handling

The API includes comprehensive error handling for:
- Missing or invalid API keys
- Invalid search parameters
- Network errors
- Search execution failures

All errors are logged and return appropriate HTTP status codes with descriptive messages.

## Development

For local development, the application runs in debug mode by default. You can modify the Flask configuration in the docker-compose.yml file or run the application directly using:

```bash
poetry run python app.py
```


## License

MIT

## Author

Nam Tran (nam3864779@gmail.com)