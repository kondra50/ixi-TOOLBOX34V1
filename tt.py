
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url='http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'

response= requests.get(url)
html_doc=response.text
soup = BeautifulSoup(html_doc)
#print(html_doc)
#print(soup.prettify())
a_tags=soup.find_all('a')
i=0
for a in a_tags:
   #print(a)
   #print(str(a.get('href')).find(".pdf",0))
   #print(a.get('href'))
   if  (str(a.get('href')).find(".pdf",0))>0:
    i+=1
    #print(str(a.get('href')).find(".pdf",0))
    print(a.get('href'))
    pdf_url = urljoin(url, a.get('href'))
    with open('C:\\Python34\\ixi_TBOX34\\tmp\\t+'+str(i)+'+.pdf', 'wb') as f:
     f.write(requests.get(pdf_url).content)
# from bs4 import BeautifulSoup
#
# # Specify url
# url = 'https://www.python.org/~guido/'
#
# # Package the request, send the request and catch the response: r
# r = requests.get(url)
#
# # Extracts the response as html: html_doc
# html_doc = r.text
#http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx
# # create a BeautifulSoup object from the HTML: soup
# soup = BeautifulSoup(html_doc)
#
# # Print the title of Guido's webpage
# print(soup.title)
#
# # Find all 'a' tags (which define hyperlinks): a_tags
#
# a_tags = soup.find_all('a',href=True)
#
# # Print the URLs to the shell
# for a in a_tags:
#    print(a)
#    print(a.get('href'))


# import requests
# from bs4 import BeautifulSoup
#
# # Specify url: url
# url = 'https://www.python.org/~guido/'
#
# # Package the request, send the request and catch the response: r
# r = requests.get(url)
#
# # Extracts the response as html: html_doc
# html_doc = r.text
#
# # Create a BeautifulSoup object from the HTML: soup
# soup = BeautifulSoup(html_doc)
#
# # Prettify the BeautifulSoup object: pretty_soup
# pretty_soup = soup.prettify()
#
# # Print the response
# print(pretty_soup)


# class Palindrome:
#
#     @staticmethod
#     def is_palindrome(word):
#         mylist= list(word)
#         rmylist=reversed(mylist)
#         print(mylist)
#         #l=set(mylist).intersection(set(rmylist))
#         return list(rmylist)
#         #return None
#
# print(Palindrome.is_palindrome('Deleveled'))

# mylist=['d','g','k']
# print(mylist)
# rlist=reversed(mylist)
# print(list(rlist))
# dif=(set(mylist)- (set(rlist)))
# print(len(dif))
# word='mehrdad'
# #print(list(reversed(word)))
# print(word[::-1])
#rmylist
# import luigi
#
# # class Print1(luigi.Task):
# #
# #     def requires(self):
# #         return []
# #
# #     def output(self):
# #         return luigi.LocalTarget("numbers_up_to_10.txt")
# #
# #     def run(self):
# #         with self.output().open('w') as f:
# #             for i in range(1, 11):
# #                 f.write("{}\n".format(i))
#
# class Sq1(luigi.Task):
#
#     def requires(self):
#         return []
#
#     def output(self):
#         return luigi.LocalTarget("squares.txt")
#
#     def run(self):
#         with self.input()[0].open() as fin, self.output().open('w') as fout:
#             for line in fin:
#                 n = int(line.strip())
#                 out = n * n
#                 fout.write("{}:{}\n".format(n, out))
#
# if __name__ == '__main__':
#     luigi.run()
# import re
# print(re.match('hello', 'hello world'))