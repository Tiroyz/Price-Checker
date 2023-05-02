import csv

# csv.field_size_limit(sys.maxsize)

# TODO:  приделать этой хрени бинарный поиск, чтобы она не искала тут по два часа всё
# barcode = '4814185020168'
# barcode = '8594737253317'

def finder(barcode):
    i = True # Флаг, для остановки поиска в случае нахождения
    with open('Barcode_db.csv', encoding='utf-8', newline='') as f: # поиск штрих кода в первой базе данных
        reader = csv.reader(f, delimiter = '\t', quoting=csv.QUOTE_NONE)
        
        for row in reader:
            if row[1] == barcode: 
                return(row[2])
                i = False
                break
    if i:
        with open('barcodes.csv', encoding='utf-8', newline='') as d: # поиск штрих кода во второй базе данных
            reader = csv.reader(d, delimiter=';', quoting=csv.QUOTE_NONE)

            for row in reader:
                row_pointer=5

                if row: # Проверка на случай, если строка будет пустой 
                    for row_pointer in range(5, len(row)):  # В данной базе данных, если у товаров есть другие штрих коды, 
                                                            # они пишутся в той же строчке, но в дополнительных столбцах, 
                                                            # поэтому поиск проводится по ним, при наличии

                        str_barcode = str(row[row_pointer])
                        
                        if  str_barcode.find(str(barcode))!=-1: 
                            return(row[3])
                            i = False
                            break
    if i:
        return False
