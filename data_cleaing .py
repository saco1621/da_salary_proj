#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:45:55 2022

@author: conerlious
"""
import pandas as pd
df = pd.read_csv('DataAnalyst.csv')

#salary parsing 
#cleaning salary estimate column
df = df[df['Salary Estimate'] != '-1']
salary_estimate =df ['Salary Estimate'].apply(lambda x: x.split('(')[0]) #remove "Glassdoor exe text"
remove_ks = salary_estimate.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = remove_ks.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = remove_ks.apply(lambda x: int(x.split('-')[1]))#take the second argument
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name to text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2022 - x)

# parsing of job description (python, etc)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#sql
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() in x.lower() else 0)
df.sql_yn.value_counts()

#tableau
df['tableau_yn'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df.tableau_yn.value_counts()

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

#power bi
df['power_bi_yn'] = df['Job Description'].apply(lambda x: 1 if 'power_bi' in x.lower() else 0)
df.power_bi_yn.value_counts()

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()


#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#drop the first column
df.columns
df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)





