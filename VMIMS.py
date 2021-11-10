# Reference: 

import datetime
import csv

class DailyEntry:

    # Drink Prices
    Type1Price = 3
    Type2Price = 2.5
    Type3Price = 2
    Type4Price = 4

    # Drink Costs
    Type1Cost = 2
    Type2Cost = 1.5
    Type3Cost = 1
    Type4Cost = 3

    def __init__(self):
        self.chicken = 0
        
    def input_date():
        print('ENTER A YEAR') # enter year prompt
        yr = int(input('YEAR: ')) # entered year - integer type b/c this is what datetime.date() accepts
        print('ENTER MONTH OF THE YEAR') # enter month prompt
        mo = int(input('MONTH: ')) # entered month - integer type for same reason as yr type
        print('ENTER DAY OF THE MONTH ') # enter day prompt
        dy = int(input('DAY: ')) # entered day - integer type for same reason as yr type

        DailyEntry.check_for_log(yr,mo,dy)

        print('Done. Back to main menu.')
        return Main.main_menu()
        
    def check_for_log(yr,mo,dy):

        try:# try to open a runnning log for the given year
            
            with open(f'Running_Log_{yr}.csv', 'r', encoding = 'utf-8') as RunningLog:
                None

            print('successfully opened running log')# will be built out to append info for a day
            DailyEntry.edit_existing_log(yr,mo,dy)
                
        except: # if no running log exists for the given year, one will be created
            DailyEntry.create_new_log(yr,mo,dy)
            print('did not find existing running log for entered year, new one created')

    def create_new_log(yr,mo,dy):
        
        with open(f'Running_Log_{yr}.csv', 'w', encoding = 'utf-8') as RunningLog:
            fieldnames = ['Date','Quantity Sold','Revenue','Cost','Profit','On Hand Qty']
            write_log = csv.DictWriter(RunningLog, fieldnames=fieldnames) # csv writer - dictwriter maps key values to rows

            day_to_write = datetime.date(yr, 1, 1) # the date that will be printed in the date column
            row = str(day_to_write) # the date in a list, to print in the column
            one_day = datetime.timedelta(days=1) # a datetime class obj containg one day interval to increment the date to write
            
            start_date = datetime.date(yr, 1, 1) # first day of the given year
            end_date = datetime.date(yr,12,31) # last day of the given year
            
            iterations = start_date - end_date # get range of days for given yr (365 or 366) - type is a datetime class obj
            iterations = str(iterations) # convert type to string
            iterations = iterations[1:4] # grab just the three digit days portion
            iterations = int(iterations) # convert to int type
            iterations += 1 # add one to iterations because range is days between 2 dates
            write_log.writeheader() # print the field names in the first row

            

            for i in range(iterations):# for every day of the year
                write_log.writerow({'Date':row})# write the date in the leftmost column
                write_log.writerow({'Date':'Total'})
                write_log.writerow({'Date':'Type 1'})
                write_log.writerow({'Date':'Type 2'})
                write_log.writerow({'Date':'Type 3'})
                write_log.writerow({'Date':'Type 4'})
                day_to_write += one_day# increment the date to write by a year
                row = str(day_to_write)# recapture the date to write as a string type - log is list of strings
                
        DailyEntry.edit_existing_log(yr,mo,dy)


    def edit_existing_log(yr,mo,dy):
        print('Daily Entry')
        drink1qty = int(input('Drink 1 QTY Sold: '))
        drink2qty = int(input('Drink 2 QTY Sold: '))
        drink3qty = int(input('Drink 3 QTY Sold: '))
        drink4qty = int(input('Drink 4 QTY Sold: '))

        cost1 = drink1qty * DailyEntry.Type1Cost
        cost2 = drink2qty * DailyEntry.Type2Cost
        cost3 = drink3qty * DailyEntry.Type3Cost
        cost4 = drink4qty * DailyEntry.Type4Cost
        total_cost = cost1 + cost2 +cost3 + cost4

        revenue1 = drink1qty * DailyEntry.Type1Price
        revenue2 = drink2qty * DailyEntry.Type2Price
        revenue3 = drink3qty * DailyEntry.Type3Price
        revenue4 = drink4qty * DailyEntry.Type4Price
        total_revenue = revenue1 + revenue2 + revenue3 + revenue4

        profit1 = revenue1 - cost1
        profit2 = revenue2 - cost2
        profit3 = revenue3 - cost3
        profit4 = revenue4 - cost4
        total_profit = profit1 + profit2 + profit3 + profit4
        
        

        mon = mo

        d = dy

        if mon < 10:
            mon = str(mon)
            mon = '0' + mon


        if d < 10:
            d = str(dy)
            d = '0' + d
        
        
        Log_List = []
        
        with open(f'Running_Log_{yr}.csv', 'r', encoding= 'utf-8') as RunningLog:
            Read_Log = csv.DictReader(RunningLog)
            Log_List.extend(Read_Log)

        for num_line, row in enumerate(Log_List):
            
            if row['Date'] == f'{yr}-{mon}-{d}':
                Log_List[num_line+1]['Quantity Sold'] = drink1qty + drink2qty + drink3qty + drink4qty
                Log_List[num_line+2]['Quantity Sold'] = drink1qty
                Log_List[num_line+3]['Quantity Sold'] = drink2qty
                Log_List[num_line+4]['Quantity Sold'] = drink3qty
                Log_List[num_line+5]['Quantity Sold'] = drink4qty

                Log_List[num_line+1]['Revenue'] = total_revenue
                Log_List[num_line+2]['Revenue'] = revenue1
                Log_List[num_line+3]['Revenue'] = revenue2
                Log_List[num_line+4]['Revenue'] = revenue3
                Log_List[num_line+5]['Revenue'] = revenue4

                Log_List[num_line+1]['Cost'] = total_cost
                Log_List[num_line+2]['Cost'] = cost1
                Log_List[num_line+3]['Cost'] = cost2
                Log_List[num_line+4]['Cost'] = cost3
                Log_List[num_line+5]['Cost'] = cost4

                Log_List[num_line+1]['Profit'] = total_profit
                Log_List[num_line+2]['Profit'] = profit1
                Log_List[num_line+3]['Profit'] = profit2
                Log_List[num_line+4]['Profit'] = profit3
                Log_List[num_line+5]['Profit'] = profit4

                
                
                

                
        with open(f'Running_Log_{yr}.csv', 'w', encoding = 'utf-8') as RunningLog:
            fieldnames = ['Date','Quantity Sold','Revenue','Cost','Profit','On Hand Qty']
            write_log = csv.DictWriter(RunningLog, fieldnames=fieldnames)
            write_log.writeheader()
            for row in Log_List:
                write_log.writerow(row)


