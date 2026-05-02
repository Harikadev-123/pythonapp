# File: bus_booking_app.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import random

class BusBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BusEase - Premium Bus Booking")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f4f8')
        
        # Set custom styles
        self.setup_styles()
        
        # Bus database
        self.buses = self.load_buses()
        self.selected_bus = None
        self.selected_seats = []
        self.current_user = None
        
        # Current frame reference
        self.current_frame = None
        
        # Show login/home screen
        self.show_main_screen()
    
    def setup_styles(self):
        """Setup color scheme and styles"""
        self.colors = {
            'primary': '#1e88e5',
            'primary_dark': '#1565c0',
            'secondary': '#ff6d00',
            'success': '#43a047',
            'danger': '#e53935',
            'warning': '#fb8c00',
            'light': '#ffffff',
            'dark': '#37474f',
            'gray': '#78909c',
            'bg': '#f0f4f8'
        }
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Title.TLabel', font=('Helvetica', 24, 'bold'), 
                       foreground=self.colors['primary'])
        style.configure('Heading.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('Normal.TLabel', font=('Helvetica', 10))
        
        style.configure('Primary.TButton', font=('Helvetica', 10, 'bold'),
                       background=self.colors['primary'], foreground='white')
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_dark'])])
    
    def load_buses(self):
        """Load bus data"""
        buses = [
            {
                'id': 1,
                'name': 'Royal Express',
                'from': 'New York',
                'to': 'Boston',
                'date': '2024-12-25',
                'time': '08:00 AM',
                'duration': '4h 30m',
                'price': 45,
                'amenities': ['AC', 'WiFi', 'Snacks', 'USB Ports'],
                'seats': self.generate_seats(40)
            },
            {
                'id': 2,
                'name': 'CityLink Travels',
                'from': 'New York',
                'to': 'Washington DC',
                'date': '2024-12-25',
                'time': '09:30 AM',
                'duration': '5h',
                'price': 55,
                'amenities': ['AC', 'WiFi', 'Water Bottle', 'Entertainment'],
                'seats': self.generate_seats(40)
            },
            {
                'id': 3,
                'name': 'Coastline Cruiser',
                'from': 'Boston',
                'to': 'Philadelphia',
                'date': '2024-12-25',
                'time': '10:00 AM',
                'duration': '6h',
                'price': 50,
                'amenities': ['AC', 'Restroom', 'Refreshments', 'Charging Points'],
                'seats': self.generate_seats(40)
            },
            {
                'id': 4,
                'name': 'Mountain Express',
                'from': 'New York',
                'to': 'Chicago',
                'date': '2024-12-26',
                'time': '11:30 PM',
                'duration': '12h',
                'price': 85,
                'amenities': ['Sleeper', 'AC', 'WiFi', 'Meal', 'Blanket'],
                'seats': self.generate_seats(40)
            },
            {
                'id': 5,
                'name': 'Sunshine Travels',
                'from': 'Miami',
                'to': 'Orlando',
                'date': '2024-12-25',
                'time': '07:00 AM',
                'duration': '3h 30m',
                'price': 35,
                'amenities': ['AC', 'WiFi', 'Snacks'],
                'seats': self.generate_seats(40)
            },
            {
                'id': 6,
                'name': 'Golden State Tours',
                'from': 'Los Angeles',
                'to': 'San Francisco',
                'date': '2024-12-27',
                'time': '08:30 PM',
                'duration': '6h',
                'price': 65,
                'amenities': ['Luxury Seats', 'WiFi', 'Meal', 'Entertainment'],
                'seats': self.generate_seats(40)
            }
        ]
        return buses
    
    def generate_seats(self, total_seats):
        """Generate seat availability (random booking for demo)"""
        seats = []
        for i in range(1, total_seats + 1):
            seats.append({
                'number': i,
                'status': random.choice(['available', 'available', 'available', 'booked'])  # 75% available
            })
        return seats
    
    def clear_frame(self):
        """Clear the current frame"""
        if self.current_frame:
            self.current_frame.destroy()
    
    def show_main_screen(self):
        """Display main screen with bus search"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = tk.Frame(self.current_frame, bg=self.colors['primary'], height=120)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🚌 BusEase", 
                        font=('Helvetica', 32, 'bold'),
                        bg=self.colors['primary'], fg='white')
        title.pack(pady=30)
        
        subtitle = tk.Label(header, text="Your Comfortable Journey Starts Here",
                         font=('Helvetica', 12),
                         bg=self.colors['primary'], fg='white')
        subtitle.pack()
        
        # Search Frame
        search_frame = tk.Frame(self.current_frame, bg=self.colors['light'],
                               relief=tk.RAISED, bd=1)
        search_frame.pack(pady=40, padx=40, fill=tk.X)
        
        tk.Label(search_frame, text="Search Buses", font=('Helvetica', 18, 'bold'),
                bg=self.colors['light'], fg=self.colors['dark']).grid(row=0, column=0, 
                columnspan=4, pady=20, padx=20, sticky='w')
        
        # Search inputs
        tk.Label(search_frame, text="From:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.from_city = ttk.Combobox(search_frame, values=self.get_unique_cities('from'),
                                     font=('Helvetica', 11), width=20)
        self.from_city.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(search_frame, text="To:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=1, column=2, padx=10, pady=10, sticky='w')
        self.to_city = ttk.Combobox(search_frame, values=self.get_unique_cities('to'),
                                   font=('Helvetica', 11), width=20)
        self.to_city.grid(row=1, column=3, padx=10, pady=10)
        
        tk.Label(search_frame, text="Travel Date:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.date_entry = ttk.Combobox(search_frame, values=self.get_dates(),
                                      font=('Helvetica', 11), width=20)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Search button
        search_btn = tk.Button(search_frame, text="🔍 Search Buses", 
                              command=self.search_buses,
                              bg=self.colors['primary'], fg='white',
                              font=('Helvetica', 12, 'bold'),
                              padx=30, pady=10, cursor='hand2')
        search_btn.grid(row=2, column=3, padx=10, pady=20)
        
        # Results section
        self.results_frame = tk.Frame(self.current_frame, bg=self.colors['bg'])
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
    
    def get_unique_cities(self, city_type):
        """Get unique cities from bus routes"""
        cities = set()
        for bus in self.buses:
            cities.add(bus[city_type])
        return sorted(list(cities))
    
    def get_dates(self):
        """Generate next 7 days dates"""
        dates = []
        for i in range(7):
            date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
            dates.append(date)
        return dates
    
    def search_buses(self):
        """Search for available buses"""
        from_city = self.from_city.get()
        to_city = self.to_city.get()
        travel_date = self.date_entry.get()
        
        if not from_city or not to_city or not travel_date:
            messagebox.showwarning("Missing Info", "Please fill all search fields")
            return
        
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Find matching buses
        matching_buses = []
        for bus in self.buses:
            if bus['from'] == from_city and bus['to'] == to_city and bus['date'] == travel_date:
                matching_buses.append(bus)
        
        if not matching_buses:
            no_buses = tk.Label(self.results_frame, 
                               text="❌ No buses found for this route",
                               font=('Helvetica', 14), bg=self.colors['bg'],
                               fg=self.colors['danger'])
            no_buses.pack(pady=50)
            return
        
        # Display results
        results_title = tk.Label(self.results_frame, 
                                text=f"🎫 Found {len(matching_buses)} buses",
                                font=('Helvetica', 16, 'bold'),
                                bg=self.colors['bg'], fg=self.colors['primary'])
        results_title.pack(anchor='w', pady=10)
        
        for bus in matching_buses:
            self.create_bus_card(bus)
    
    def create_bus_card(self, bus):
        """Create a bus card widget"""
        card = tk.Frame(self.results_frame, bg=self.colors['light'],
                       relief=tk.RAISED, bd=1)
        card.pack(fill=tk.X, pady=10, padx=5)
        
        # Bus info
        info_frame = tk.Frame(card, bg=self.colors['light'])
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Bus name and amenities
        tk.Label(info_frame, text=f"🚍 {bus['name']}", 
                font=('Helvetica', 14, 'bold'),
                bg=self.colors['light'], fg=self.colors['dark']).pack(anchor='w')
        
        amenities_text = " • ".join(bus['amenities'][:3])
        tk.Label(info_frame, text=f"✨ {amenities_text}",
                font=('Helvetica', 9), bg=self.colors['light'],
                fg=self.colors['gray']).pack(anchor='w', pady=5)
        
        # Route details
        route_frame = tk.Frame(info_frame, bg=self.colors['light'])
        route_frame.pack(fill=tk.X, pady=10)
        
        # Departure
        dept_frame = tk.Frame(route_frame, bg=self.colors['light'])
        dept_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(dept_frame, text=f"Departure", font=('Helvetica', 8),
                bg=self.colors['light'], fg=self.colors['gray']).pack()
        tk.Label(dept_frame, text=bus['time'], font=('Helvetica', 14, 'bold'),
                bg=self.colors['light'], fg=self.colors['dark']).pack()
        tk.Label(dept_frame, text=bus['from'], font=('Helvetica', 10),
                bg=self.colors['light'], fg=self.colors['gray']).pack()
        
        # Arrow
        tk.Label(route_frame, text="→", font=('Helvetica', 20),
                bg=self.colors['light'], fg=self.colors['primary']).pack(side=tk.LEFT, padx=30)
        
        # Arrival
        arrival_frame = tk.Frame(route_frame, bg=self.colors['light'])
        arrival_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(arrival_frame, text=f"Duration", font=('Helvetica', 8),
                bg=self.colors['light'], fg=self.colors['gray']).pack()
        tk.Label(arrival_frame, text=bus['duration'], font=('Helvetica', 14, 'bold'),
                bg=self.colors['light'], fg=self.colors['dark']).pack()
        tk.Label(arrival_frame, text=bus['to'], font=('Helvetica', 10),
                bg=self.colors['light'], fg=self.colors['gray']).pack()
        
        # Price and booking
        price_frame = tk.Frame(card, bg=self.colors['light'])
        price_frame.pack(side=tk.RIGHT, padx=20, pady=15)
        
        tk.Label(price_frame, text=f"₹{bus['price']}", 
                font=('Helvetica', 20, 'bold'),
                bg=self.colors['light'], fg=self.colors['secondary']).pack()
        
        tk.Label(price_frame, text="per seat", font=('Helvetica', 9),
                bg=self.colors['light'], fg=self.colors['gray']).pack()
        
        available_seats = len([s for s in bus['seats'] if s['status'] == 'available'])
        tk.Label(price_frame, text=f"{available_seats} seats left",
                font=('Helvetica', 9), bg=self.colors['light'],
                fg=self.colors['success']).pack(pady=5)
        
        select_btn = tk.Button(price_frame, text="Select Bus", 
                              command=lambda b=bus: self.select_bus(b),
                              bg=self.colors['primary'], fg='white',
                              font=('Helvetica', 10, 'bold'),
                              padx=20, pady=5, cursor='hand2')
        select_btn.pack(pady=5)
    
    def select_bus(self, bus):
        """Select a bus and show seat selection"""
        self.selected_bus = bus
        self.selected_seats = []
        self.show_seat_selection()
    
    def show_seat_selection(self):
        """Display seat selection screen"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = tk.Frame(self.current_frame, bg=self.colors['primary'], height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="🎫 Select Your Seats", 
                font=('Helvetica', 24, 'bold'),
                bg=self.colors['primary'], fg='white').pack(pady=30)
        
        # Main content
        main_frame = tk.Frame(self.current_frame, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Bus info sidebar
        info_frame = tk.Frame(main_frame, bg=self.colors['light'], 
                             relief=tk.RAISED, bd=1, width=300)
        info_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        info_frame.pack_propagate(False)
        
        # Bus details
        tk.Label(info_frame, text=f"🚍 {self.selected_bus['name']}",
                font=('Helvetica', 16, 'bold'), bg=self.colors['light'],
                fg=self.colors['dark']).pack(pady=20)
        
        tk.Label(info_frame, text=f"From: {self.selected_bus['from']}",
                font=('Helvetica', 11), bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Label(info_frame, text=f"To: {self.selected_bus['to']}",
                font=('Helvetica', 11), bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Label(info_frame, text=f"Date: {self.selected_bus['date']}",
                font=('Helvetica', 11), bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Label(info_frame, text=f"Time: {self.selected_bus['time']}",
                font=('Helvetica', 11), bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Label(info_frame, text=f"Duration: {self.selected_bus['duration']}",
                font=('Helvetica', 11), bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        
        tk.Label(info_frame, text=f"Price: ₹{self.selected_bus['price']}/seat",
                font=('Helvetica', 13, 'bold'), bg=self.colors['light'],
                fg=self.colors['secondary']).pack(anchor='w', padx=20, pady=15)
        
        # Amenities
        tk.Label(info_frame, text="Amenities:", font=('Helvetica', 11, 'bold'),
                bg=self.colors['light']).pack(anchor='w', padx=20, pady=(20, 5))
        
        for amenity in self.selected_bus['amenities']:
            tk.Label(info_frame, text=f"✓ {amenity}", font=('Helvetica', 10),
                    bg=self.colors['light'], fg=self.colors['gray']).pack(anchor='w', padx=30, pady=2)
        
        # Seat selection area
        seat_frame = tk.Frame(main_frame, bg=self.colors['light'], relief=tk.RAISED, bd=1)
        seat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Legend
        legend_frame = tk.Frame(seat_frame, bg=self.colors['light'])
        legend_frame.pack(pady=20)
        
        tk.Label(legend_frame, text="🟢 Available", font=('Helvetica', 10),
                bg=self.colors['light'], fg='green').pack(side=tk.LEFT, padx=10)
        tk.Label(legend_frame, text="🔵 Selected", font=('Helvetica', 10),
                bg=self.colors['light'], fg='blue').pack(side=tk.LEFT, padx=10)
        tk.Label(legend_frame, text="🔴 Booked", font=('Helvetica', 10),
                bg=self.colors['light'], fg='red').pack(side=tk.LEFT, padx=10)
        
        # Bus layout header
        tk.Label(seat_frame, text="BUS LAYOUT", font=('Helvetica', 12, 'bold'),
                bg=self.colors['light'], fg=self.colors['primary']).pack(pady=10)
        
        # Driver section
        driver_frame = tk.Frame(seat_frame, bg='#e0e0e0', height=40)
        driver_frame.pack(fill=tk.X, padx=50, pady=5)
        tk.Label(driver_frame, text="🚌 DRIVER", font=('Helvetica', 10, 'bold'),
                bg='#e0e0e0').pack()
        
        # Seats grid
        seats_grid = tk.Frame(seat_frame, bg=self.colors['light'])
        seats_grid.pack(pady=20, padx=40)
        
        self.seat_buttons = {}
        seats_per_row = 4
        for i, seat in enumerate(self.selected_bus['seats']):
            row = i // seats_per_row
            col = i % seats_per_row
            
            # Add aisle after 2 seats
            if col == 2:
                aisle = tk.Label(seats_grid, text="    ", bg=self.colors['light'])
                aisle.grid(row=row, column=col, padx=5, pady=2)
                col += 1
            
            color = 'green' if seat['status'] == 'available' else 'red'
            if seat['status'] == 'available':
                btn = tk.Button(seats_grid, text=f"{seat['number']}",
                              bg='#4caf50', fg='white',
                              font=('Helvetica', 9, 'bold'),
                              width=6, height=2,
                              command=lambda s=seat: self.toggle_seat(s))
                self.seat_buttons[seat['number']] = btn
            else:
                btn = tk.Button(seats_grid, text=f"{seat['number']}",
                              bg='#f44336', fg='white',
                              font=('Helvetica', 9, 'bold'),
                              width=6, height=2, state='disabled')
            
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Selection summary
        summary_frame = tk.Frame(seat_frame, bg=self.colors['light'])
        summary_frame.pack(fill=tk.X, pady=20)
        
        self.selection_label = tk.Label(summary_frame, text="Selected seats: None",
                                       font=('Helvetica', 11), bg=self.colors['light'],
                                       fg=self.colors['primary'])
        self.selection_label.pack(pady=5)
        
        self.total_label = tk.Label(summary_frame, text="Total: ₹0",
                                   font=('Helvetica', 14, 'bold'),
                                   bg=self.colors['light'], fg=self.colors['secondary'])
        self.total_label.pack(pady=5)
        
        # Buttons
        button_frame = tk.Frame(summary_frame, bg=self.colors['light'])
        button_frame.pack(pady=20)
        
        back_btn = tk.Button(button_frame, text="← Back to Search",
                            command=self.show_main_screen,
                            bg=self.colors['gray'], fg='white',
                            font=('Helvetica', 11), padx=20, pady=10)
        back_btn.pack(side=tk.LEFT, padx=10)
        
        proceed_btn = tk.Button(button_frame, text="Proceed to Payment →",
                               command=self.payment_screen,
                               bg=self.colors['secondary'], fg='white',
                               font=('Helvetica', 11, 'bold'), padx=20, pady=10)
        proceed_btn.pack(side=tk.LEFT, padx=10)
    
    def toggle_seat(self, seat):
        """Toggle seat selection"""
        if seat['status'] == 'available':
            if seat['number'] in self.selected_seats:
                self.selected_seats.remove(seat['number'])
                seat['status'] = 'available'
                self.seat_buttons[seat['number']].config(bg='#4caf50')
            else:
                self.selected_seats.append(seat['number'])
                seat['status'] = 'selected'
                self.seat_buttons[seat['number']].config(bg='#2196f3')
            
            # Update summary
            total = len(self.selected_seats) * self.selected_bus['price']
            seats_text = ', '.join(map(str, sorted(self.selected_seats))) if self.selected_seats else 'None'
            self.selection_label.config(text=f"Selected seats: {seats_text}")
            self.total_label.config(text=f"Total: ₹{total}")
    
    def payment_screen(self):
        """Show payment screen"""
        if not self.selected_seats:
            messagebox.showwarning("No Seats", "Please select at least one seat")
            return
        
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = tk.Frame(self.current_frame, bg=self.colors['primary'], height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="💰 Payment Details", 
                font=('Helvetica', 24, 'bold'),
                bg=self.colors['primary'], fg='white').pack(pady=30)
        
        # Main content
        main_frame = tk.Frame(self.current_frame, bg=self.colors['light'],
                             relief=tk.RAISED, bd=1)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=100, pady=40)
        
        # Booking summary
        summary_frame = tk.LabelFrame(main_frame, text="Booking Summary",
                                     font=('Helvetica', 12, 'bold'),
                                     bg=self.colors['light'], fg=self.colors['dark'])
        summary_frame.pack(fill=tk.X, padx=30, pady=20)
        
        total_amount = len(self.selected_seats) * self.selected_bus['price']
        
        details = f"""
        Bus: {self.selected_bus['name']}
        Route: {self.selected_bus['from']} → {self.selected_bus['to']}
        Date: {self.selected_bus['date']} at {self.selected_bus['time']}
        Seats: {', '.join(map(str, sorted(self.selected_seats)))}
        Tickets: {len(self.selected_seats)}
        Amount: ₹{total_amount}
        """
        
        tk.Label(summary_frame, text=details, font=('Helvetica', 11),
                bg=self.colors['light'], justify=tk.LEFT).pack(anchor='w', padx=20, pady=15)
        
        # Passenger details
        passenger_frame = tk.LabelFrame(main_frame, text="Passenger Details",
                                       font=('Helvetica', 12, 'bold'),
                                       bg=self.colors['light'], fg=self.colors['dark'])
        passenger_frame.pack(fill=tk.X, padx=30, pady=20)
        
        form_frame = tk.Frame(passenger_frame, bg=self.colors['light'])
        form_frame.pack(padx=20, pady=15)
        
        # Name
        tk.Label(form_frame, text="Full Name:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=0, column=0, sticky='w', pady=5)
        self.name_entry = tk.Entry(form_frame, font=('Helvetica', 11), width=30)
        self.name_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Email
        tk.Label(form_frame, text="Email:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=1, column=0, sticky='w', pady=5)
        self.email_entry = tk.Entry(form_frame, font=('Helvetica', 11), width=30)
        self.email_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Phone
        tk.Label(form_frame, text="Phone:", font=('Helvetica', 11),
                bg=self.colors['light']).grid(row=2, column=0, sticky='w', pady=5)
        self.phone_entry = tk.Entry(form_frame, font=('Helvetica', 11), width=30)
        self.phone_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Payment method
        payment_frame = tk.LabelFrame(main_frame, text="Payment Method",
                                     font=('Helvetica', 12, 'bold'),
                                     bg=self.colors['light'], fg=self.colors['dark'])
        payment_frame.pack(fill=tk.X, padx=30, pady=20)
        
        self.payment_var = tk.StringVar(value="card")
        tk.Radiobutton(payment_frame, text="💳 Credit/Debit Card", variable=self.payment_var,
                      value="card", bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Radiobutton(payment_frame, text="🏦 Net Banking", variable=self.payment_var,
                      value="netbanking", bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        tk.Radiobutton(payment_frame, text="📱 UPI", variable=self.payment_var,
                      value="upi", bg=self.colors['light']).pack(anchor='w', padx=20, pady=5)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors['light'])
        button_frame.pack(pady=20)
        
        back_btn = tk.Button(button_frame, text="← Back to Seats",
                            command=lambda: self.select_bus(self.selected_bus),
                            bg=self.colors['gray'], fg='white',
                            font=('Helvetica', 11), padx=20, pady=10)
        back_btn.pack(side=tk.LEFT, padx=10)
        
        pay_btn = tk.Button(button_frame, text=f"Pay ₹{total_amount} →",
                           command=self.confirm_booking,
                           bg=self.colors['success'], fg='white',
                           font=('Helvetica', 11, 'bold'), padx=20, pady=10)
        pay_btn.pack(side=tk.LEFT, padx=10)
    
    def confirm_booking(self):
        """Confirm booking and show success message"""
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        
        if not name or not email or not phone:
            messagebox.showwarning("Missing Info", "Please fill all passenger details")
            return
        
        if '@' not in email or '.' not in email:
            messagebox.showwarning("Invalid Email", "Please enter a valid email address")
            return
        
        total_amount = len(self.selected_seats) * self.selected_bus['price']
        
        # Mark seats as booked
        for seat in self.selected_bus['seats']:
            if seat['number'] in self.selected_seats:
                seat['status'] = 'booked'
        
        # Show success message
        success_msg = f"""
✅ Booking Confirmed!

Dear {name},

Your booking has been successfully confirmed.

📋 Booking Details:
• Bus: {self.selected_bus['name']}
• Route: {self.selected_bus['from']} → {self.selected_bus['to']}
• Date: {self.selected_bus['date']} at {self.selected_bus['time']}
• Seats: {', '.join(map(str, sorted(self.selected_seats)))}
• Total Paid: ₹{total_amount}

📧 Confirmation sent to: {email}
📱 Reference ID: BUS{random.randint(10000, 99999)}

Thank you for choosing BusEase! 🚌
        """
        
        messagebox.showinfo("Booking Successful", success_msg)
        self.show_main_screen()

def main():
    root = tk.Tk()
    app = BusBookingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
