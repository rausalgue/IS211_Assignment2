#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Two"""

#import needed libraries
import urllib2
from itertools import islice
from pprint import pprint
from datetime import datetime
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL for data retrieval",default=None)
parser.add_argument("--id", type=int, help="Person ID", default=None)
args = parser.parse_args()

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('assignment2')
logger.info('Begin Maniputaling Data')

def downloadData(url):
    """Downloads data from URL

    Args:
        url (string): string value for URL data fetch

    Returns:
        data: something to return
    """
    value = urllib2.Request(url)
    data = urllib2.urlopen(value)

    logger.info('Retrieve Data from URL')
    #logger.debug('data: %s', data.read())

    #print data.read()
    return data

def processData(fileContents):
    """Processes data passed in

    Args:
        fileContents (object): string value the data file

    Returns:
        full_person_database: something to return
    """

    #print fileContents.read()
    full_person_database = {}
    person_data = []

    counter = 0

    for elem in islice(fileContents, 1, None):
        counter += 1
        # all but the first element
        person_data = elem.split(",")
        id = person_data[0]

        rawDate = person_data[2].rstrip()

        #print id + ": Date: "+ date
        try:
            date = datetime.strptime(rawDate, "%m/%d/%Y")
            formatted_date = datetime.strftime(date, "%Y-%m-%d")
        except ValueError:
            try:
                date = datetime.strptime(rawDate, "%d/%m/%Y")
                formatted_date = datetime.strftime(date, "%Y-%m-%d")
            except ValueError:
                formatted_date = "0"
                logger.error('Error processing line {} '.format(counter) + 'for ID {}'.format(id))
                #print 'You have {} things.'.format(counter) + 'You have {} id.'.format(id)
                #print "error"

        full_person_database[id] = (person_data[1],formatted_date)

    logger.info('Data Processing Complete')

    return full_person_database

def displayPerson(id, personData):
    """Processes id passed in

    Args:
        id (integer): id value
        personData (dictionary): database in dictionary format

    Returns:
        full_person_database: something to return
    """

    #print 'entering display person'
    #print '*',id,'*'
    #print isinstance(id, int)
    #pprint(personData)

    ind_person_data = ()

    if isinstance( id, int ) == True:
        if id > 0:
            # Find the Data for Given USer ID
            for key in personData:
                # print key
                if int(key) == id:
                    # print "ids matched"
                    ind_person_data = personData[key]
                    # the key is in the dict

            if len(ind_person_data) > 0:
                if ind_person_data[1] != '0':
                    print 'Person #{} '.format(id) + 'is {} with a birthday of {}'.format(ind_person_data[0],
                                                                                          ind_person_data[1])
                else:
                    print 'Person #{} '.format(id) + 'is {} but has an invalid DOB'.format(ind_person_data[0])
            else:
                print 'No user found with that id'
        else:
            print "Please enter a valid User ID"
    else:
        print "Please enter a valid User ID"


#logger.debug('Person Database: %s', len(full_person_database))


#obj = downloadData("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")

#cleanData = processData(obj)

#displayPerson(10, cleanData)


def main():
    url = args.url if args.url else raw_input("Please provide the URL for data retrieval: ")

    if url != '':
        print 'Processing url for data: ' +url

        try:
            csvData = downloadData(url)
            personData = processData(csvData)
            print 'Data has been added to database' , len(personData)
            id = args.id if args.id else raw_input("Please enter User ID: ")
            print 'You have entered: ',id

            try:
                displayPerson(int(id), personData)
            except ValueError:
                main()

        except ValueError:
            print 'There was an error processing the URL'

    else:
        print 'URL is required'





if __name__ == "__main__":
    main()




#print len(cleanData)

#pprint(cleanData)