class ViewDaily:

    def daily_menu():

        print('ENTER A YEAR') # enter year prompt
        yr = int(input('YEAR: ')) # entered year - integer type b/c this is what datetime.date() accepts
        print('ENTER MONTH OF THE YEAR') # enter month prompt
        mo = int(input('MONTH: ')) # entered month - integer type for same reason as yr type
        print('ENTER DAY OF THE MONTH ') # enter day prompt
        dy = int(input('DAY: ')) # entered day - integer type for same reason as yr type

        print('What data would you like to see?')
        print('1) Daily Profit')
        print('2) Daily Cost')
        print('3) Daily Revenue')
        print('4) Daily Quantity Sold')

        Log_List = []

        option = int(input('Option: '))

        mon = mo

        d = dy

        if mon < 10:
            mon = str(mon)
            mon = '0' + mon


        if d < 10:
            d = str(dy)
            d = '0' + d
        

        try:
            with open(f'Running_Log_{yr}.csv', 'r', encoding= 'utf-8') as RunningLog:
                Read_Log = csv.DictReader(RunningLog)
                Log_List.extend(Read_Log)
        except:
            print('Running Log does not exist for the entered year. Going back to main menu.\n')
            return Main.main_menu()
            
        if option == 1:
                
                for num_line, row in enumerate(Log_List):
                    if row['Date'] == f'{yr}-{mon}-{d}':
                        print('total:', Log_List[num_line + 1]['Profit'])
                        print('drink 1:',Log_List[num_line + 2]['Profit'])
                        print('drink 2:',Log_List[num_line + 3]['Profit'])
                        print('drink 3:',Log_List[num_line + 4]['Profit'])
                        print('drink 4:',Log_List[num_line + 5]['Profit'])

        elif option == 2:
            
                for num_line, row in enumerate(Log_List):
                    if row['Date'] == f'{yr}-{mon}-{d}':
                        print('total:', Log_List[num_line + 1]['Cost'])
                        print('drink 1:',Log_List[num_line + 2]['Cost'])
                        print('drink 2:',Log_List[num_line + 3]['Cost'])
                        print('drink 3:',Log_List[num_line + 4]['Cost'])
                        print('drink 4:',Log_List[num_line + 5]['Cost'])

        elif option == 3:

                for num_line, row in enumerate(Log_List):
                    if row['Date'] == f'{yr}-{mon}-{d}':
                        print('total:', Log_List[num_line + 1]['Revenue'])
                        print('drink 1:',Log_List[num_line + 2]['Revenue'])
                        print('drink 2:',Log_List[num_line + 3]['Revenue'])
                        print('drink 3:',Log_List[num_line + 4]['Revenue'])
                        print('drink 4:',Log_List[num_line + 5]['Revenue'])

        elif option == 4:

                for num_line, row in enumerate(Log_List):
                    if row['Date'] == f'{yr}-{mon}-{d}':
                        print('total:', Log_List[num_line + 1]['Quantity Sold'])
                        print('drink 1:',Log_List[num_line + 2]['Quantity Sold'])
                        print('drink 2:',Log_List[num_line + 3]['Quantity Sold'])
                        print('drink 3:',Log_List[num_line + 4]['Quantity Sold'])
                        print('drink 4:',Log_List[num_line + 5]['Quantity Sold'])

        else:
            print('Invalid Option. Back to main menu.\n')
            return Main.main_menu()

        print('Done. Back to main menu.\n')
        return Main.main_menu()
        

        
            

