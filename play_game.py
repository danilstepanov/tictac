import random
from selenium.webdriver import Chrome


def quick_win(parametr):
    driver = Chrome()
    driver.get("https://kirsorokin.github.io/tictactoe-angular-1.5/")
    table = driver.find_element_by_class_name("field")
    table_rows = table.find_elements_by_tag_name('tr')
    count_table_rows = len(table_rows)
    headers = table_rows[0]
    cells = headers.find_elements_by_tag_name('td')
    count_cells = 0
    for item in cells:
        count_cells += 1
    first_cell = random.randint(1, count_cells)
    first_row = random.randint(1, count_table_rows)
    end_cell = first_cell
    end_row = first_row
    if parametr == "row":
        for item in range(1, 6):
            if first_row > count_table_rows:
                end_row -= 1
                table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]' % (end_row, first_cell)).click()
            else:
                table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]' % (first_row, first_cell)).click()
                first_row +=1
    elif parametr == "cell":
        for item in range(1, 6):
            if first_cell > count_cells:
                end_cell -= 1
                table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]' % (first_row, end_cell)).click()
            else:
                table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]' % (first_row, first_cell)).click()
                first_cell +=1
    else:
        print "no parametr"
        return 0
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        print e
        return 0
    table = driver.find_element_by_class_name("field")
    assert(find_o(table.text)==1)
    driver.close()
    return 1

def find_o(text):
    count = 0
    for item in text:
        if item == 'O':
            count +=1
    if count != 5:
        print "ERROR, perezapis O"
        print "continue"
    return 1


