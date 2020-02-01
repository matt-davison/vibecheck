import concurrent.futures

def newsQuery(query):
    def scrapeFOX():
        print("todo")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        FOX = executor.submit(scrapeFOX)
        #end add thread

        #add results to return string
        ret = []
        ret.append(FOX.result())

        return ret