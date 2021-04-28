# import the necessary packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
def search(index,query,result_path):
# initialize the image descriptor
    cd = ColorDescriptor((8, 12, 3))
    # load the query image and describe it
    query1 = cv2.imread(query)
    features = cd.describe(query1)
    # perform the search
    searcher = Searcher(index)
    results = searcher.search(features)
    # display the query
    #cv2.imshow("Query", query1)
    search_output = []
    for (score,resultID) in results:
        #print(result_path+"/"+resultID)
        full_path=result_path+"/"+resultID
        #result=cv2.imread(result_path+"/"+resultID)
        #cv2.imshow("Result", result)
        #cv2.waitKey(0)
        search_output.append(resultID)
    #print(search_output)
    return search_output
