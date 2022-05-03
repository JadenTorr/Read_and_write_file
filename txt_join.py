import os


def txt_file_snowman():
    file_list = os.listdir()
    txt_files = [file for file in file_list if '.txt' == file[len(file) - 4 :] and file != 'result.txt' and file != 'file.txt']
    lines_list = []
    tmp_dict = {}

    for el in txt_files:
        with open(el, encoding='utf-8') as f:
            tmp_file = f.readlines()
            len_tmp_file = len(tmp_file)
            lines_list.append(len_tmp_file)
            tmp_dict[len_tmp_file] = (el, tmp_file)


    lines_list.sort()

    with open('result.txt', 'a+', encoding='utf-8') as f:
        for lines in lines_list:
            f.write(tmp_dict[lines][0])
            f.write('\n')
            f.write(str(lines))
            f.write('\n')
            f.writelines(tmp_dict[lines][1])
            f.write('\n')

txt_file_snowman()