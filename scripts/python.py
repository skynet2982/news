#!/usr/bin/python
import subprocess
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser("site")
parser.add_argument("site", type=str)
args = parser.parse_args()



def clearUrl(url):
  redirection=subprocess.check_output(["/home/runner/work/news.toulouse.social/news.toulouse.social/clean_url.sh", url])
  return redirection.decode('utf-8')

def replace(site):
  f=open(site, 'r')
  contents = f.read()
  soup = BeautifulSoup(contents, features="html.parser")
  for a in soup.findAll('a'):
    mySite=clearUrl(a['href'])
    a['href'] = mySite
  f.close()
  return soup

def override(site, clearedHtml):
  print(str(clearedHtml))
  f=open(site, 'w')
  f.truncate(0)
  f.write(str(clearedHtml))
  f.close()


clearedHtml=replace(args.site)
override(args.site, clearedHtml)
