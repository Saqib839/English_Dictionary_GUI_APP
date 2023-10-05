import json, re, difflib
data = json.load(open('data.json'))
first_match = None

def search_func(query):
    try:
        return data[query]
    except:
        return 'Word not found!\nPlease check spelling\n\n\n\n\n\n\n\n\
                    Program is created by Muhammad Saqib'

def query_adjustment(user_in):
    temp1 = ''.join(re.findall('[a-zA-Z ]', user_in.lower()))
    close_match = difflib.get_close_matches(temp1, data.keys() , n=1, cutoff= 0.7)
    global first_match
    first_match = close_match[0] if len(close_match) > 0 else temp1
    output= search_func(first_match)
    return display(output)

def checker(user_in):
    global first_match
    first_match = user_in
    if user_in in data:
        output = data[user_in]
        return display(output)
    elif user_in.title() in data:
        output = data[user_in.title()]
        return display(output)
    elif user_in.upper() in data:
        output = data[user_in.upper()]
        return display(output)
    else:
        return query_adjustment(user_in)
   
def display(output):
    temp1 = re.sub(r"[\[\]{}']", '', str(output))
    return temp1

def first_match_func():
    global first_match
    return f'Showing result for : {first_match}'