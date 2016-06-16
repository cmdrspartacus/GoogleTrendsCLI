# GoogleTrendsCLI
Retrieve Google Trends data in JSON or chart format with the keywords and geo-targeting you provide at command line.

Requires:
  - Requests

The module can be launched from the CL as follows:
  python googletrendscli.py firstkeyword secondkeyword --geo US

The command line operation requires two positional arguments, the first and second keywords, which are the search targets you wish to represent in your graph or JSON data. For example, 'html' and 'jquery', or 'coffee' and 'pasta'.

The --geo or -g argument is optional allowing you to enter a two-letter Google-friendly country code to define the geographical results.

Lastly, a -r or --results argument allows you to define the format of your results: 'C' for chart or 'J' for JSON.

CLI functionality is naturally limited. The intention is to include the Google Trends retriever into further projects.

Thank you.
