import csv
import os

dir_path = "path/to/csv/"

#open the file Ygr_GibiHouse.csv with UTF-8 character map
with open('Ygr_GibiHouse.csv', encoding='utf-8') as csvfile:
    #read one row at a time
    reader = csv.DictReader(csvfile)
    #create a list of dictionaries
    data = list(reader)

    for i in range(0, len(data)): 
        k = i // 1000   #divide by 1000 to get the thousandth digit

        #create a directory in dir_path
        if not os.path.exists(dir_path + str(k)):
            os.makedirs(dir_path + str(k))

        #create a html file
        # open the file
        with open(dir_path + str(k) + '\\gibi' + str(i) + '.html', 'w', encoding='utf-8') as html:  
            # write the html header
            html.write('<html>\n')
            # write the html body
            html.write('<body>\n')

            # write de email in the body       
            html.write(data[i]['RecDate'] + '<br>\n')    
            html.write(data[i]['From'] + '<br><br>\n')           
            html.write(data[i]['Subject'] + '<br><br>\n')                         
            html.write(data[i]['Message'] + '<br>\n')   

            # write the html footer
            html.write('</body>\n')
            html.write('</html>\n')

            # close the file
            html.close()

    #close the file
    csvfile.close()