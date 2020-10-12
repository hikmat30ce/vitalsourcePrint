# vitalsourcePrint
This code will download vitalsource book. Each page will be image. Latter it can be passed to ocr and merge pdf

This use python version : ````Python 3.8.3````

### Command line param 
````angular2html
--course <Course title in url>
--loginurl https://bookshelf.vitalsource.com/#/user/signin
--email <email>
--password <password>
--title <title>
--total_pages 133
--initial_page 1
--resolution 4
````

## Example
````
python .\printbook.py --course <Course title in url> --email <email> --password <password> --title <title> --total_pages 133

````