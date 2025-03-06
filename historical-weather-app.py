import customtkinter as ctk
from data_cleaner import dailyweather
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WeatherApp:
    def __init__(self):
        #initialise application window 
        self.app=ctk.CTk()
        self.app.title("Hong Kong Historical Weather Check")
        self.app.geometry("1000x800")

        #dictionary to store checkboxes and their dates
        self.checkboxes={}
        #to close window 
        self.app.protocol("WM_DELETE_WINDOW", self.on_close)
        self.dates=sorted(dailyweather.keys())
        self.first_date=self.dates[0]
        self.last_date=self.dates[-1 ]


        #create and layout UI widgets 
        self.create_widgets()
    def create_widgets(self): 
        """Layout of the widgets."""
        #instruction label
        ctk.CTkLabel(self.app, text=f"Input a date between {self.first_date} to {self.last_date}", font=("Courier New", 20)).pack(pady=20) 


        #frame to hold data entry fields 
        date_frame = ctk.CTkFrame(self.app)
        date_frame.pack(pady=20)    
        
        """Input for dates"""
        #day input 
        ctk.CTkLabel(date_frame, text="Day:").grid(row=0, column=0, padx=5, pady=5)
        self.day_entry = ctk.CTkOptionMenu(date_frame, values=[str(i) for i in range(1, 32)])
        self.day_entry.grid(row=0, column=1, padx=5, pady=5)

        #month input
        ctk.CTkLabel(date_frame, text="Month:").grid(row=0, column=2, padx=5, pady=5)
        self.month_entry = ctk.CTkOptionMenu(date_frame, values=[str(i) for i in range(1, 13)])
        self.month_entry.grid(row=0, column=3, padx=5, pady=5)

        #year input         
        ctk.CTkLabel(date_frame, text="Year:").grid(row=0, column=4, padx=5, pady=5)            
        self.year_entry = ctk.CTkOptionMenu(date_frame, values=[str(i) for i in range(2020, 2026)])
        self.year_entry.grid(row=0, column=5, padx=5, pady=5)
        #Label
        self.date_label=ctk.CTkLabel(self.app, text="Weather Data: ")
        self.date_label.pack()

        #scrollable frame to display weather data
        self.scrollframe = ctk.CTkScrollableFrame(self.app, height=400, width=800)
        self.scrollframe.pack(pady=10, padx=20, fill="both", expand=True)

        #button to confirm selected date
        confirm_button=ctk.CTkButton(self.app, text="Confirm", command=lambda: self.display_data(self.get_date()))
        confirm_button.pack(pady=10)

        #button to graph
        graph_button=ctk.CTkButton(self.app, text="Graph", command=self.graph_selected_dates)
        graph_button.pack(pady=10)
    def on_close(self):
        """Handle the window close event."""
        print("Closing application...")
        self.app.quit()
    

    def get_date(self):
        """Get the date from the user input."""
        day=self.day_entry.get()
        month=self.month_entry.get()
        year=self.year_entry.get()
        return datetime(int(year), int(month), int(day)).date()
    
    def display_data(self, chosen_date):
        """Display the weather data for the selected date."""
        try:
            weather_on_day=dailyweather[chosen_date]
            weather_info = (
            f"Temperature: {weather_on_day['temperature']}°C\n"
            f"Precipitation: {weather_on_day['precipitation']}mm\n"
            f"Wind Speed: {weather_on_day['wind_speed']}m/s\n"
            f"Humidity: {weather_on_day['humidity']}%\n"
            "----------------------------\n"
            )
            #frame for each weather info and checkbox 
            weather_info_frame = ctk.CTkFrame(self.scrollframe)
            weather_info_frame.pack(fill="x", pady=5, padx=10)
            
            # Add a label with the weather info
            date_label = ctk.CTkLabel(weather_info_frame, text=f"Date:\n {chosen_date}", font=("Helvetica", 20, "bold"), text_color="light blue")
            date_label.pack(side="left", pady=(0,30))
            info_label = ctk.CTkLabel(weather_info_frame, text=weather_info, font=("Helvetica", 20), justify="left")
            info_label.pack(side="left")
            checkbox = ctk.CTkCheckBox(weather_info_frame, text="", width=10)
            checkbox.pack(side="left", padx=20, pady=(0,25))
            self.checkboxes[chosen_date]=checkbox #to link checkbox to the relevant date
        except KeyError:
            ctk.CTkLabel(self.scrollframe, text=f"Weather data not available for the {chosen_date} date.").pack()
        # Prepare data for graphing
 
    def graph_selected_dates(self):
        selected_dates=[date for date, checkbox in self.checkboxes.items() if checkbox.get()==True]
        if not selected_dates:
            ctk.CTkLabel(self.scrollframe, text="No dates selected for graphing")
            return
        dates=[]
        temperatures = []
        precipitations = []
        wind_speeds = []
        humidities = []
        for date in selected_dates:
            dates.append(date)
            weather_on_day=dailyweather[date]
            temperatures.append(weather_on_day['temperature'])
            precipitations.append(weather_on_day['precipitation'])
            wind_speeds.append(weather_on_day['wind_speed'])
            humidities.append(weather_on_day['humidity'])
            print(wind_speeds)
        #the graph itself 
        fig, axs=plt.subplots(nrows=2,ncols=2, figsize=(10,8))
        plt.subplots_adjust(hspace=0.3)
        axs=axs.flat
        for ax, data, title, color in zip(
            axs, [temperatures, precipitations, wind_speeds, humidities],
            ["Temperature", "Precipitations", "Wind speed (m/s)", "Humidity (%)"],
            ["red", "blue", "green", "purple"]
        ):
            formatted_dates=[date.strftime("%m/%y") for date in dates]
            ax.plot(dates, data, color=color, marker='o')
            ax.set_xticks(dates)
            ax.set_xticklabels(formatted_dates, rotation=45)
            ax.set_title(title)
            ax.grid(True)
        
        #window to show graph
        self.graph_window=ctk.CTkToplevel(self.app)
        self.graph_window.wm_transient(self.app) #transient window for the main app window so it shows up
        self.graph_window.title("Weather Graph")
        self.graph_window.geometry("1000x800")
        self.graph_window.focus_force()
        #embed the figure in tkinter
        canvas= FigureCanvasTkAgg(fig, master=self.graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both",expand=True)
        

    def run_self(self): 
        self.app.mainloop()


#running the app

weather_app = WeatherApp()
weather_app.run_self()
            
