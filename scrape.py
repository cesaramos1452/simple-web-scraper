import argparse
import requests
import re
import sys

"""SIMPLE WEB SCRAPER BY CESAR RAMOS"""


def url(site):
    """"returns all urls from user's input site"""
    url_pattern = (r"""\bhttp[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|
    [!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\b""")
    return re.findall(url_pattern, site)


def email(site):
    """"returns all emails from user's input site"""
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)"
    return (re.findall(email_pattern, site) if
            re.findall(email_pattern, site) else None)


def phone(site):
    """"returns all phone #'s from user's input site"""
    part = r'1?\W*([2-9][0-8][0-9])\W*'
    part_2 = r'([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?'
    phone = part + part_2
    nums = re.findall(phone, site)
    if len(nums):
        for i in range(len(nums)):
            nums[i] = list(filter(None, nums[i]))
            nums[i] = ''.join(nums[i])
        return nums
    else:
        return None


def create_parser():
    """returns an instance of an argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description='Enter a website to parse')
    parser.add_argument('website', help='website to be parsed')
    return parser


def main(args):
    """"implementation of scrape.py"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if ns.website:
        site = requests.get(ns.website).text
        if url(site):
            print('URLS: ', '\n'.join(url(site)))
        else:
            print('URLS: ', None)
        if email(site):
            print('EMAILS: ', '\n'.join(email(site)))
        else:
            print('EMAILS: ', None)
        if phone(site):
            print('PHONES:', '\n', '\n'.join(set(phone(site))))
        else:
            print('PHONES: ', None)


if __name__ == '__main__':
    main(sys.argv[1:])
