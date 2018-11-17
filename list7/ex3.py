from gi.repository import Gtk, GObject

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Minutnik")
        self.set_default_size(300, 300)
        self.set_border_width(10)
        self.seconds_cnt = 0
        self.counting = False
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        self.time_label = Gtk.Label("Time")
        self.time_label.set_markup("<big><b>0:00</b></big>")
        vbox.pack_start(self.time_label, True, True, 0)
        
        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)
        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        
        set_time_label = Gtk.Label("Ustaw czas (mm:ss):")
        vbox1.pack_start(set_time_label, True, True, 0)
        
        self.time_entry = Gtk.Entry()
        vbox2.pack_start(self.time_entry, True, True, 0)
        
        meals_list = Gtk.ListStore(str)
        meals = ["Jajka na twardo", "Jajka na miękko", "Ryż", "Makaron", "Ziemniaki"]
        for meal in meals:
            meals_list.append([meal])

        choose_meal_label = Gtk.Label("albo wybierz z listy:")
        vbox1.pack_start(choose_meal_label, True, True, 0)
        
        meal_combo = Gtk.ComboBox.new_with_model(meals_list)
        renderer_text = Gtk.CellRendererText()
        meal_combo.pack_start(renderer_text, True)
        meal_combo.add_attribute(renderer_text, "text", 0)
        meal_combo.connect("changed", self.on_meal_combo_changed)
        vbox2.pack_start(meal_combo, True, True, 0)
        
        start_button = Gtk.Button.new_with_label("Start")
        start_button.connect("clicked", self.on_start_button_clicked)
        hbox1.pack_start(start_button, True, True, 0)
        
        stop_button = Gtk.Button.new_with_label("Stop")
        stop_button.connect("clicked", self.on_stop_button_clicked)
        hbox1.pack_start(stop_button, True, True, 0)
        
        hbox.pack_start(vbox1, True, True, 0) 
        hbox.pack_start(vbox2, True, True, 0)
        vbox.pack_start(hbox, True, True, 0)
        vbox.pack_start(hbox1, True, True, 0)
        self.add(vbox)

    def sec_to_min(self, sec):
        return (sec // 60, sec % 60)
        
    def min_to_sec(self, _min, sec):
        return 60 * _min + sec
        
    def on_start_button_clicked(self, button):
        if self.counting:
            return
        start_values = self.time_entry.get_text().split(':')
        _min = int(start_values[0])
        sec  = int(start_values[1])
        sec_text = str(sec)
        if sec < 10: 
            sec_text = "0" + sec_text
        self.time_label.set_markup("<big><b>" + str(_min) + ":" + sec_text + "</b></big>")
        self.progressbar.set_fraction(0)
        self.seconds_cnt = self.min_to_sec(_min, sec)
        self.seconds_max = self.seconds_cnt
        self.counting = True
        self.start_timer()
        
    def on_stop_button_clicked(self, button):
        self.counting = False
        self.seconds_cnt = 0
        self.stopped = True
    
    def on_meal_combo_changed(self, combo):
        _iter = combo.get_active_iter()
        if _iter != None:
            model = combo.get_model()
            meal = model[_iter][0]
            time_min = 0
            if meal == "Jajka na twardo": 
                time_min = 7
            if meal == "Jajka na miękko": 
                time_min = 4
            if meal == "Ryż": 
                time_min = 14
            if meal == "Makaron": 
                time_min = 10
            if meal == "Ziemniaki": 
                time_min = 20
            self.time_entry.set_text(str(time_min) + ":00")
            
    def start_timer(self):
        self.g = GObject.timeout_add(1000, self.timer)
        self.stopped = False
    
    def timer(self):
        if self.seconds_cnt > 0:
            self.seconds_cnt -= 1
            self.progressbar.set_fraction((self.seconds_max - self.seconds_cnt)/self.seconds_max)
            _min, sec = self.sec_to_min(self.seconds_cnt)
            sec_text = str(sec)
            if sec < 10: 
                sec_text = "0" + sec_text
            self.time_label.set_markup("<big><b>" + str(_min) + ":" + sec_text + "</b></big>")
            return True    
        else:
            self.counting = False
            if not self.stopped:
                self.time_label.set_markup("<big><b>Koniec!</b></big>")
                self.progressbar.set_fraction(1)
            return False
        
win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
