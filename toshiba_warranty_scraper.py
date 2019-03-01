import requests
import csv
import time

def getData(search_input):
    # This Function builds URL and posts GET to toshiba website

    base = "https://support.toshiba.com/support/warrantyResults?sno="
    serial = search_input
    url = base + serial

    data = requests.get(url).json()

    # Create variables for all data I want to extract
    serialNo = (data["commonBean"]["serialNumber"])
    warrantyOnsiteExpiryDate = (data["commonBean"]["warrantyOnsiteExpiryDate"])
    partNumber = (data["commonBean"]["partNumber"])
    warrantyExpiryDate = (data["commonBean"]["warrantyExpiryDate"])
    customerPurchaseDate = (data["commonBean"]["customerPurchaseDate"])
    warranty = (data["warranty"])
    hasWarrantyExpired = ("warranty expired? " + str(data["hasWarrantyExpired"]))

    # Write CSV row and close
    row = [serialNo, warrantyOnsiteExpiryDate, partNumber, warrantyExpiryDate, customerPurchaseDate, warranty, hasWarrantyExpired]
    with open("output_toshiba.csv", 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()

    # Rate limit requests
    time.sleep(0.25)

    # print(serialNo)
    # print(warrantyOnsiteExpiryDate)
    # print(partNumber)
    # print(warrantyExpiryDate)
    # print(customerPurchaseDate)
    # print(warranty)
    # print(hasWarrantyExpired)

def machineGun():
    text_file = open("serials.txt", "r")
    list_of_serials = text_file.readlines()

    # Run getData func on each serial in txt file
    for obj in list_of_serials:
        getData(obj)


machineGun()