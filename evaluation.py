# -*- coding:utf-8 -*-
from mymodule import Server_Mydatabase
import os
import sys
import math

'''global variable'''
methods = ["", "_friend", "_follower", "_mutual", "_tweet", "_profile"]
path = "../query/evaluation/"

def nDCG(queryID):
  rec_list = []
  ideal_list = []

  SQL = Server_Mydatabase.select("SELECT ID, result from query where queryID = \'" + queryID + "\' and result <> 'None' order by ID")
  
  true = len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\' and result = '2'"))
  half = len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\' and result = '1'"))
  false = len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\' and result = '0'"))

  for user in SQL: rec_list.append(user[1])

  TRUE = [2 for i in range(true)]
  HALF = [1 for i in range(half)]
  FALSE = [0 for i in range(false)]

  ideal_list = TRUE + HALF + FALSE

  return DCG(rec_list)/DCG(ideal_list), rec_list, ideal_list


def DCG(users):
  
  ans = 0.0

  for i, user in enumerate(users):
    ans += (2**int(user)-1)/math.log2(1+(i+1))

  return ans


def AP(rec_list):

  ans = 0.0
  p_index = []
  for i, user in enumerate(rec_list):
    if int(user) == 2:
      p_index.append(i)
      ans += len(p_index) / (i+1) * 1.0

  ans = ans /len(p_index) * 1.0

  return ans, p_index


if __name__ == "__main__":
  
  while(1):
    print("input queryID")
    
    queryID = input('>>> ')
    
    if len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\'")) != 0: break
    else: print("input again!!")

  for method in methods:
    add_queryID = method + queryID
    if len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + add_queryID + "\'")) == 0: continue
    
    '''calucrate score'''
    nDCG_score, rec_list, ideal_list = nDCG(add_queryID)
    AP_score, p_index = AP(rec_list)
    
    '''output nDCG'''
    texts = [str(nDCG_score), "\nrecommendation \t ideal"]
    for rec, ideal in zip(rec_list, ideal_list): texts.append("\n" + str(rec) + '\t' + str(ideal))
    f = open(path + add_queryID + '_nDCG.txt', 'w')
    f.writelines(texts)
    f.close()

    '''output AP'''
    texts = [str(AP_score), "\n p_index"]
    for p in p_index: texts.append("\n" + str(p))
    f = open(path + add_queryID + '_AP.txt', 'w')
    f.writelines(texts)
    f.close()

    '''output_all'''
    title = "query_ID : " + str(add_queryID)
    f = open(path + add_queryID + '.txt', 'a')
    f.write(title + "\nnDCG : " + str(nDCG_score) + "\nAP : " + str(AP_score) + "\n\n")
    f.close()
    
    print(add_queryID + ".txt output !!")
