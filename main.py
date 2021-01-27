from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp

item = """

TwoLineIconListItem:
	text: "Sj Bros"
	secondary_text: "Contact"
	on_press: app.press(*args)
				
	ImageLeftWidget:
		source: "result.png"

"""

class Tab(FloatLayout, MDTabsBase):
	'''Class implementing content for a tab.'''
		
		

class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Green"
		self.title = "Whatsapp"
		self.root = Builder.load_file("design.kv")
		
	
	def inspect(self, text):
		print(self.root.ids.main_tab.default_tab)
		self.title = text
		
		
	def on_start(self):
		lst = self.root.ids.list
		for i in range(1,31):
			list_item = item
			lst.add_widget(Builder.load_string(list_item))
	
	def show_more(self):
		self.title = "Wait for more :)"
		
	def press(self, obj):
		print(f"contact list: {obj}")
		#print("User tried to open a contact but failed.")



if __name__ == "__main__":
	MainApp().run()