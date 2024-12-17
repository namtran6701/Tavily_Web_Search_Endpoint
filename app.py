from flask import Flask, request, jsonify
from tavily_tool import TavilySearch
import logging

# set up logging
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/search', methods = ['POST'])
def search():
    """ 
    Endpoint for multiple web search

    Expected Json body:
    {
        "query": "search query",
        "mode": "news" or "general", default is "news"
        "max_results": optional int, default = 2
        "include_domains": optional list of strings, default = None
    }
    """
    try:
        data = request.get_json()
        
        # validate reuqired fields:
        if not data or 'query' not in data:
            logger.error("Missing required field: 'query'")
            return jsonify({
                'error': "Missing required field: 'query'"
            }), 400
        
        # get optional parameters 
        mode = data.get('mode', 'news')
        max_results = data.get('max_results', 2)
        if not isinstance(max_results, int) or max_results < 1:
            logger.error(f"Invalid max_results: {max_results}")
            return jsonify({
                'error': "Invalid max_results. Please provide a positive integer."
            }), 400
        include_domains = data.get('include_domains', None)
        if include_domains is not None and not isinstance(include_domains, list):
            logger.error(f"Invalid include_domains: {include_domains}")
            return jsonify({
                'error': "Invalid include_domains. Please provide a list of strings."
            }), 400

        # initialize searcher
        logger.info("Initializing TavilySearch")
        try:
            searcher = TavilySearch(max_results=max_results, 
                                    include_domains=include_domains)
        except ValueError as e:
            logger.error(f"Error initializing TavilySearch: {e}")
            return jsonify({
                'error': f"Invalid configuration: {str(e)}"
            }), 400

        # perform search based on mode. If mode is not provided, default to news
        if mode.lower() == 'news':
            logger.info("Performing news search")
            results = searcher.search_news(data['query'])
        elif mode.lower() == 'general':
            logger.info("Performing general search")
            results = searcher.search_general(data['query'])
        else:
            logger.error("Invalid mode. Please use 'news' or 'general'.")
            return jsonify({
                'error': "Invalid mode. Please use 'news' or 'general'."
            }), 400
    
        # format results
        logger.info("Formatting search results")
        formatted_results = searcher.format_result(results)
        
        logger.info("Search completed successfully")
        return jsonify(formatted_results)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({
            'error': "An error occurred while processing the request."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
