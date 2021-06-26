#! /usr/bin/env python

import re

from bs4 import BeautifulSoup

INPUT_FILE  = 'modlist.raw.html'
OUTPUT_FILE = 'modlist.html'

def _get_mod_and_creator(anchor_text):
  search = re.search(r'(.*)\((\w+)\)$', anchor_text)

  return (search.group(1).strip(), search.group(2).strip())

def _process_list_item(item):
  anchor = item.find_all('a')[0]

  mod_name, creator_name = _get_mod_and_creator(anchor.text)

  mod_href = anchor.get('href')
  mod_anchor = '<a href={}>{}</a>'.format(mod_href, mod_name)

  creator_href = 'https://www.curseforge.com/members/{}/projects'.format(creator_name)
  creator_anchor = '<a href={}>{}</a>'.format(creator_href, creator_name)

  list_item = '<li>{}(by {})</li>'.format(mod_anchor, creator_anchor)
  return list_item

def main():
  with open(INPUT_FILE, 'r') as in_file:
    input_soup = BeautifulSoup(in_file, 'html.parser')

  list_items  = input_soup.find_all('li')
  list_items  = list(map(_process_list_item, list_items))

  list_html   = '<ul>{}</ul>'.format(''.join(list_items))
  output_soup = BeautifulSoup(list_html, 'html.parser')
  list_html   = output_soup.prettify()

  list_html   = re.sub(r'\(by\s+<a', '(by <a', list_html)
  list_html   = re.sub(r'>\s+(\w+)\s+</a>\s+\)', r'>\g<1></a>)', list_html)
  list_html   = re.sub(r'>\s+(.+)\s+</a>', r'>\g<1></a>', list_html)

  with open(OUTPUT_FILE, 'w') as out_file:
    out_file.write(list_html)

if __name__ == '__main__':
  main()
