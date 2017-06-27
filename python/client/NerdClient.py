import requests


class NerdClient:
    nerdLocation = "http://localhost:8090/service"
    nerdQueryUrl = nerdLocation + "/disambiguate"
    nerdConceptUrl = nerdLocation + "/kb/concept"

    def processText(self, text):
        text = text.replace("\n", "").replace("\r", "")
        
        body = {
            "text": text,
            "entities": [],
            "resultLanguages": ["fr", "de", "en"],
            "onlyNER": "false",
            "sentence": "true",
            "customisation": "generic"
        }

        files = {"query": str(body)}

        r = requests.post(self.nerdQueryUrl, files=files, headers={'Accept': 'application/json'})

        statusCode = r.status_code
        nerdResponse = r.reason
        if statusCode == 200:
            nerdResponse = r.json()

        return nerdResponse, statusCode

    def fetchConcept(self, id, lang="en"):
        url = self.nerdConceptUrl + "/"+id+"?lang="+lang
        r = requests.get(url, headers={'Accept': 'application/json'})

        statusCode = r.status_code
        nerdResponse = r.reason
        if statusCode == 200:
            nerdResponse = r.json()

        return nerdResponse, statusCode


    def termDisambiguation(self, terms):
        if isinstance(terms, str):
            terms = [terms, 'history']

        body = {
            "termVector": [],
            "nbest": 0
        }

        for term in terms:
            body["termVector"].append({"term": term})

        r = requests.post(self.nerdQueryUrl, json=body, headers={'Content-Type': 'application/json; charset=UTF-8'})

        statusCode = r.status_code
        nerdResponse = r.reason
        if statusCode == 200:
            nerdResponse = r.json()

        return nerdResponse, statusCode

    def getNerdLocation(self):
        return self.nerdQueryUrl
