import sqlite3
import dbm.gnu
import dbm
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import datetime

db = sqlite3.connect('music1.db')
cur = db.cursor()

def init():
    cur.execute("DROP TABLE IF EXISTS MusicLibrary")
    cur.execute("""CREATE TABLE IF NOT EXISTS MusicLibrary 
                (AlbumId integer primary key, Author text, Title text, TracksNr int, Tracks text, PublishYear int, Genre text, Rented int)""")
    cur.execute("""INSERT INTO MusicLibrary VALUES
                (0, 'Red Hot Chili Peppers','Californication', 15, "Around the World; Parallel Universe; Scar Tissue; Otherside; Get on Top; Californication; Easily; Porcelain; Emit Remmus; I Like Dirt; This Velvet Glove; Savior; Purple Stain; Right on Time; Road Trippin'", 1999, 'Rock', 1)""")
    cur.execute("""INSERT INTO MusicLibrary VALUES
                (1, 'Red Hot Chili Peppers','Stadium Arcadium', 1, 'Dani California', 2004, 'Rock', 1)""")
    db.commit()

class InitWindow(Gtk.Window): #ustal marginesy
    def __init__(self):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(200,150)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        label = Gtk.Label("Wybierz opcję:")
        browse_button = Gtk.Button.new_with_label("Przeszukaj kolekcję")
        browse_button.connect("clicked",self.on_browse_button_clicked)
        add_button = Gtk.Button.new_with_label("Dodaj album...")
        add_button.connect("clicked",self.on_add_button_clicked)
        edit_button = Gtk.Button.new_with_label("Edytuj album...")
        edit_button.connect("clicked",self.on_edit_button_clicked)
        exit_button = Gtk.Button.new_with_label("Wyjdź")
        exit_button.connect("clicked",Gtk.main_quit)
        vbox.pack_start(label,True,True,0)
        vbox.pack_start(browse_button,True,True,0)
        vbox.pack_start(add_button,True,True,0)
        vbox.pack_start(edit_button,True,True,0)
        vbox.pack_start(exit_button,True,True,0)
        self.add(vbox)

    def on_browse_button_clicked(self, button):
        self.destroy()
        select = SelectWindow()
        select.connect("delete-event",Gtk.main_quit)
        select.show_all()
    
    def on_add_button_clicked(self, button):
        self.destroy()
        add = AddWindow()
        add.connect("delete-event",Gtk.main_quit)
        add.show_all()
    
    def on_edit_button_clicked(self, button):
        self.destroy()
        edit = EditWindow1()
        edit.connect("delete-event",Gtk.main_quit)
        edit.show_all()

class SelectWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(300,200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.show_label = Gtk.Label("Wyświetl względem kategori:")
        vbox.pack_start(self.show_label, True, True, 0)
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
        self.grid.set_column_homogeneous(True)
        self.grid.set_column_spacing(4)
        self.grid.set_row_spacing(4)

        button1 = Gtk.Button(label="Albumy")
        button1.connect("clicked",self.on_button_clicked,"albums")
        button1.set_size_request(50,50)

        button2 = Gtk.Button(label="Wykonawcy")
        button2.connect("clicked",self.on_button_clicked,"authors")
        button2.set_size_request(50,50)

        button3 = Gtk.Button(label="Utwory")
        button3.connect("clicked",self.on_button_clicked,"songs")
        button3.set_size_request(50,50)

        button4 = Gtk.Button(label="Gatunki")
        button4.connect("clicked",self.on_button_clicked,"genres")
        button4.set_size_request(50,50)
        
        self.grid.attach(button1,0,0,3,3)
        self.grid.attach(button2,3,0,3,3)
        self.grid.attach(button3,0,3,3,3)
        self.grid.attach(button4,3,3,3,3)
        vbox.pack_start(self.grid, False, False, 0)

        button5 = Gtk.Button(label="Powrót")
        button5.connect("clicked",self.on_return_button_clicked)
        button5.set_size_request(30,30)
        vbox.pack_start(button5, False, True, 0)
        self.add(vbox)

    def on_button_clicked(self, button, attr):
        self.destroy()
        win = BrowseWindow(attr)
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

    def on_return_button_clicked(self, button):
        self.destroy()
        win = InitWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

class BrowseWindow(Gtk.Window):
    def __init__(self,attr):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(500,300)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        if(attr=='albums'):
            cur.execute("""SELECT Title AS Album, Author AS Wykonawca, Genre AS Gatunek, PublishYear AS Rok, Rented AS 'Czy wypożyczona' FROM MusicLibrary 
                        ORDER BY Genre, Author, Title""")
            store = Gtk.ListStore(str,str,str,int,int)
            columns = 5
        elif(attr=='authors'):
            cur.execute("""SELECT Author AS Wykonawca, count(Title) AS 'Liczba płyt', sum(Rented) AS 'Ile wypożyczonych'  
                        FROM MusicLibrary GROUP BY Author ORDER BY 'Liczba płyt'""")
            store = Gtk.ListStore(str,int,int)
            columns = 3
        elif(attr=='songs'):
            cur.execute("""SELECT Tracks, Title AS Album, Author AS Wykonawca
                        FROM MusicLibrary ORDER BY Author, Title""")
            store = Gtk.ListStore(str,str,str)
            columns = 3
        elif(attr=='genres'):
            cur.execute("""SELECT Genre AS Gatunek, count(Title) AS 'Liczba płyt', sum(Rented) AS 'Ile wypożyczonych' 
                        FROM MusicLibrary GROUP BY Genre ORDER BY 'Liczba płyt' DESC""")
            store = Gtk.ListStore(str,int,int)
            columns = 3

        names = list(map(lambda x: x[0], cur.description))
        if(attr=='songs'):
            names[0]='Utwór'
            self.populate_store_songs(store, cur)
        else:
            self.populate_store(store, cur)

        self.treeview = Gtk.TreeView(model=store)
        renderer = Gtk.CellRendererText()

        for i in range(columns):
            column = Gtk.TreeViewColumn(names[i], renderer, text=i)
            column.set_sort_column_id(i)
            self.treeview.append_column(column)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(self.treeview)
        scrolled_window.set_min_content_height(200)

        vbox.pack_start(scrolled_window, True, True, 0)
        return_button = Gtk.Button("Powrót")
        return_button.connect("clicked",self.on_return_button_clicked)
        vbox.pack_start(return_button,True,True,0)
        self.add(vbox)

    def populate_store(self, store, cursor):
        rows = cursor.fetchall()
        for row in rows:
            store.append(row)

    def populate_store_songs(self, store, cursor):
        rows = cursor.fetchall()
        for row in rows:
            songs = row[0].split(";")
            for s in songs:
                if(s[0] == ' '):
                    s = s[1:]
                store.append([s,row[1],row[2]])

    def on_return_button_clicked(self, button):
        self.destroy()
        win = SelectWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

#TODO Dodać opcje w menu głównym "edytuj"/"wypożycz" dzięki której będzie możliwy update
# Podać trzeba będzie "Author" "Title" i następnie będzie można podać edytowane cechy

class AddWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(500,300)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        labels = ["Wykonawca:","Album:","Liczba utworów:", "Lista utworów:","Gatunek:","Rok:"]
        for l in labels:
            label = Gtk.Label(l)
            vbox1.pack_start(label,True,True,6)
        
        self.author_entry = Gtk.Entry()
        self.album_entry = Gtk.Entry()
        self.tracknr_entry = Gtk.Entry()
        self.tracks_entry = Gtk.Entry()
        self.genre_entry = Gtk.Entry()
        self.year_entry = Gtk.Entry()

        vbox2.pack_start(self.author_entry,True,True,6)
        vbox2.pack_start(self.album_entry,True,True,6)
        vbox2.pack_start(self.tracknr_entry,True,True,6)
        vbox2.pack_start(self.tracks_entry,True,True,6)
        vbox2.pack_start(self.genre_entry,True,True,6)
        vbox2.pack_start(self.year_entry,True,True,6)

        hbox.pack_start(vbox1,True,True,6)
        hbox.pack_start(vbox2,True,True,6)

        vbox.pack_start(hbox,True,True,0)

        commit_button = Gtk.Button.new_with_label("Dodaj")
        commit_button.connect("clicked",self.on_commit_button_clicked)
        vbox.pack_start(commit_button,False,False,0)
        
        return_button = Gtk.Button.new_with_label("Powrót")
        return_button.connect("clicked",self.on_return_button_clicked)
        vbox.pack_start(return_button,False,False,0)
        
        self.add(vbox)

    def on_commit_button_clicked(self, button):
        try:
            if(self.check_data()):
                cur.execute("INSERT INTO MusicLibrary (Author, Title, TracksNr, Tracks, PublishYear, Genre, Rented) VALUES (?,?,?,?,?,?,?)",
                    (self.author_entry.get_text(),self.album_entry.get_text(),int(self.tracknr_entry.get_text()),self.tracks_entry.get_text(),int(self.year_entry.get_text()),self.genre_entry.get_text(),0))
                print("Poprawnie dodano album: {} - {}".format(self.author_entry.get_text(),self.album_entry.get_text()))
                self.destroy()
                win = InitWindow()
                win.connect("delete-event",Gtk.main_quit)
                win.show_all()
            
        except sqlite3.IntegrityError:
            print("Błąd")
    
    def check_data(self):
        self.author_entry.set_text(self.author_entry.get_text().title())
        self.genre_entry.set_text(self.genre_entry.get_text().title())
        tracknr = int(self.tracknr_entry.get_text())
        tracks = len(self.tracks_entry.get_text().split(";"))
        year = int(self.year_entry.get_text())
        if( tracks != tracknr ):
            print("Liczba utworów się nie zgadza.")
            return False
        if( year < 1900 or year > datetime.datetime.now().year):
            print("Podaj prawidłowy rok.")
            return False
        return True

    def on_return_button_clicked(self, button):
        self.destroy()
        win = InitWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

class EditWindow1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(300,200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        label1 = Gtk.Label("Podaj wykonawcę:")
        vbox1.pack_start(label1, True, True, 6)

        label2 = Gtk.Label("Podaj album:")
        vbox1.pack_start(label2, True, True, 6)

        self.author_entry = Gtk.Entry()
        vbox2.pack_start(self.author_entry, True, True, 6)

        self.album_entry = Gtk.Entry()
        vbox2.pack_start(self.album_entry, True, True, 6)

        hbox.pack_start(vbox1, True, True, 6)
        hbox.pack_start(vbox2, True, True, 6)
        vbox.pack_start(hbox, True, True, 6)

        edit_button = Gtk.Button.new_with_label("Edytuj")
        edit_button.connect("clicked",self.on_edit_button_clicked)
        vbox.pack_start(edit_button,False,False,0)

        return_button = Gtk.Button.new_with_label("Powrót")
        return_button.connect("clicked",self.on_return_button_clicked)
        vbox.pack_start(return_button,False,False,0)

        self.add(vbox)

    def on_edit_button_clicked(self, button):
        if(self.check_if_exists(self.author_entry.get_text().rstrip(),self.album_entry.get_text().rstrip())):
            win = EditWindow2(self.author_entry.get_text().rstrip(),self.album_entry.get_text().rstrip())
            self.destroy()
            win.connect("delete-event",Gtk.main_quit)
            win.show_all()
        else:
            print("Nie ma takiej płyty w kolekcji.")

    def check_if_exists(self,author,album):
        cur.execute("""SELECT EXISTS(SELECT 1 FROM MusicLibrary WHERE Author="{}" AND Title="{}" LIMIT 1)""".format(author,album))
        res, = cur.fetchall()[0]
        return(res)

    def on_return_button_clicked(self, button):
        self.destroy()
        win = InitWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

class EditWindow2(Gtk.Window):
    def __init__(self,author,album):
        Gtk.Window.__init__(self, title="Biblioteka muzyczna")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(500,300)
        self.author = author
        self.album  = album

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        label0 = Gtk.Label("Edytowany album:")
        vbox1.pack_start(label0, True, False, 3) 
        label1 = Gtk.Label("Liczba utworów:")
        vbox1.pack_start(label1, True, False, 3)
        label2 = Gtk.Label("Lista utworów (;):")
        vbox1.pack_start(label2, True, False, 3)
        label3 = Gtk.Label("Rok wydania:")
        vbox1.pack_start(label3, True, False, 3)
        label4 = Gtk.Label("Gatunek:")
        vbox1.pack_start(label4, True, False, 3)
        label5 = Gtk.Label("Wypożyczona (0-1):")
        vbox1.pack_start(label5, True, False, 3)

        edited = Gtk.Label("Edited")
        edited.set_markup("<big><b>%s</b></big>" % (author + " - " + album))
        vbox2.pack_start(edited, True, True, 6)

        cur.execute("""SELECT * FROM MusicLibrary WHERE Author="{}" AND Title="{}" LIMIT 1""".format(author,album))
        cur_data = cur.fetchall()[0]

        self.tracknr_entry = Gtk.Entry()
        self.tracknr_entry.set_text(str(cur_data[3]))
        vbox2.pack_start(self.tracknr_entry, True, True, 6)
        self.tracks_entry = Gtk.Entry()
        self.tracks_entry.set_text(cur_data[4])
        vbox2.pack_start(self.tracks_entry, True, True, 6)
        self.year_entry = Gtk.Entry()
        self.year_entry.set_text(str(cur_data[5]))
        vbox2.pack_start(self.year_entry, True, True, 6)
        self.genre_entry = Gtk.Entry()
        self.genre_entry.set_text(cur_data[6])
        vbox2.pack_start(self.genre_entry, True, True, 6)
        self.rented_entry = Gtk.Entry()
        self.rented_entry.set_text(str(cur_data[7]))
        vbox2.pack_start(self.rented_entry, True, True, 6)

        hbox.pack_start(vbox1, True, True, 6)
        hbox.pack_start(vbox2, True, True, 6)
        vbox.pack_start(hbox, True, True, 6)

        edit_button = Gtk.Button.new_with_label("Edytuj")
        edit_button.connect("clicked",self.on_edit_button_clicked)
        vbox.pack_start(edit_button,False,False,0)

        delete_button = Gtk.Button.new_with_label("Usuń")
        delete_button.connect("clicked",self.on_delete_button_clicked)
        vbox.pack_start(delete_button,False,False,0)

        cancel_button = Gtk.Button.new_with_label("Anuluj")
        cancel_button.connect("clicked",self.on_cancel_button_clicked)
        vbox.pack_start(cancel_button,False,False,0)

        self.add(vbox)
    
    def on_edit_button_clicked(self, button):
        if(self.check_data()):
            cur.execute("""UPDATE MusicLibrary SET TracksNr=?, Tracks=?, 
                    PublishYear=?, Genre=?, Rented=? WHERE Author=? AND Title=? """,(
                    int(self.tracknr_entry.get_text()),self.tracks_entry.get_text(),int(self.year_entry.get_text()),self.genre_entry.get_text(),self.rented_entry.get_text(),self.author,self.album))
            print("Poprawnie edytowano album: {} - {}".format(self.author,self.album))
            self.destroy()
            win = InitWindow()
            win.connect("delete-event",Gtk.main_quit)
            win.show_all()

    def check_data(self):
        self.genre_entry.set_text(self.genre_entry.get_text().capitalize())
        tracknr = int(self.tracknr_entry.get_text())
        tracks = len(self.tracks_entry.get_text().split(";"))
        year = int(self.year_entry.get_text())
        rented = int(self.rented_entry.get_text())
        if( rented != 0 and rented != 1):
            print("Podaj wartość 0 albo 1.")
            return False
        if( tracks != tracknr ):
            print("Liczba utworów się nie zgadza.")
            return False
        if( year < 1900 or year > datetime.datetime.now().year):
            print("Podaj prawidłowy rok.")
            return False
        return True

    def on_delete_button_clicked(self, button):
        cur.execute("""DELETE FROM MusicLibrary WHERE Author=? AND Title=?""",(self.author,self.album))
        print("Poprawnie usunięto album: {} - {}".format(self.author,self.album))
        self.destroy()
        win = InitWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

    def on_cancel_button_clicked(self, button):
        self.destroy()
        win = InitWindow()
        win.connect("delete-event",Gtk.main_quit)
        win.show_all()

init()
win = InitWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()

cur.close()
db.close()