import pymysql

__author__ = 'Puru Pathak'

import traceback
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from dateparser import parse
from regex import sub
from datetime import datetime

#to calculate Math.ceil
def ceil(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

#to Parse Date in MySQL format i.e. YYYY-MM-DD
def parse_date(data):
    try:
        data = parse(data,settings={'PREFER_DAY_OF_MONTH': 'first'})
        data = (datetime.__format__(data,'%Y-%m-%d'))
    except:
        print('error')
    return data

# This function converts text phase into a number eg: phase 3 => 3
def parse_phase(text):
    text+="/ Phase 2"
    if '/' in text:
        text = text.split('/')[-1]
    num = sub(r'\D',"",text)
    return num

# Function to parse NCT Data into a Dictionary
def parse_nct_xml_data(data):
    CT_Brief_Title ='Null'
    CT_NCT='Null'
    FDA_Org_ID=''
    CT_Agency ='Null'
    CT_Acronym = 'Null'
    CT_Countries = 'Null'
    CT_Start_Date = 'Null'
    CT_Completion_Date = 'Null'
    CT_PCD = 'Null'
    CT_Verification_Date = 'Null'
    CT_Last_Changed_Date= 'Null'
    CT_First_Received_Date='Null'
    CT_Phase = 'Null'
    CT_Study_Type = 'Null'
    CT_Study_Design = 'Null'
    CT_Is_FDA_Regulated = 'Null'
    CT_Is_Section_801 = 'Null'
    CT_Interventions =  'Null'
    print(data)
    root = ET.parse(data).getroot()
    map ={}
    for child in root:

        if child.tag == 'id_info':
            try:
                FDA_Org_ID = child.find('org_study_id').text
                map['FDA_Org_ID']=FDA_Org_ID
            except:
                print("No FDA id")
            CT_NCT = child.find('nct_id').text
            map['CT_NCT'] = CT_NCT
        elif child.tag == 'brief_title':
            CT_Brief_Title = child.text
            map['CT_Brief_Title'] = CT_Brief_Title

        elif child.tag == 'sponsors':
            CT_Agency = child.find('lead_sponsor').find('agency').text
            map['CT_Agency'] = CT_Agency

        elif child.tag == 'start_date':
            CT_Start_Date = parse_date(child.text)
            if(len(CT_Start_Date) >4):
                map['CT_Start_Date'] = CT_Start_Date

        elif child.tag =='completion_date':
            CT_Completion_Date = parse_date(child.text)
            if (len(CT_Completion_Date) > 4):
                map['CT_Completion_Date'] = CT_Completion_Date

        elif child.tag =='primary_completion_date':
            CT_PCD = parse_date(child.text)
            if(len(CT_PCD)>4):
                map['CT_PCD'] = CT_PCD

        elif child.tag == 'phase':
            CT_Phase = parse_phase(child.text)
            map['CT_Phase'] = CT_Phase

        elif child.tag == 'study_type':
            CT_Study_Type = child.text
            map['CT_Study_Type'] = CT_Study_Type

        elif child.tag == 'study_design':
            CT_Study_Design =child.text
            map['CT_Study_Design'] = CT_Study_Design

        elif child.tag == 'location_countries':
            for country in child.findall('country'):
                if CT_Countries == 'Null':
                    CT_Countries = country.text
                else:
                    CT_Countries = CT_Countries +str(', ')+ country.text

        elif child.tag == 'verification_date':
            CT_Verification_Date = parse_date(child.text)
            if len(CT_Verification_Date) >4:
                map['CT_Verification_Date'] = CT_Verification_Date

        elif child.tag =='lastchanged_date':
            CT_Last_Changed_Date = parse_date(child.text)
            if(len(CT_Last_Changed_Date)>4):
                map['CT_Last_Changed_Date'] = CT_Last_Changed_Date

        elif child.tag == 'firstreceived_date':
            CT_First_Received_Date = parse_date(child.text)
            if len(CT_First_Received_Date) >4:
                map['CT_First_Received_Date'] = CT_First_Received_Date

        elif child.tag == 'is_fda_regulated':
            if(child.text == 'Yes' or child.text=='yes'):
                CT_Is_FDA_Regulated = 'Y'
                map['CT_Is_FDA_Regulated'] = CT_Is_FDA_Regulated

        elif child.tag == 'is_section_801':
            if (child.text == 'Yes' or child.text == 'yes'):
                CT_Is_Section_801= 'Y'
                map['CT_Is_Section_801'] = CT_Is_Section_801

        elif child.tag == 'acronym':
            CT_Acronym = child.text
            map['CT_Acronym'] = CT_Acronym

        elif child.tag =='intervention':
            intervention_type = child.find('intervention_type')
            intervention_name = child.find('intervention_name')
            if CT_Interventions == 'Null':
                CT_Interventions = intervention_type.text+": "+intervention_name.text
            else:
                CT_Interventions = CT_Interventions+" | "+intervention_type.text + ": " + intervention_name.text
    if CT_Interventions is not 'Null':
        map['CT_Interventions'] = CT_Interventions

    if CT_Countries is not 'Null':
        map['CT_Countries'] = CT_Countries

    return map

#populatin data into databse, arg Data is Dictionary retruned from parse_nct_xml
def push_in_db(data):
    print('Pushing Data into DB')
    #name of the table
    table = 'pageincrement'

    # Database connection object, makesure you have proper username, pwd and db field
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',  # make sure correct password
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 db='puru')

    cursor = connection.cursor()
    columns = ', '.join(data.keys())
    values = list(data.values())
    temp = ()
    for i in range(0,len(values)):
        temp = temp +(values[i],)

    sql = "INSERT INTO %s ( %s ) VALUES %s " % (table, columns, temp)
    try:
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except:
        traceback.print_exc()
        print(sql)
        print("Error In table structure!")



# https://clinicaltrials.gov/ct2/results?term=%2219.4.306%22+AND+%22Bridion%22&Search=Searchdisplayxml=true


def get_nct_data(nct_id):
    print("retriving NCT data for id: ",nct_id)
    strURL = 'https://clinicaltrials.gov/show/' + str(nct_id) + '?displayxml=true'
    # Requesting Clinical Trial API
    req = urlopen(strURL)
    return req


#print('Enter Search Term')
#search_term = input()
list1=['aubagio']
for indic1 in list1:

 strURL = "https://clinicaltrials.gov/ct2/results?term="+indic1+"&displayxml=true"
 req = urlopen(strURL)
 root = ET.parse(req).getroot()
 search_count = int(root.attrib['count'])
 total_pages = ceil(search_count/20)
 count = 1
 for i in range(1,total_pages+1):
    page_url = "https://clinicaltrials.gov/ct2/results?term="+indic1+"&pg="+str(i)+"&displayxml=true"
    print(page_url)
    print('finding NCT')
    page_data = urlopen(page_url)
    page_root = ET.parse(page_data).getroot()
    for child in page_root:
        if child.tag == 'clinical_study':
            print('Starting for: ',count)
            count=count+1
            nct_id = child.find('nct_id').text
            nct_data = get_nct_data(nct_id)
            map = parse_nct_xml_data(nct_data)
            push_in_db(map)
            print('done')