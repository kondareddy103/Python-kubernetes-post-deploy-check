import os
import re
import datetime
import json

contexts_information = {}
contextsNames = os.popen('kubectl config get-clusters').read()
print(contextsNames.split('\n')[1:])
os.system("rm -f context_details_pre_deployment.json")
os.system("rm -f context_count_details_pre_deployment.json")
f = open("context_details_pre_deployment.json", "a+")
f2 = open("context_count_details_pre_deployment.json", "a+")


for context in contextsNames.split('\n')[1:4]:
    if context == '':
        continue
        print("empty input")
    print('switching to context -->' + context)
    os.system('kubectl config use-context ' + context)
    #contexts_information["'" + context + "'"]['version'] = os.popen('kubectl version').read()
    #a = os.popen('kubectl get pods,svc,jobs --all-namespaces').read()
    contexts_information[context] = os.popen('kubectl get pods,svc,jobs --all-namespaces').read()
    kub_pv_count = os.popen('kubectl  get pv,pvc --all-namespaces  | wc -l').read()
    #json_helm_info = json.dumps(helm)
    json_count_info = json.dumps(kub_pv_count)
    f2.write(context + " = " + json_count_info + "\n")
    #helm =os.popen('helm ls').read()
json_context_info = json.dumps(contexts_information)
    #json_helm_info = json.dumps(helm)
f.write(json_context_info)
    #f.write(json_helm_info)
f.close()
f2.close()

with open('context_details_pre_deployment.json', 'r') as fPre:
    datastore = json.load(fPre)
    fPre.close()
with open('context_details_post_deployment.json', 'r') as fPost:
    datastore2 = json.load(fPost)
    fPost.close()



    for key, value in datastore.items() :
        print (key
