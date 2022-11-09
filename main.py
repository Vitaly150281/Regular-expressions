from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

#pprint(contacts_list)

  pattern_name = r"(^[а-яёА-ЯЁ]+)[\,\s]?([а-яёА-ЯЁ]+)[\,\s]?([а-яёА-ЯЁ]*)\,{1,3}([а-яёА-ЯЁ]*)\,{1}([а-яёА-ЯЁ\s\-a-z]*)\,{1}([а-я\d\s\-+()\.]*)\,{0,1}([a-zA-Z\.@\d]*)"
  result_name = r"\1,\2,\3,\4,\5,\6,\7"

  pattern_phone = r"(\+7|8)*\s*\(?(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{2})\-?(\d{2})\s*\(?(\доб.)?\s*(\d{4})?\)?"
  result_phone = r"+7(\2)\3-\4-\5 \6\7"

  new_contacts_list = []

  for row in contacts_list:
      new_row = ','.join(row)
      new_row = re.sub(pattern_name, result_name, new_row)
      new_row = re.sub(pattern_phone, result_phone, new_row)
      new_contacts_list.append(new_row.split(","))

  for row1 in new_contacts_list:
      for row2 in new_contacts_list:
          if row1[0] == row2[0] and row1[1] == row2[1] and row1 is not row2:
              k = 2
              while k <= len(row1) - 1:
                  if row1[k] == '':
                      row1[k] = row2[k]
                  k += 1
              new_contacts_list.remove(row2)


#pprint(new_contacts_list)

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)

