

# Marshaling parameters:

        baseurl = "https://api.datamuse.com/words"
        params_diction = {'rel_rhy':'blue'}
        response = requests.get(baseurl, params_diction)

# sends the following request:

        https://api.datamuse.com/words?rel_rhy=blue

# Packaging responses:

    status_code = response.status_code #200 is "OK"
    response_body = response.text # this is what you usually want
    response_data_struct = response.json() # if you're SURE it's json! else error
