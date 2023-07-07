import requests

for i in range(1,5000):
    customerurl=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r=requests.get(url=customerurl)

    if r.status_code==200:
        print(customerurl)

        continue

    # else:
    #     print("unable to fetch the url")


