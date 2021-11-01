import re
from typing import Collection
import numpy as np

def prepare(col):
    """
    This function converts a panda series into a new one with the data converted into more "programming-friendly" strings in order to ease data analysis.
    Args:
    col(pandas series): panda data series that we want to convert.
    return:
    list of elements converted into lower case, no spaces no the sides and replaces the spaces in between the words with a low bar(_).
    """  
    return [i.lower().strip().replace(" ","_") for i in list(col)]



def strdata(col):
    """
    This function casts data to string in order to ease its analysis.
    Args:
    col(pandas series): panda data series that we want to convert.
    return:
    list of elements casted into string.
    """
    return [str(i) for i in col]


def unify(data,findthis,replaceforthis):
    """
    It finds a chosen word contained in a string and replaces it for another one, making it easier to unify categories.
    Args:
        Arg1(data):pandas data series (or column in a dataframe) previously casted into string.
        Arg2(findthis): chosen word that we want to look for in Arg1. All that contains this word will be taken into account.
        Arg3(replaceforthis): chosen word that we want to get instead of Arg2 word.
    return:
    list of words replaced with the word Arg3.
    """
    new = []
    for i  in list(data):
        if findthis in i:
            new.append(re.sub(f'(\S+|{findthis}.*)',str(replaceforthis),i))
        else:
            new.append(i)
    return new

def fatal(col):
    """
    It unifies the values in a column where you only find "y" or "n" and useless values, creating a NaN in the ones that are not "y" or "n".
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    list of values as "y", "n" or NaN.
    """
    for i in col:
        if i == "y":
            return "yes"
        elif i == "n":
            return "no"
        else:
            return np.nan

def act(col):
    """
    This function replaces the activities that have a minor importance for the string "other_activities".
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    list of converted data that is not part of a previously set relevant category into the string "other_activities".
    """
    for activity in col:
        if col == "swimming":
            return "swimming"
        elif col == "surfing":
            return "surfing"
        elif col == "fishing":
            return "fishing"
        elif col == "boat":
            return "boat"
        elif col == None:
            pass
        else:
            return "other_activities"

def getmonth(col):
    """
    It takes into account the positions where the month is expressed and converts them into the "whole" month word.
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    list of months expressed in a complete word. If no "month word" is found, it returns NaN.
    """
    for month in col:
        if col[3:6] == "jan" or "jan" in col:
            return "january"
        elif col[3:6] == "feb" or "feb" in col:
            return "february"
        elif col[3:6] == "mar" or "mar" in col:
            return "march"
        elif col[3:6] == "apr" or "apr" in col:
            return "april"
        elif col[3:6] == "may" or "may" in col:
            return "may"
        elif col[3:6] == "jun" or "jun" in col:
            return "june"
        elif col[3:6] == "jul" or "jul" in col:
            return "july"
        elif col[3:6] == "aug" or "aug" in col:
            return "august"
        elif col[3:6] == "sep" or "sep" in col:
            return "september"
        elif col[3:6] == "oct" or "oct" in col:
            return "october"
        elif col[3:6] == "nov" or "nov" in col:
            return "november"
        elif col[3:6] == "dec" or "dec" in col:
            return "december"
        else:
            return np.nan

def australia(col):
    """
    This function takes a column and converts the strings not equal to australia into Nan.
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    list of data with strings equal to "australia" or otherwise NaN.
    """
    for country in col:
        if col == "australia":
            return "australia"
        else:
            return np.nan

def season(col):
    """
    It takes the months words and converts them into the corresponding season name in the southern hemisphere. If no month words are found, it creates NaNs.
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    name of the corresponding season in the souther hemisphere. If no month words are found, it creates NaNs.
    """
    for i in str(col):
        if col == "december":
            return "summer"
        elif col == "january":
            return "summer"
        elif col == "february":
            return "summer"
        elif col == "march":
            return "autumn"
        elif col == "april":
            return "autumn"
        elif col == "may":
            return "autumn"
        elif col == "june":
            return "winter"
        elif col == "july":
            return "winter"
        elif col == "august":
            return "winter"
        elif col == "september":
            return "spring"
        elif col == "october":
            return "spring"
        elif col == "november":
            return "spring"
        else:
            return np.nan

def actnan(col):
    """
    This function replaces the activities that have a minor importance for NaNs.
    Args:
    col(pandas series): panda data series (or column in a dataframe) previously casted into string.
    return:
    list of converted data that is not part of a previously set relevant category into NaNs.
    """
    for activity in col:
        if col == "swimming":
            return "swimming"
        elif col == "surfing":
            return "surfing"
        elif col == "fishing":
            return "fishing"
        elif col == "boat":
            return "boat"
        elif col == np.nan:
            pass
        else:
            return np.nan