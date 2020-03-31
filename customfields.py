#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

from ringcentral.http.api_exception import ApiException
from ringcentral import SDK
from config import USERNAME, EXTENSION, PASSWORD, APP_KEY, APP_SECRET, SERVER


def main():

    sdk = SDK(APP_KEY, APP_SECRET, SERVER)
    platform = sdk.platform()
    platform.login(USERNAME, EXTENSION, PASSWORD)
    

    def getcustomfields():

        response = platform.get('/account/~/custom-fields')
        custom_fields = response.json()
        try:
         for x in range(len(custom_fields.records)):
             print('Display Name- ' + custom_fields.records[x].displayName + ' id- ' +custom_fields.records[x].id + ' Category- '+custom_fields.records[x].category + '\n' )
           
           #print(custom_fields.records)
        except ApiException as e:
         print("Error while fetching custom fields" + e)

   # This is to Fetch the custom Fields in an Account
    def createcustomfields():
        #POST Body
        body ={
             "category": "User",
             "displayName": "HRCODE-TEST3"
              }
        try:

            response =  platform.post('/account/~/custom-fields', body)
            print("Custom Field Created")
        
        except ApiException as e:
            print("Error while creating custom fields" + e)
    
     # This is to Fetch the custom Fields in an Account
    def updatecustomfields(id):
        #POST Body
        body ={
                "displayName": "HRCODE"
              }
        try:

            response =  platform.put('/account/~/custom-fields/{}'.format(id), body)
            print(response.json().displayName)
        except ApiException as e:
            print("Error while creating custom fields" + e)
    
    def deletecustomfields(id):
    
        try:


            response =  platform.delete('/account/~/custom-fields/{}'.format(id))
            
            print("Deleted")
            print("Custom Field Deleted")
        except ApiException as e:
            print("Error while creating custom fields" + e)

    #createcustomfields()
   #getcustomfields()
   #updatecustomfields(1016) 
   #deletecustomfields(41016)

    


    # GET API to get a List of the Extension Devices
    # API Endpoint https://platform.devtest.ringcentral.com/restapi/v1.0/account/accountId/extension/extensionId/device

    #response = platform.get('/account/~/extension/~/device')
    #device_list = response.json()

    #print('The Devices are' + str(device_list))

    # Simple GET 1
    #response = platform.get('/account/~/extension/~')
   # user = response.json()
   # user_id = str(user.id)
   # print('User loaded ' + user.name + ' (' + user_id + ')')
   # print('Headers ' + str(response.response().headers))

  #print(type(response.response()._content))

    # Multipart response
   # try:
   #  multipart_response = platform.get('/account/~/extension/' + user_id + ',' + user_id + '/presence').multipart()
       # print('Multipart 1\n' + str(multipart_response[0].json_dict()))
       # print('Multipart 2\n' + str(multipart_response[1].json_dict()))
    #except ApiException as e:
       # print('Cannot load multipart')
      #  print('URL ' + e.api_response().request().url)
      #  print('Response' + str(e.api_response().json()))

    # Simple GET 2
    #response = platform.get('/account/~/extension/~/device')
    #device = response.json()
    # Multipart response
   # try:
      #  print('Device ID - ' +  device.records[0].id + ' Name' +  device.records[0].name + ' Status - ' +device.records[0].status )
   # except ApiException as e:
      # print("Error while getting Device List")
# Testing Call-Out API
    # POST BODY
    #body = {
   # 'from': {
    #   'deviceId': '801534661005'
   #         },
   # 'to': {
    #    'phoneNumber': '+4083388064',
   #       }}
    #https://platform.ringcentral.com/restapi/v1.0/account/~/telephony/call-out
    #https://platform.ringcentral.com/restapi/v1.0/account/~/telephony/call-out
    #response =  platform.post('/account/~/telephony/call-out', body)

   # Testing Custom Fields

  



if __name__ == '__main__':
    main()
