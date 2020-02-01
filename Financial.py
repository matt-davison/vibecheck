import concurrent.futures

def finQuery(query):
    def scrapeBloomberg():
        #do scraping here
        scrapeData = ""
        return scrapeData
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        bloomberg = executor.submit(scrapeBloomberg)
        #end add thread

        #add results to return string
        ret = []
        ret.append(bloomberg.result())
        
    return ret
    