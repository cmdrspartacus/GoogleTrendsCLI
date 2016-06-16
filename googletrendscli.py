import argparse
import requests
import bs4
import webbrowser

# CLI argments for keywords and country
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--geo', help='Enter the option search country in two letter country code. (Defaults to SG)',
                    required=False)
parser.add_argument('first_keyword', help='Enter first keyword.')
parser.add_argument('second_keyword', help='Enter second keyword.')
parser.add_argument('-r', '--results', help='Enter C for chart or J for JSON.', required=False)
args = parser.parse_args()

# Function for defining search location. (defaults to SG)

country = args.geo


def geo_target():
    if not country:
        return 'SG'
    else:
        return str(country)


geo = 'geo={}'.format(geo_target())

base_url = 'http://www.google.com/trends/fetchComponent?hl=en-US'

# keywords
q = [args.first_keyword, args.second_keyword]
keyword_url = 'q={},{}'.format(q[0], q[1])

# Argparse option to return chart or json
choice = args.results


def define_graph_or_json():
    if choice == 'C':
        figure = '5'
    elif choice == 'J':
        figure = '3'
    else:
        figure = '5'
    return figure


result = 'export={}'.format(define_graph_or_json())

width = 'w=500'
height = 'h=300'

# Create target url
target_url = "{}&{}&cid=TIMESERIES_GRAPH_0&{}&{}&{}&{}".format(base_url, keyword_url, result, width, height, geo)

# Retrieving Google Trends chart

r = requests.get(target_url)
soup = bs4.BeautifulSoup(r.content, 'lxml')
meat = soup.select('time-chart')

webbrowser.open_new(target_url)
