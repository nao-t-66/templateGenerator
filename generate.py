#! -*- coding:utf-8 -*-
import os
import csv
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--template', default='./template.html', help='template html file path')
parser.add_argument('--source', default='./source.csv', help='source csv file path')
parser.add_argument('--outputDir', default='./output', help='output directory')

args = parser.parse_args()

# make output dir
if not os.path.exists(args.outputDir):
  os.makedirs(args.outputDir)

# get template html as text
with open(args.template) as target:
  targetText = target.read()

# get source csv as [list]
with open(args.source, encoding='utf-8') as sourceCsv:
  reader = csv.reader(sourceCsv)
  csvList = [row for row in reader]

elementList = csvList.pop(0)
contentList = csvList

elementLength = len(elementList)
contentLength = len(contentList)

for (index, List) in enumerate(contentList):
  outputText = targetText
  outputFilePath = args.outputDir + '/' + str(index) + '.html'
  with open(outputFilePath, mode='w') as outputFile:
    # log('outputText', outputText)
    for num in range(elementLength):
      replaceTarget = '{%' + elementList[num] + '%}'
      outputText = outputText.replace(replaceTarget, List[num])
    outputFile.write(outputText)

