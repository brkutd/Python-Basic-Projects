# Napisz program, który pobierze ciąg tekstowy od użytkownika,
# a następnie wypisze wszystkie linki z tego ciągu.
# Uwaga: Portal stepik.org ma problem z interpretacją linków.
# Dlatego wszystkie linki tutaj zamiast // mają ////.
# W rozwiązaniu w środowisku Pycharm używaj linków z //.


import re
text = input()
results = re.findall(r'\bhttps?:/{4}\w+\.[a-z]{2,3}(\.)?[a-z]{2,3}\b', text)
print(results)