class ViewMonthly:

    def menu():

        print('ENTER A YEAR') # enter year prompt
        yr = int(input('YEAR: ')) # entered year - integer type b/c this is what datetime.date() accepts
        print('ENTER MONTH OF THE YEAR') # enter month prompt
        mo = int(input('MONTH: ')) # entered month - integer type for same reason as yr type
        
        print('What monthly data would you like to see?')
        print('1) Quantity')
        print('2) Cost')
        print('3) Revenue')
        print('4) Profit')

        option = int(input('Option: '))

        Log_List = []

        mon = mo

        if mon < 10:
            mon = str(mon)
            mon = '0' + mon
        
        try:
            with open(f'Running_Log_{yr}.csv', 'r', encoding= 'utf-8') as RunningLog:
                Read_Log = csv.DictReader(RunningLog)
                Log_List.extend(Read_Log)
        except:
            print('Running Log does not exist for the entered year. Going back to main menu.\n')
            return Main.main_menu()


        if option == 1:
            ViewMonthly.monthly_quantity(yr, mon,Log_List)

        elif option == 2:
            ViewMonthly.monthly_cost(yr,mon,Log_List)

        elif option == 3:
            ViewMonthly.monthly_revenue(yr,mon,Log_List)

        elif option == 4:
            ViewMonthly.monthly_revenue(yr,mon,Log_List)
            
        else:
            print('Invalid Option. Back to main menu.\n')
            return Main.main_menu()

        print('Done. Back to main menu.\n')
        return Main.main_menu()
            

    def monthly_quantity(yr,mon,Log_List):
        total_qty = 0
        type1_qty = 0
        type2_qty = 0
        type3_qty = 0
        type4_qty = 0
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-3] == f'{yr}-{mon}':
                if any(Log_List[num_line + 1]['Quantity Sold']) == True:
                    total_qty += float(Log_List[num_line + 1]['Quantity Sold'])

                if any(Log_List[num_line + 2]['Quantity Sold']) == True:
                    type1_qty += float(Log_List[num_line + 2]['Quantity Sold'])

                if any(Log_List[num_line + 3]['Quantity Sold']) == True:
                    type2_qty += float(Log_List[num_line + 3]['Quantity Sold'])

                if any(Log_List[num_line + 4]['Quantity Sold']) == True:
                    type3_qty += float(Log_List[num_line + 4]['Quantity Sold'])

                if any(Log_List[num_line + 5]['Quantity Sold']) == True:
                    type4_qty += float(Log_List[num_line + 5]['Quantity Sold'])

        print(f'total quantity for month - {total_qty}')
        print(f'drink 1 qty - {type1_qty}')
        print(f'drink 2 qty - {type2_qty}')
        print(f'drink 3 qty - {type3_qty}')
        print(f'drink 4 qty - {type4_qty}')

    def monthly_cost(yr, mon,Log_List):

        total_cost = 0
        type1_cost = 0
        type2_cost = 0
        type3_cost = 0
        type4_cost = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-3] == f'{yr}-{mon}':
                if any(Log_List[num_line + 1]['Cost']) == True:
                    total_cost += float(Log_List[num_line + 1]['Cost'])

                if any(Log_List[num_line + 2]['Cost']) == True:
                    type1_cost += float(Log_List[num_line + 2]['Cost'])

                if any(Log_List[num_line + 3]['Cost']) == True:
                    type2_cost += float(Log_List[num_line + 3]['Cost'])

                if any(Log_List[num_line + 4]['Cost']) == True:
                    type3_cost += float(Log_List[num_line + 4]['Cost'])

                if any(Log_List[num_line + 5]['Cost']) == True:
                    type4_cost += float(Log_List[num_line + 5]['Cost'])
                    

        print(f'total cost for month - {total_cost}')
        print(f'drink 1 cost - {type1_cost}')
        print(f'drink 2 cost - {type2_cost}')
        print(f'drink 3 cost - {type3_cost}')
        print(f'drink 4 cost - {type4_cost}')
        

    def monthly_revenue(yr, mon, Log_List):
        
        total_rev = 0
        type1_rev = 0
        type2_rev = 0
        type3_rev = 0
        type4_rev = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-3] == f'{yr}-{mon}':
                if any(Log_List[num_line + 1]['Revenue']) == True:
                    total_rev += float(Log_List[num_line + 1]['Revenue'])

                if any(Log_List[num_line + 2]['Revenue']) == True:
                    type1_rev += float(Log_List[num_line + 2]['Revenue'])

                if any(Log_List[num_line + 3]['Revenue']) == True:
                    type2_rev += float(Log_List[num_line + 3]['Revenue'])

                if any(Log_List[num_line + 4]['Revenue']) == True:
                    type3_rev += float(Log_List[num_line + 4]['Revenue'])

                if any(Log_List[num_line + 5]['Revenue']) == True:
                    type4_rev += float(Log_List[num_line + 5]['Revenue'])

        print(f'total Revenue for month - {total_rev}')
        print(f'drink 1 revenue - {type1_rev}')
        print(f'drink 2 revenue - {type2_rev}')
        print(f'drink 3 revenue - {type3_rev}')
        print(f'drink 4 revenue - {type4_rev}')
        

    def monthly_profit(yr,mon,Log_List):

        total_prof = 0
        type1_prof = 0
        type2_prof = 0
        type3_prof = 0
        type4_prof = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-3] == f'{yr}-{mon}':
                if any(Log_List[num_line + 1]['Profit']) == True:
                    total_prof += float(Log_List[num_line + 1]['Profit'])

                if any(Log_List[num_line + 2]['Profit']) == True:
                    type1_prof += float(Log_List[num_line + 2]['Profit'])

                if any(Log_List[num_line + 3]['Profit']) == True:
                    type2_prof += float(Log_List[num_line + 3]['Profit'])

                if any(Log_List[num_line + 4]['Profit']) == True:
                    type3_prof += float(Log_List[num_line + 4]['Profit'])

                if any(Log_List[num_line + 5]['Profit']) == True:
                    type4_prof += float(Log_List[num_line + 5]['Profit'])

        print(f'total profit for month - {total_prof}')
        print(f'drink 1 profit - {type1_prof}')
        print(f'drink 2 profit - {type2_prof}')
        print(f'drink 3 profit - {type3_prof}')
        print(f'drink 4 profit - {type4_prof}')

        
