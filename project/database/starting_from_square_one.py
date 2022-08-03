import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nav@12905', database = 'grocery_store')
mycursor=mydb.cursor()

def insert_books():
    ans = 'y'
    while ans == 'y':
        book_id = int(input('input book id'))
        book_name = input('input book name')
        author_name = input('input author name')
        genre = input('input genre')
        price = int(input('input book price'))
        mycursor.execute('insert into all_books values("{}",{},{},{},"{}")'.format(book_id,book_name,author_name,genre,price))
        mydb.commit()
        ans = input ('do you want to add more records? (y/n)')
insert_books()


    
