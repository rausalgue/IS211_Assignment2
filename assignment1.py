#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Two"""

#import needed libraries
import urllib2
import csv


def downloadData(url):
    """Downloads data from URL

    Args:
        url (string): string value for URL data fetch

    Returns:
        data: something to return
    """

    value = urllib2.Request(url)
    data = urllib2.urlopen(value)

    return data

def processData(fileContents):
    """Processes data passed in

    Args:
        fileContents (object): string value the data file

    Returns:
        data: something to return
    """

    #print fileContents.read()
    person_data = []

    readCSV = csv.reader(fileContents, delimiter=',')
    for row in readCSV:
        print(row)
        if
        person_data[row[0]] = [row[1]]
        #print(row[0])
        #print(row[0], row[1], row[2],)

    print person_data




obj = downloadData("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")

processData(obj)