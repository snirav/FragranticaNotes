import Tkinter as tk
import tkMessageBox
from FragCrawlThreadCreation import *

class fragranceCrawler(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=400,
                          height=300)
        # Set the title
        self.master.title('Perfume Crawler')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()
 
        # Fill the  Website List
        self.webSiteList=['http://www.fragrantica.com']
        # Fill the designers List
        self.designerEntries=['Azzaro',
                            'Bond-No-9',
                            'Boucheron',
                            'Britney-Spears',
                            'Burberry',
                            'Bvlgari',
                            'Cacharel',
                            'Calvin-Klein',
                            'Carolina-Herrera',
                            'Cartier',
                            'Chanel',
                            'Creed',
                            'Davidoff',
                            'Dior',
                            'Dolce%26Gabbana',
                            'Donna-Karan',
                            'Elizabeth-Arden',
                            'Escada',
                            'Estee-Lauder',
                            'Giorgio-Armani',
                            'Givenchy',
                            'Gucci',
                            'Guerlain',
                            'Guy-Laroche',
                            'Gwen-Stefani',
                            'Hermes',
                            'Hugo-Boss',
                            'Jean-Paul-Gaultier',
                            'Jennifer-Lopez',
                            'Kenzo',
                            'Lacoste',
                            'Lancome',
                            'Liz-Claiborne',
                            'Mariah-Carey',
                            'Moschino',
                            'Nina-Ricci',
                            'Paco-Rabanne',
                            'Paris-Hilton',
                            'Perry-Ellis',
                            'Prada',
                            'Ralph-Lauren',
                            'Rochas',
                            'Thierry-Mugler',
                            'Tommy-Hilfiger',
                            'Vera-Wang',
                            'Versace',
                            'Victoria%60s-Secret',
                            'Yves-Saint-Laurent']
        # Website Selection Menu
        self.defaultWebsite = tk.StringVar()
        self.defaultWebsite.set('Please Select the Websites to crawl')
        self.websiteDropdown = tk.OptionMenu(self,
                                      self.defaultWebsite, *self.webSiteList)
                                     
        # Designer Selection Menu
        self.defaultDesigner = tk.StringVar()
        self.defaultDesigner.set('Please Select the sites to crawl')
        self.designerList = tk.OptionMenu(self,
                                      self.defaultDesigner, "All",
                                      *self.designerEntries)
 
        # Declaring the buttons and linking the functions
        self.textBox=tk.Text(xscrollcommand=set(), yscrollcommand=set(), height=5,width=5)
        
        self.crawl_button = tk.Button(self,
                                   text='Crawl Designer',
                                   command=self.initiateCrawl, height=2, width=15)

        # Put the controls on the form
        
        self.websiteDropdown.pack(fill=tk.X, side=tk.TOP)
        self.designerList.pack(fill=tk.X, side=tk.TOP)
        self.crawl_button.pack(fill=tk.X, side=tk.TOP)
        self.textBox.pack(fill=tk.X, side=tk.TOP)
        
    # Crawl handling routine
    def initiateCrawl(self):                     
        crawl(self.defaultWebsite.get().title().lower(), self.defaultDesigner.get().title(), self.designerEntries)
        tkMessageBox.showinfo("Crawling Status", "Crawling Completed Successfully!!")
        self.textBox.insert('1.0', "Crawling Completed Successfully!!","a")
     
    def run(self):
        ''' Run the app '''        
        self.mainloop()
 
app = fragranceCrawler(tk.Tk())
app.run()
