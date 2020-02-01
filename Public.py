import concurrent.futures

def pubQuery(query):
    def scrapeReddit():
        print("todo")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        reddit = executor.submit(scrapeReddit)
        #end add thread

        #add results to return string
        ret = []
        ret.append(reddit.result())


        return ret