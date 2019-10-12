import sys

import module_define_codirovka as m1
import module_format_json_or_tsv as m2
import module_print as m3

if __name__ == '__main__':
    filename = 'files/' + sys.argv[1]

    open_result = m1.open_file(filename)  # определение кодировки

    format_data = m2.format_data(data=open_result, filename=filename) # определение формта
    m3.print_table(data=open_result, format_data=format_data) # форматированный вывод