class ViewAnnual:
    
    def menu():
        print('ENTER A YEAR') # enter year prompt
        yr = int(input('YEAR: ')) # entered year - integer type b/c this is what datetime.date() accepts

        print('What annual data would you like to see?')
        print('1) Quantity')
        print('2) Cost')
        print('3) Revenue')
        print('4) Profit')

        option = int(input('Option: '))
        
        Log_List = []
        
        
        try:
            with open(f'Running_Log_{yr}.csv', 'r', encoding= 'utf-8') as RunningLog:
                Read_Log = csv.DictReader(RunningLog)
                Log_List.extend(Read_Log)
        except:
            print('Running Log does not exist for the entered year. Going back to main menu.\n')
            return Main.main_menu()

        if option == 1:
            ViewAnnual.annual_quantity(yr, Log_List)
            
        elif option == 2:
            ViewAnnual.annual_cost(yr, Log_List)

        elif option == 3:
            ViewAnnual.annual_revenue(yr, Log_List)

        elif option == 4:
            ViewAnnual.annual_profit(yr, Log_List)

        else:
            print('Invalid Option. Back to main menu.\n')
            return Main.main_menu()

        print('Done. Back to main menu.\n')
        return Main.main_menu()

    def annual_quantity(yr, Log_List):
        
        total_qty = 0
        type1_qty = 0
        type2_qty = 0
        type3_qty = 0
        type4_qty = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-6] == f'{yr}':
                
                if any(Log_List[num_line + 1]['Quantity Sold']) == True:
                    total_qty += float(Log_List[num_line + 1]['Quantity Sold'])

                if any(Log_List[num_line + 2]['Quantity Sold']) == True:
                    type1_qty += float(Log_List[num_line + 2]['Quantity Sold'])

                if any(Log_List[num_line + 3]['Quantity Sold']) == True:
                    type2_qty += float(Log_List[num_line + 3]['Quantity Sold'])

                if any(Log_List[num_line + 4]['Quantity Sold']) == True:
                    type3_qty += float(Log_List[num_line + 4]['Quantity Sold'])

                if any(Log_List[num_line + 5]['Quantity Sold']) == True:
                    type4_qty += float(Log_List[num_line + 5]['Quantity Sold'])

        print(f'total quantity for the year - {total_qty}')
        print(f'drink 1 qty - {type1_qty}')
        print(f'drink 2 qty - {type2_qty}')
        print(f'drink 3 qty - {type3_qty}')
        print(f'drink 4 qty - {type4_qty}')

    def annual_cost(yr,Log_List):

        total_cost = 0
        type1_cost = 0
        type2_cost = 0
        type3_cost = 0
        type4_cost = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-6] == f'{yr}':
                if any(Log_List[num_line + 1]['Cost']) == True:
                    total_cost += float(Log_List[num_line + 1]['Cost'])

                if any(Log_List[num_line + 2]['Cost']) == True:
                    type1_cost += float(Log_List[num_line + 2]['Cost'])

                if any(Log_List[num_line + 3]['Cost']) == True:
                    type2_cost += float(Log_List[num_line + 3]['Cost'])

                if any(Log_List[num_line + 4]['Cost']) == True:
                    type3_cost += float(Log_List[num_line + 4]['Cost'])

                if any(Log_List[num_line + 5]['Cost']) == True:
                    type4_cost += float(Log_List[num_line + 5]['Cost'])
                    

        print(f'total cost for year - {total_cost}')
        print(f'drink 1 cost - {type1_cost}')
        print(f'drink 2 cost - {type2_cost}')
        print(f'drink 3 cost - {type3_cost}')
        print(f'drink 4 cost - {type4_cost}')

    def annual_revenue(yr, Log_List):

        total_rev = 0
        type1_rev = 0
        type2_rev = 0
        type3_rev = 0
        type4_rev = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-6] == f'{yr}':
                if any(Log_List[num_line + 1]['Revenue']) == True:
                    total_rev += float(Log_List[num_line + 1]['Revenue'])

                if any(Log_List[num_line + 2]['Revenue']) == True:
                    type1_rev += float(Log_List[num_line + 2]['Revenue'])

                if any(Log_List[num_line + 3]['Revenue']) == True:
                    type2_rev += float(Log_List[num_line + 3]['Revenue'])

                if any(Log_List[num_line + 4]['Revenue']) == True:
                    type3_rev += float(Log_List[num_line + 4]['Revenue'])

                if any(Log_List[num_line + 5]['Revenue']) == True:
                    type4_rev += float(Log_List[num_line + 5]['Revenue'])

        print(f'total revenue for year - {total_rev}')
        print(f'drink 1 revenue - {type1_rev}')
        print(f'drink 2 revenue - {type2_rev}')
        print(f'drink 3 revenue - {type3_rev}')
        print(f'drink 4 revenue - {type4_rev}')

    def annual_profit(yr,Log_List):

        total_prof = 0
        type1_prof = 0
        type2_prof = 0
        type3_prof = 0
        type4_prof = 0
        
        for num_line, row in enumerate(Log_List):
            
            if row['Date'][:-6] == f'{yr}':
                if any(Log_List[num_line + 1]['Profit']) == True:
                    total_prof += float(Log_List[num_line + 1]['Profit'])

                if any(Log_List[num_line + 2]['Profit']) == True:
                    type1_prof += float(Log_List[num_line + 2]['Profit'])

                if any(Log_List[num_line + 3]['Profit']) == True:
                    type2_prof += float(Log_List[num_line + 3]['Profit'])

                if any(Log_List[num_line + 4]['Profit']) == True:
                    type3_prof += float(Log_List[num_line + 4]['Profit'])

                if any(Log_List[num_line + 5]['Profit']) == True:
                    type4_prof += float(Log_List[num_line + 5]['Profit'])

        print(f'total profit for year - {total_prof}')
        print(f'drink 1 profit - {type1_prof}')
        print(f'drink 2 profit - {type2_prof}')
        print(f'drink 3 profit - {type3_prof}')
        print(f'drink 4 profit - {type4_prof}')

def option5():
    pass

def option6():
    pass

class Main:

    def main_menu():
        
        print('WHAT TYPE OF DATA WOULD YOU LIKE TO VIEW/ENTER?\n')

        print('1) MAKE A DAILY ENTRY')
        print('2) VIEW DAILY DATA')
        print('3) VIEW MONTHLY DATA')
        print('4) VIEW ANNUAL DATA')
        print('5) VIEW SEASONAL DATA')
        print('6) VIEW OTHER DATA')
        print('7) QUIT\n')
        
        option = int(input('OPTION:'))

        if option == 1:
            DailyEntry.input_date()

        if option == 2:
            ViewDaily.daily_menu()

        if option == 3:
            
            ViewMonthly.menu()

        if option == 4:
            ViewAnnual.menu()

        if option == 7:
            exit()
        

Main.main_menu()
