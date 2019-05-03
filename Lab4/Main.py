from County import County



import csv

def main():
    path_file = ["./unifiedCancerData_212.csv", "./unifiedCancerData_562.csv", "./unifiedCancerData_1041.csv",
                 "./unifiedCancerData_3108.csv"]

    file_counties_element = []
    for file in path_file:
        county_list = {}  # mappa che racchiude gli id delle contee associate alla contea stessa

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                print("",row[0])
                line_count += 1
                county = County(row[0], row[1], row[2], row[3], row[4])
                county_list[row[0]] = county
                #county_list.append(county)

            file_counties_element.append(county_list)
            #print(f'Processed {line_count} lines.')
    #print(file_counties_element)



























if __name__ == '__main__':
    main()
