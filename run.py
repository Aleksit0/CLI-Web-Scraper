import requests
from bs4 import BeautifulSoup
from csv import writer

# pocetni tekst
def main():
    print(" ")
    print("This is the first version of this CLI app.")
    print("For any suggestions contact me on alexa.codes(IG).")
    print(" ")

    # unos url-a
    unos_urla = input("Enter a Web Site that you want to scrape (URL) : ")

    # response dio
    url = requests.get(unos_urla)
    soup = BeautifulSoup(url.text, 'html.parser')   
    print("\n")

    # unos HTML elementa
    unos_elementa = input("Enter the HTML5 element : ")
    print("\n")

    # izbor elemenata
    if (unos_elementa == 'body'):
        print(soup.body)
    elif (unos_elementa == 'head'):
        print(soup.title)
    elif (unos_elementa == 'div'):
        print(soup.div)
    elif (unos_elementa == 'ul'):
        print(soup.ul)
    elif (unos_elementa == 'li'):
        print(soup.li)
    elif (unos_elementa == 'ol'):
        print(soup.ol)
    elif (unos_elementa == 'p'):
        print(soup.p)
    elif (unos_elementa == 'h1'):
        print(soup.h1)
    elif (unos_elementa == 'h2'):
        print(soup.h2)
    elif (unos_elementa == 'h3'):
        print(soup.h3)
    elif (unos_elementa == 'h4'):
        print(soup.h4)
    elif (unos_elementa == 'h5'):
        print(soup.h5)
    elif (unos_elementa == 'h6'):
        print(soup.h6)
    elif (unos_elementa == 'a'):
        print(soup.a)
    elif (unos_elementa == 'button'):
        print(soup.button)
    elif (unos_elementa == 'footer'):
        print(soup.footer)
    elif (unos_elementa == 'html'):
        print(soup.html)
    elif (unos_elementa == 'hr'):
        print(soup.hr)
    elif (unos_elementa == 'img'):
        print(soup.img)
    elif (unos_elementa == 'span'):
        print(soup.span)
    else:
        print("Error! Element not found!")

if __name__ == "__main__":
    main()